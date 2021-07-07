#include <stdio.h>
#define MAX_STACK 100

#define SWAP(a, b, type) do { \
    type temp; \
    temp = a;  \
    a = b;     \
    b = temp;  \
} while (0)

typedef int Data;

void selection(Data* list, int n) {
	for (int i = 0; i < n - 1; i++) {
		int min = i;
		for (int j = i + 1; j < n; j++) {
			if (list[min] > list[j])
				min = j;
		}
		SWAP(list[i], list[min], int);
	}
}
