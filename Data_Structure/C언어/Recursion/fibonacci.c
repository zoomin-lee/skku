#include <stdio.h>

int fibo(int n) {
	if (n == 1 || n == 2)
		return 1;
	else {
		int prev = 1, cur = 1, next = 1;
		for (int i = 3; i <= n; i++) {
			prev = cur, cur = next;
			next = prev + cur;
		}
		return next;
	}
}

int rfibo(int n) {
	if (n == 1 || n == 2)
		return 1;
	else {
		return rfibo(n - 1) + rfibo(n - 2);
	}
}