comps = 0

def read_input(filename):
    f = open(filename, 'r')
    unsorted_list = [int(line) for line in f]
    f.close()
    return unsorted_list

def pivot1(unsorted_list, start_index, end_index):
    return start_index

def pivot2(unsorted_list, start_index, end_index):
    cum_sum = 0
    for i in range(start_index, end_index+1):
        cum_sum += unsorted_list[i]
    avg = cum_sum/(end_index-start_index+1)
    closest_avg = unsorted_list[start_index]
    closest_index = start_index
    for i in range(start_index+1, end_index+1):
        if abs(unsorted_list[i]-avg) < abs(closest_avg-avg):
            closest_avg = unsorted_list[i]
            closest_index = i
    return closest_index

def pivot3(unsorted_list, start_index, end_index):
    return end_index

def pivot4(unsorted_list, start_index, end_index):
    mid = int(float(end_index - start_index)/2.0)
    med_set = {unsorted_list[start_index]: start_index,\
            unsorted_list[end_index]: end_index,\
            unsorted_list[mid]: mid}
    med_sorted = [unsorted_list[start_index], unsorted_list[mid], unsorted_list[end_index]]
    med_sorted = sorted(med_sorted)
    return med_set[med_sorted[1]]

def qsort(unsorted_list, pivot_func=pivot1, start_index=0, end_index=-2):
    if end_index == -2:
        end_index = len(unsorted_list)-1
    length = end_index - start_index + 1
    global comps
    comps += (length-1)
    if length < 2:
        return unsorted_list
    if length == 2:
        if unsorted_list[start_index] < unsorted_list[end_index]:
            return unsorted_list
        temp = unsorted_list[start_index]
        unsorted_list[start_index] = unsorted_list[end_index]
        unsorted_list[end_index] = temp
        return unsorted_list

    pivot = pivot_func(unsorted_list, start_index, end_index)
    pivot_val = unsorted_list[pivot]
    unsorted_list[pivot] = unsorted_list[start_index]
    unsorted_list[start_index] = pivot_val
    pivot = start_index

    i = start_index+1
    while i <= end_index:
        if unsorted_list[i] < pivot_val:
            unsorted_list[pivot] = unsorted_list[i]
            unsorted_list[i] = unsorted_list[pivot+1]
            pivot += 1
            unsorted_list[pivot] = pivot_val
        i += 1
    unsorted_list = qsort(unsorted_list, pivot_func, start_index, pivot-1)
    unsorted_list = qsort(unsorted_list, pivot_func, pivot+1, end_index)
    return unsorted_list

def test_qsort():
    global comps
    a = [1, 6, 7, 8, 5, 0, 3, 4, 2]
    big_test = read_input('QuickSort.txt')

    tests = [a, big_test]
    pivot_functions = [pivot1, pivot2, pivot3, pivot4]

    print 'input runtime'
    for test in tests:
        for pivot_f in pivot_functions:
            temp = test[:]
            comps = 0
            qsort(temp, pivot_f)
            print len(test), comps

def main():
    test_qsort()

if __name__ == "__main__":
    main()
