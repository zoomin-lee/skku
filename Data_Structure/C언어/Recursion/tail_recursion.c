#include <stdio.h>

int rsum(int n) {
	if (n == 0)
		return 0;
	else
		return rsum(n-1) + n;
}

int rsumtail(int n, int sum) {
	if (n == 0)
		return sum;
	else
		return rsum2(n - 1, sum + n);
}




int rfibo(int n) {
	if (n == 1 || n == 2)
		return 1;
	else {
		return rfibo(n - 1) + rfibo(n - 2);
	}
}

int rfibotail(int n, int prev, int cur) {
	if (n == 1 || n == 2)
		return cur;
	else {
		return rfibotail(n - 1, cur, prev + cur);
	}
}



int rfindMax(int* arr, int n) {
	if (n == 1)
		return arr[0];
	else {
		int max = rfindMax(arr, n - 1);
		if (max < arr[n - 1])
			return arr[n - 1];
		else
			return max;
	}
}

int rfindMaxtail(int* arr, int n, int max) {
	if (n == 1)
		return max;
	else {
		if (max < arr[n - 1])
			max = arr[n - 1];

		return rfindMaxtail(arr, n - 1, max);
	}
}