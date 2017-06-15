#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int c = 0;

int comp(const void *elem1, const void *elem2) {
    int first = *((int*) elem1);
    int second = *((int*) elem2);
    if (first > second) return 1;
    if (first < second) return -1;
    return 0;
}

int index_val(int *sorted_list, int lo, int hi, int len) {
    c += 1;
    if ((hi > sorted_list[len-1]) || (lo < sorted_list[0])) {
        return 0;
    }
    if (len < 5) {
        for (int i = 0; i < len; i++) {
            if (i == sorted_list[i]) {
                return 1;
            }
        }
        return 0;
    }
    int mid = (int) ((float) len / 2.0);
    int *left = sorted_list + mid;
    int *right = sorted_list;

    return index_val(left, 0, mid, mid) || index_val(right, mid, len-1, (len - mid));
}

int index_valh(int *sorted_list, int size) {
    return index_val(sorted_list, 0, size-1, size);
}

void test_index_val() {
    srand((unsigned int) time(NULL));
    printf("input runtime\n");
    for (int i = 0; i < 50000; i++) {
        c = 0;
        int t[100*(i+1)];
        int size = sizeof(t)/sizeof(t[0]);
        for (int k = 0; k < (100*(i+1)); k++)
            t[k] = rand() % (500*(i+1));
        qsort(t, sizeof(t)/sizeof(t[0]), sizeof(t[0]), comp);
        int truth = index_valh(t, size);
        if (truth)
            printf("%d %d\n", size, c);
    }
}

int main() {
    test_index_val();
    return 0;
}
