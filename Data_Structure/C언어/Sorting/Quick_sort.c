#include <stdio.h>
#define MAX_STACK 100

#define SWAP(a, b, type) do { \
    type temp; \
    temp = a;  \
    a = b;     \
    b = temp;  \
} while (0)

typedef int Data;

typedef enum {
	false, true
} bool;

typedef struct {
	Data items[MAX_STACK];
	int top;
} Stack;

void initstack(Stack* stack) {
	stack->top = -1;
}

bool isempty(Stack* stack) {
	return stack->top == -1;
}

bool isfull(Stack* stack) {
	return stack->top == MAX_STACK - 1;
}

Data peek(Stack* stack) {
	return stack->items[stack->top];
}

void push(Stack* stack, Data item) {
	if (isfull(stack))
		exit(1);
	stack->items[++(stack->top)] = item;
}

void pop(Stack* stack) {
	if (isempty(stack))
		exit(1);
	--(stack->top);
}

int partitioning(Data* list, int left, int right) {
	int low = left + 1, high = right;
	while (1) {
		while (low < right && list[low] < list[left]) {
			low++;
		}
		while (high > left && list[high] >= list[left]) {
			high--;
		}
		if (low < high)
			SWAP(list[low], list[high], int);
		else
			break;
	}
	SWAP(list[left], list[high], int);
	return high;
}

void rquick(Data* list, int left, int right) {
	if (left < right) {
		int mid = partitioning(list, left, right);
		rquick(list, left, mid - 1);
		rquick(list, mid + 1, right);
	}
}

void quick(Data* list, int n) {
	Stack stack;
	int low, high;
	initstack(&stack);
	push(&stack, 0), push(&stack, n - 1);

	while (!isempty(&stack)) {
		high = peek(&stack), pop(&stack);
		low = peek(&stack), pop(&stack);

		int mid = partitioning(list, low, high);

		if (mid > low) {
			push(&stack, low);
			push(&stack, mid);
		}

		if (mid + 1 < high) {
			push(&stack, mid + 1);
			push(&stack, high);
		}
	}
}