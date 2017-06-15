import random

def rselect(unsorted_list, index_select, *kwargs):
    if len(kwargs) < 2 and len(kwargs) > 0:
        print "error with input arguments"
    elif len(kwargs) == 2:
        start = kwargs[0]
        end = kwargs[1]
    else:
        start = 0
        end = len(unsorted_list)-1

    if (end-start+1) == 1:
        return unsorted_list[index_select]
    pivot = int(random.random()*float(end-start) + 0.5) + start
    pivot_val = unsorted_list[pivot]
    unsorted_list[pivot] = unsorted_list[start]
    unsorted_list[start] = pivot_val
    pivot = start
    for i in range(start+1, end+1):
        if unsorted_list[i] < pivot_val:
            unsorted_list[pivot] = unsorted_list[i]
            unsorted_list[i] = unsorted_list[pivot+1]
            unsorted_list[pivot+1] = pivot_val
            pivot += 1
    if pivot < index_select:
        return rselect(unsorted_list, index_select, pivot+1, end)
    if pivot > index_select:
        return rselect(unsorted_list, index_select, start, pivot-1)
    return pivot_val

def unsorted_median(unsorted_list):
    if len(unsorted_list) % 2 == 0:
        return (rselect(unsorted_list, len(unsorted_list)/2) +\
                rselect(unsorted_list, len(unsorted_list)/2-1))/2.0
    return rselect(unsorted_list, int(len(unsorted_list)/2))

def qsort(unsorted_list, *kwargs):
    if len(kwargs) == 2:
        start = kwargs[0]
        end = kwargs[1]
    else:
        start = 0
        end = len(unsorted_list)-1
    length = end-start+1
    if length < 2:
        return
    if length == 2:
        if unsorted_list[start] > unsorted_list[end]:
            swap = unsorted_list[start]
            unsorted_list[start] = unsorted_list[end]
            unsorted_list[end] = swap
        return

    pivot = int(random.random()*float(length-1)+0.5)+start
    pivot_val = unsorted_list[pivot]
    unsorted_list[pivot] = unsorted_list[start]
    unsorted_list[start] = pivot_val
    pivot = start

    for i in range(start+1, end+1):
        if unsorted_list[i] < pivot_val:
            unsorted_list[pivot] = unsorted_list[i]
            unsorted_list[i] = unsorted_list[pivot+1]
            unsorted_list[pivot+1] = pivot_val
            pivot += 1

    qsort(unsorted_list, 0, pivot-1)
    qsort(unsorted_list, pivot+1, end)

def test_rselect():
    a = [5,3,1,4,2,6,7]
    b = [13, 4, 2, 7, 6, 1, 9, 11, 15, 20]
    print rselect(a, 3)
    print sorted(a)[3]
    print rselect(b, 3)
    print sorted(b)[3]

def test_qsort():
    c = [5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11]
    print c
    qsort(c)
    print c


def test_unsorted_median(unsorted_list):
    sorted_list = sorted(unsorted_list)
    median_test = unsorted_median(unsorted_list)
    if len(unsorted_list)%2 == 1:
        median = sorted_list[int(len(unsorted_list)/2)]
    else:
        median = (sorted_list[len(unsorted_list)/2] +\
                sorted_list[len(unsorted_list)/2-1])/2.0
    return (median == median_test, median_test, median)

def test_unsorted_medians():
    c = [5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11]
    d = [1, 1, 3, 5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11, 8, 23]
    e = [1, 1, 3, 5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11, 9, 23]

    all_tests = [c, d]
    all_tests_passed = True
    failed_tests = []

    for i in range(len(all_tests)):
        test = all_tests[i]
        (passed, median_test, median)  = test_unsorted_median(test)
        all_tests_passed &= passed
        if not passed:
            failed_tests.append((str(i), str(test), \
                    str(median_test), str(median)))

    if all_tests_passed:
        print "unsorted_median: all test cases pass"
    else:
        test_output = open("unsorted_medians_tests.log", 'w')
        test_output.write("Index\tFailed test case\tReturned median")
        test_output.write("\tActual median\n")
        for failed_test in failed_tests:
            test_output.write("\t".join(failed_test))
        test_output.close()
        print "unsorted_median:", len(failed_tests), "test case(s) failed"
        print "error(s) written to unsorted_median_tests.log"

def main():
    test_rselect()
    #test_qsort()
    #test_unsorted_medians()

if __name__ == "__main__":
    main()
