c = 0

def unimodal_max(unimodal_list):
    global c
    if len(unimodal_list) == 0:
        return unimodal_list
    if len(unimodal_list) == 1:
        return unimodal_list[0]

    c += 1

    mid = int(len(unimodal_list)/2.0)
    left = unimodal_list[:mid]
    right = unimodal_list[mid:]
    
    left_left_inc = (left[1]-left[0]) > 0
    left_right_inc = (left[len(left)-1] - left[len(left)-2]) > 0

    right_left_inc = (right[1]-right[0]) > 0
    right_right_inc = (right[len(right)-1] - right[len(right)-2]) > 0

    if left_left_inc != left_right_inc:
        return unimodal_max(left)
    elif right_left_inc != right_right_inc:
        return unimodal_max(right)
    elif left[len(left)-1] > right[0]:
        return left[len(left)-1]
    return right[0]

def test_unimodal_max():
    global c
    a = [1, 2, 3, 4, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8]
    print unimodal_max(a)
    print len(a), c
    c = 0
    b = range(1, 1032)
    b.extend(range(3333, 4, -2))
    print unimodal_max(b)
    print len(b), c


def main():
    test_unimodal_max()

if __name__ == "__main__":
    test_unimodal_max()
