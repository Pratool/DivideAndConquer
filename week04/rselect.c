#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int rselect(int *unsorted_list, unsigned int list_length, int index_select,
        int start, int end) {
    if (end-start+1 == 1)
        return unsorted_list[index_select];

    srand((unsigned int) time(NULL));
    int pivot = (rand() % (end-start)) + start;
    int pivot_val = unsorted_list[pivot];
    unsorted_list[pivot] = unsorted_list[start];
    unsorted_list[start] = pivot_val;
    pivot = start;
    for (int i = start+1; i <= end; i++) {
        if (unsorted_list[i] < pivot_val) {
            unsorted_list[pivot] = unsorted_list[i];
            unsorted_list[i] = unsorted_list[pivot+1];
            unsorted_list[pivot+1] = pivot_val;
            pivot++;
        }
    }

    if (pivot < index_select)
        return rselect(unsorted_list, list_length, index_select, pivot+1, end);
    if (pivot > index_select)
        return rselect(unsorted_list, list_length, index_select, start, pivot-1);
    return pivot_val;
}

void test_rselect() {
    int a[] = {5, 3, 1, 4, 2, 6, 7};
    int a_size = sizeof(a)/sizeof(a[0]);
    int b[] = {13, 4, 2, 7, 6, 1, 9, 11, 15, 20};
    int b_size = sizeof(b)/sizeof(b[0]);
    printf("position 3: %d\n", rselect(a, a_size, 3, 0, a_size-1));
    printf("position 3: %d\n", rselect(b, b_size, 3, 0, b_size-1));
}

int main() {
    test_rselect();
    return 0;
}
