#include <stdio.h>

int bsearch(int arr[], int low, int high, int target) {
	if (low > high)
		return -1;
	else {
		int mid = (low + high) / 2;
		if (target == arr[mid])
			return mid;
		else if (target < arr[mid])
			bsearch(arr, low, mid - 1, target);
		else
			bsearch(arr, mid + 1, high, target);
	}
}

int main() {
	int a;
	int arr[9] = { 1,5,17,25,27,29,31,35,38 };

	a = bsearch(arr, 0, 8, 31);
	printf("%d", a);
}