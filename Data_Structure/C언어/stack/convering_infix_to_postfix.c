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

int getpriority(char exp) {
	if (exp == '*' || exp == '/')
		return 3;
	else if (exp == '+' || exp == '-')
		return 2;
	else if (exp == ')' || exp == '(')
		return 1;
	else
		return 0;
}

bool comparepriority(char op1, char op2) {
	int pr1 = getpriority(op1);
	int pr2 = getpriority(op2);

	if (pr1 >= pr2)
		return true;
	else
		return false;
}

void infix2postfix(char* exp, int len) {
	Stack stack;
	initstack(&stack);

	for (int i = 0; i < len; i++) {
		if (isdigit(exp[i]))
			printf("%c", exp[i]);

		else if (exp[i] == '(')
			push(&stack, '(');
		
		else if (exp[i] == ')') {
			while (!peek(&stack) == '(') {
				printf("%c", peek(&stack));
				pop(&stack);
			}
			printf("%c", peek(&stack));
			pop(&stack);
			pop(&stack);
		}
		
		else {
			while (!isempty(&stack) && comparepriority(peek(&stack), exp[i])) {
				printf("%c", peek(&stack));
				pop(&stack);
			}
			push(&stack, exp[i]);
		}
	}
	while (!isempty(&stack)) {
		printf("%c", peek(&stack));
		pop(&stack);
	}
	printf("\n");
}

int main() {
	char exp[11] = { '(','3','+','(','4','-','1',')',')','*','5' };
	infix2postfix(exp, 11);
	return 0;

