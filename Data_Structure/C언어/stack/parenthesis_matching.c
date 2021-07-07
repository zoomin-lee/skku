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

bool isparanbalanced(char* exp, int len) {
	Stack stack;

	initstack(&stack);
	for (int i = 0; i < len; i++) {
		if (exp[i] == '(')
			push(&stack, exp[i]);
		else if (exp[i] == ')') {
			if (isempty(&stack))
				return false;
			pop(&stack);
		}
	}
	if (isempty(&stack))
		return true;
	else return false;
}

//int main() {
//	char exp[8] = "()(())()";
//	bool a = isparanbalanced(exp, 8);
//	printf("%s\n", a ? "true" : "false");
//}