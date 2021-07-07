#include <stdio.h>

typedef int Data;

void merge(Data* list, int left, int mid, int right) {
	int sorted[100] = { 0 };
	int first = left, second = mid + 1, i = left;

	while (first <= mid && second <= right) {
		if (list[first] < list[second])
			sorted[i++] = list[first++];
		else
			sorted[i++] = list[second++];
	}

	if (first > mid)
		for (int j = second; j <= right; j++)
			sorted[i++] = list[j];
	else
		for (int j = first; j <= mid; j++)
			sorted[i++] = list[j];

	for (int j = left; j <= right; j++)
		list[j] = sorted[j];
}

void rmergesort(Data* list, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		rmergesort(list, left, mid);
		rmergesort(list, mid + 1, right);
		merge(list, left, mid, right);
	}
}

void mergesort(Data* list, int n) {
	int right_end;
	for (int size = 1; size < n - 1; size = 2 * size) {
		for (int left_start = 0; left_start < n - 1; left_start += 2 * size) {
			int mid = left_start + size - 1;
			if (left_start + 2 * size - 1 < n - 1)
				right_end = left_start + 2 * size - 1;
			else
				right_end = n - 1;
			merge(list, left_start, mid, right_end);
		}
	}
}

int main() {
	int list[8] = { 7,4,8,1,12,11,3,9 };

	mergesort(list, 5);

	for (int i = 0; i < 5; i++)
		printf("%d ", list[i]);
}