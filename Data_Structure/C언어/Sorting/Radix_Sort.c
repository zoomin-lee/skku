typedef int Data;

void radix(Data* list, int n, int exp) {
	Data count[10] = { 0 };
	Data output[6];
	for (int i = 0; i < n; i++)
		count[(list[i] / exp) % 10]++;

	for (int i = 1; i < 7; i++)
		count[i] += count[i - 1];

	for (int i = n - 1; i >= 0; i--) {
		output[count[(list[i] / exp) % 10] - 1] = list[i];
		count[(list[i] / exp) % 10]--;
	}

	for (int i = 0; i < n; i++) {
		list[i] = output[i];
	}
}

void radix_sort(Data* list, int n) {
	int max = list[0];

	for (int i = 0; i < 5; i++) {
		if (list[i] > max)
			max = list[i];
	}

	for (int exp = 1; max / exp > 0; exp *= 10)
		radix(list, 5, exp);
}

int main() {
	int list[5] = { 12,22,34,16,46 };

	radix_sort(list, 5);

	for (int i = 0; i < 5; i++)
		printf("%d ", list[i]);
}