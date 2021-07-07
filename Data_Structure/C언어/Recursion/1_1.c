#include <stdio.h>

int rsum(int n) {
	if (n == 0)
		return 0;
	else if (n % 3 != 0)
		return rsum(n - n % 3);
	else
		return rsum(n - 3) + n;
}

int findMax(int* arr, int n) {
	int max = arr[0];
	for (int i = 1; i < n; i++) {
		if (arr[i] > max)
			max = arr[i];
	}
	return max;
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

void rprint(char* s, int n) {
	if (n == 0)
		return;
	else {
		printf("%c", s[n - 1]);
		return rprint(s, n - 1);
	}
}

void binary(int n) {
	if (n == 0)
		return;
	else {
		binary(n / 2);
		print("%d", n%2);
	}
}

int rpower(int x, int n) {
	if (n == 0)
		return 1;
	else
		return x * rpower(x, n - 1);
}

int rpower2(int x, int n) {
	if (n == 0)
		return 1;
	else if (n % 2 == 0) {
		int m = rpower2(x, n / 2);
		return m * m;
	}
	else
		return x * rpower2(x, n - 1);
}

int main() {
	int a, b, c;
	a = S(3);
	printf("%d\n", a);

	b = rsum(7);
	printf("%d\n", b);

	int arr1[5] = { 1,6,4,3,2 };
	c = rfindMax(arr1, 5);
	printf("%d\n", c);

}