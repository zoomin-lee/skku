#include <stdio.h>

typedef int Data;

#define SWAP(a, b, type) do { \
    type temp; \
    temp = a;  \
    a = b;     \
    b = temp;  \
} while (0)

void insertion(Data* list, int n) {
	for (int i = 0; i < n - 1; i++) {
		for (int j = i + 1; j > 0; j--) {
			if (list[j] < list[j - 1])
				SWAP(list[j], list[j - 1], int);
			else
				break;
		}
	}
}
