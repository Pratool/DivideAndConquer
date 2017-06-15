def merge_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list

    sorted_list = []
    mid = int(len(unsorted_list)/2.0 + 0.5)
    left = merge_sort(unsorted_list[:mid])
    right = merge_sort(unsorted_list[mid:])
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1
    i = l if l < len(left) else r
    rest = left if l < len(left) else right
    while i < len(rest):
        sorted_list.append(rest[i])
        i += 1

    return sorted_list

def merge_sort_tests():
    a = [5, 4, 3, 2, 1]
    b = [4, 1, 39, 2, 0, 8, -4]
    c = [1, 3, 5, 2, 4, 5, 6, 8, 7]

    print 'a:', a
    print 'sorted a:', merge_sort(a)
    print 'b:', b
    print 'sorted b:', merge_sort(b)
    print 'c:', c
    print 'sorted c:', merge_sort(c)

def main():
    merge_sort_tests()

if __name__ == "__main__":
    main()
