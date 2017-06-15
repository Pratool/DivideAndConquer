#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <limits.h>

#define CHUNK 5

// Something in this application is written improperly
// This is supposed to run the Deterministic Selection algorithm (O(n) time)

int comp(const void *elem1, const void *elem2) {
    int first = *((int*) elem1);
    int second = *((int*) elem2);
    if (first > second) return 1;
    if (first < second) return -1;
    return 0;
}

int dselect(int *unsorted_list, unsigned int list_length, int index_select,
        int start, int end) {
    for (unsigned int i = start; i <= (unsigned int) end ; i++)
        printf("%d ", unsorted_list[i]);
    printf("\n%d %d %d %d\n", list_length, index_select, start, end);
    if (end-start+1 == 1)
        return unsorted_list[index_select];
    if (end-start+1 <= CHUNK) {
        int sorted_list[end-start+1];
        for (int i = 0; i < start-end+1; i++)
            sorted_list[i] = unsorted_list[start+i];
        qsort(sorted_list, sizeof(sorted_list)/sizeof(sorted_list[0]),
                sizeof(sorted_list[0]), comp);
        return sorted_list[index_select];
    }

    // Length over the array that we are examining currently
    // (this value can be less than list_length)
    int length = end-start+1;

    int med_recurse[(int) ((length+4)/5)];
    int med_recurse_index = 0;
    for (int i = start; i <= end; i += 5) {
        int chunk_size = end-i+1 > CHUNK ? CHUNK : length-i;
        int list_chunk[chunk_size];
        printf("List chunk: ");
        for (int k = 0; k < chunk_size; k++) {
            list_chunk[k] = unsorted_list[i+k];
            printf("%d ", list_chunk[k]);
        }
        printf("\n");
        qsort(list_chunk, sizeof(list_chunk)/sizeof(list_chunk[0]),
                sizeof(list_chunk[0]), comp);
        int mid = (int) (((float) chunk_size)/2.0 - 0.5);
        med_recurse[med_recurse_index] = list_chunk[mid];
        med_recurse_index++;
    }

    printf("medrecurse: ");
    for (unsigned int i = 0; i < (sizeof(med_recurse)/sizeof(med_recurse[0])); i++)
        printf("%d ", med_recurse[i]);
    printf("\n");

    int pivot = (int) (((float) (sizeof(med_recurse)/sizeof(med_recurse[0])))/2.0 - 0.5);
    printf("pivot: %d\n", pivot);
    int pivot_val = dselect(med_recurse, sizeof(med_recurse)/sizeof(med_recurse[0]),
            pivot, 0, sizeof(med_recurse)/sizeof(med_recurse[0])-1);

    unsorted_list[pivot] = unsorted_list[start];
    unsorted_list[start] = pivot_val;
    pivot = start;
    for (int i = start; i <= end; i++)
        printf("unsorted %d ", unsorted_list[i]);
    printf("\n");
    for (int i = start+1; i <= end; i++) {
        if (unsorted_list[i] < pivot_val) {
            unsorted_list[pivot] = unsorted_list[i];
            unsorted_list[i] = unsorted_list[pivot+1];
            unsorted_list[pivot+1] = pivot_val;
            pivot++;
        }
    }
    printf("\n");

    if (pivot < index_select) {
        if (end-pivot <= CHUNK)
            return dselect(unsorted_list, list_length, index_select-pivot-1, pivot+1, end);
        return dselect(unsorted_list, list_length, index_select, pivot+1, end);
    }
    if (pivot > index_select) {
        if (end-pivot <= CHUNK)
            return dselect(unsorted_list, list_length, index_select-start, start, pivot-1);
        return dselect(unsorted_list, list_length, index_select, start, pivot-1);
    }
    return pivot_val;
}

void test_dselect() {
    int a[] = {5, 3, 1, 4, 2, 6, 7};
    int a_size = sizeof(a)/sizeof(a[0]);
    //int b[] = {13, 4, 2, 7, 6, 1, 9, 11, 15, 20};
    //int b_size = sizeof(b)/sizeof(b[0])
    printf("position 3: %d\n", dselect(a, a_size, 3, 0, a_size-1));
    //printf("position 3: %d\n", dselect(b, b_size, 3, 0, b_size-1));
}

int main() {
    test_dselect();
    return 0;
}
