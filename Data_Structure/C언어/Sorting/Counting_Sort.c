typedef int Data;

void counting(Data* list, int n) {
	Data count[7] = { 0 };
	Data output[6];
	for (int i = 0; i < n; i++)
		count[list[i]]++;

	for (int i = 1; i < 7; i++)
		count[i] += count[i - 1];

	for (int i = n - 1; i >= 0; i--) {
		output[count[list[i]] - 1] = list[i];
		count[list[i]]--;
	}

	for (int i = 0; i < n; i++) {
		list[i] = output[i];
	}
}