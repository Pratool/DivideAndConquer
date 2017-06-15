import random

c = 0
def index_val(sorted_list, lo, hi):
    global c
    c += 1
    if hi > sorted_list[len(sorted_list)-1] or lo < sorted_list[0]:
        return False
    if len(sorted_list) < 5:
        for i in range(len(sorted_list)):
            if i == sorted_list[i]:
                return True
        return False

    mid = int(len(sorted_list)/2.0)
    left = sorted_list[:mid]
    right = sorted_list[mid:]
    return index_val(left, 0, mid) or index_val(right, mid, len(sorted_list)-1)

def index_valh(sorted_list):
    return index_val(sorted_list, 0, len(sorted_list)-1)

def test_index_val():
    global c
    #a = range(4, 60, 4)
    #print a
    #print index_valh(a)
    #print len(a), c
    print 'input', 'runtime'
    for i in range(5000):
        c = 0
        t = sorted([int(random.random()*500.0*(i+1)) for j in range(100*(i+1))])
        truth = index_valh(t)
        if truth:
            #print truth
            print len(t), c

def main():
    test_index_val()

if __name__ == "__main__":
    main()
