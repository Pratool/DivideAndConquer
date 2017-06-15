import math
import random

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

def compare_points_x(p, q):
    if p[0] == q[0]:
        return 0
    if p[0] > q[0]:
        return 1
    return -1

def compare_points_y(p, q):
    if p[1] == q[1]:
        return 0
    if p[1] > q[1]:
        return 1
    return -1

def compare_points(p, q):
    dp = distance(p, (0, 0))
    dq = distance(q, (0, 0))
    if dp == dq:
        return 0
    if dp > dq:
        return 1
    return -1

def distance(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)

def merge_sort(unsorted_list, compare):
    if len(unsorted_list) < 2:
        return unsorted_list

    mid = int(len(unsorted_list)/2.0 + 0.5)
    left = merge_sort(unsorted_list[:mid], compare)
    right = merge_sort(unsorted_list[mid:], compare)

    l = 0
    r = 0
    sorted_list = []

    for i in range(len(unsorted_list)):
        if r >= len(right) or (l < len(left) and compare(left[l], right[r]) < 1):
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1

    return sorted_list

def closest_split_pair(pairs_x_sorted, pairs_y_sorted, delta):
    if len(pairs_x_sorted) < 2:
        return (-float("inf"), +float("inf"))
    if len(pairs_x_sorted) == 2:
        return (pairs_x_sorted[0], pairs_x_sorted[1])

    mid = int(len(pairs_x_sorted)/2.0)
    xbar = pairs_x_sorted[mid][0]
    if len(pairs_x_sorted)%2 == 0:
        xbar = (pairs_x_sorted[mid][0] + pairs_x_sorted[mid-1][0])/2.0
    x_delta_pairs = []
    y_delta_pairs = []

    for pair in pairs_x_sorted:
        if pair[0] > xbar-delta or pair[0] < xbar+delta:
            x_delta_pairs.append(pair)

    x_delta_pairs_set = set(x_delta_pairs)
    
    for pair in pairs_y_sorted:
        if pair in x_delta_pairs_set:
            y_delta_pairs.append(pair)


    min_distance = +float("inf")
    min_pair = (-float("inf"), +float("inf"))
    for i in range(len(y_delta_pairs)):
        j = 1
        while i+j < len(y_delta_pairs) and j <= 7:
            cur_distance = distance(y_delta_pairs[i], y_delta_pairs[i+j])
            if cur_distance < min_distance:
                min_distance = cur_distance
                min_pair = (y_delta_pairs[i], y_delta_pairs[i+j])
            j += 1

    return min_pair

def closest_pair(pairs_x_sorted, pairs_y_sorted):
    if len(pairs_x_sorted) < 2:
        return ((-float("inf"), -float("inf")), (+float("inf"), +float("inf")))
    if len(pairs_x_sorted) == 2:
        return pairs_x_sorted

    mid = int(len(pairs_x_sorted)/2.0 + 0.5)
    left_x = pairs_x_sorted[:mid]
    right_x = pairs_x_sorted[mid:]
    left_x_set = set(left_x)
    right_x_set = set(right_x)
    left_y = []
    right_y = []

    for pair in pairs_y_sorted:
        if pair in left_x_set:
            left_y.append(pair)
        elif pair in right_x_set:
            right_y.append(pair)

    p_left, q_left = closest_pair(left_x, left_y)
    p_right, q_right = closest_pair(right_x, right_y)
    left_distance = distance(p_left, q_left)
    right_distance = distance(p_right, q_right)

    delta = left_distance if left_distance < right_distance else right_distance

    p_split, q_split = closest_split_pair(pairs_x_sorted, pairs_y_sorted, delta)
    split_distance = distance(p_split, q_split)

    distances = [right_distance, split_distance]
    min_pairs = [(p_right, q_right), (p_split, q_split)]
    min_distance = left_distance
    min_pair = (p_left, q_left)
    for d, p in zip(distances, min_pairs):
        if d < min_distance:
            min_distance = d
            min_pair = p

    return min_pair

def closest_pair_wrapper(pairs):
    pairs_x_sorted = merge_sort(pairs, compare_points_x)
    pairs_y_sorted = merge_sort(pairs, compare_points_y)
    return closest_pair(pairs_x_sorted, pairs_y_sorted)
    
def test_merge_sort():
    a = []
    for i in range(8):
        a = [(int(random.random()*1000.0), int(random.random()*1000.0)) for i in range(8)]

    print a
    print
    print merge_sort(a, compare_points_x)
    print 
    print merge_sort(a, compare_points_y)
    print
    print merge_sort(a, compare_points)

def test_closest_pair(b, test_no):
    b_cp = closest_pair_wrapper(b)

    for pair in b:
        plt.scatter(pair[0], pair[1], color='black', marker='o', s=100)
    for pair in b_cp:
        plt.scatter(pair[0], pair[1], color='red', marker=r'o', s=25)
    plt.title('Closest Pair Test ' + str(test_no) + ', ' + str(len(b)) + ' Points')
    plt.show()

def closest_pair_tests():
    a = []
    j = 1
    while j <= 10:
        a = [(int(random.random()*1000.0), int(random.random()*1000.0)) for i in range(int(8+j))]
        test_closest_pair(a, j)
        j += 1

    b = [(11, 243), (19, 79), (73, 329), (405, 836), (569, 993), (895, 545), (928, 317), (945, 727)]

    test_closest_pair(b, j)

def main():
    style = {'text.usetex': True, 'font.family': 'serif', 'font.serif': ['cmr17'] }
    sns.set(context="poster", style="whitegrid", palette="bright", font_scale=1.5,\
            rc=style)
    closest_pair_tests()

if __name__ == "__main__":
    main()
