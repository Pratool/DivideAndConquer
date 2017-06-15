def import_unsorted_arr(file_name):
    unsorted_arr = []
    f = open(file_name)
    for line in f:
        unsorted_arr.append(int(line))
    return unsorted_arr

def inv_count_sort(unsorted_arr, inv_count = 0):
    if len(unsorted_arr) < 2:
        return (unsorted_arr, 0)

    mid = int(len(unsorted_arr)/2.0 + 0.5)
    left, left_inv = inv_count_sort(unsorted_arr[:mid])
    right, right_inv = inv_count_sort(unsorted_arr[mid:])
    sorted_arr = []

    inv_count += (left_inv + right_inv)

    l = 0
    r = 0
    for k in range(len(unsorted_arr)):
        if r >= len(right) or (l < len(left) and left[l] <= right[r]):
            sorted_arr.append(left[l])
            l += 1
        else:
            sorted_arr.append(right[r])
            r += 1
            inv_count += (len(left)-l)

    return (sorted_arr, inv_count)

def inv_count_sort_test():
    a = [5, 4, 3, 2, 1]
    b = range(6, 0, -1)
    print inv_count_sort(a)
    print inv_count_sort(b)

def main():
    inv_count_sort_test()
    print "From a large integer array file, inversion count:"
    print inv_count_sort(import_unsorted_arr("IntegerArray.txt"))[1]

if __name__ == "__main__":
    main()

