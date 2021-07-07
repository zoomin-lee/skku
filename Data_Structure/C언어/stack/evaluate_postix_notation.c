#include <stdio.h>
#include <ctype.h>
#define MAX_STACK 5

typedef enum {
	false, true
}bool;

typedef int Data;

typedef struct {
	Data items[MAX_STACK];
	int top;
}Stack;


void initstack(Stack* pstack) {
	pstack->top = -1;
}

bool isfull(Stack* pstack) {
	return pstack->top == MAX_STACK - 1;
}

bool isempty(Stack* pstack) {
	return pstack->top == -1;
}

Data peek(Stack* pstack) {
	if (isempty(pstack))
		exit(1);
	return pstack->items[pstack->top];
}

void push(Stack* pstack, Data item) {
	if (isfull(pstack))
		exit(1);
	pstack->items[++(pstack->top)] = item;
}
void pop(Stack* pstack) {
	if (isempty(pstack))
		exit(1);
	--(pstack->top);
}

int evalpostfix(char* exp, int len) {
	Stack stack;
	int op1, op2;
	initstack(&stack);

	for (int i = 0; i < len; i++) {
		if (isdigit(exp[i]))
			push(&stack, exp[i] - '0');
		else {
			op1 = peek(&stack);
			pop(&stack);
			op2 = peek(&stack);
			pop(&stack);
			if (exp[i] == '+')
				push(&stack, op1 + op2);
			else if (exp[i] == '-')
				push(&stack, op1 - op2);
			else if (exp[i] == '*')
				push(&stack, op1 * op2);
			else if (exp[i] == '/')
				push(&stack, op1 / op2);
		}
	}
	return peek(&stack);
}

//int main() {
//	char exp[5] = "23+4*";
//	int a = evalpostfix(exp, 5);
//	printf("%d", a);
//}