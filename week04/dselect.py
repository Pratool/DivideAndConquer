def dselect(unsorted_list, order, *kwargs):
    if len(kwargs) == 0:
        start = 0
        end = len(unsorted_list)-1
    elif len(kwargs) == 2:
        start = kwargs[0]
        end = kwargs[1]
    print unsorted_list
    print len(unsorted_list), order, start, end

    length = end-start+1

    if length < 2:
        return unsorted_list[order]
    if length <= 5:
        sorted_list = []
        for i in range(length):
            sorted_list.append(unsorted_list[start+i])
        sorted_list = sorted(sorted_list)
        return sorted_list[order]

    med_recurse = []

    for i in range(start, end+1, 5):
        temp_list = sorted(unsorted_list[i:i+5])
        print "List chunk:", temp_list
        mid = int(len(temp_list)/2.0-0.5)
        med_recurse.append(temp_list[mid])
    print "medrecurse:", med_recurse
    pivot = int(float(len(med_recurse))/2.0-0.5)
    print "pivot:", pivot
    pivot_val = dselect(med_recurse, pivot)

    unsorted_list[pivot] = unsorted_list[start]
    unsorted_list[start] = pivot_val
    pivot = start

    print "unsorted", unsorted_list
    for i in range(start+1, end+1):
        if unsorted_list[i] < pivot_val:
            unsorted_list[pivot] = unsorted_list[i]
            unsorted_list[i] = unsorted_list[pivot+1]
            unsorted_list[pivot+1] = pivot_val
            pivot += 1

    if pivot < order:
        if end-pivot <= 5:
            return dselect(unsorted_list, order-pivot-1, pivot+1, end)
        return dselect(unsorted_list, order, pivot+1, end)
    if pivot > order:
        if end-pivot <= 5:
            return dselect(unsorted_list, order-start, start, pivot-1)
        return dselect(unsorted_list, order, start, pivot-1)
    return pivot_val

def test_dselect():
    a = [5, 3, 1, 4, 2, 6, 7]
    b = [13, 4, 2, 7, 6, 1, 9, 11, 15, 20]
    c = [5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11]
    d = [1, 1, 3, 5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11, 8, 23]
    e = [1, 1, 3, 5, 4, 3, 7, 9, 13, 21, 25, 63, 12, 11, 9, 23]
    print "value:", dselect(a, 3)
    #print "expected:", sorted(a)[3]
    #print "value:", dselect(b, 3)
    #print "expected:", sorted(b)[3]
    #print "value:", dselect(c, 10)
    #print "expected:", sorted(c)[10]
    #print "value:", dselect(d, 9)
    #print "expected:", sorted(d)[9]

def main():
    test_dselect()

if __name__ == "__main__":
    main()
