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

void reverseprint(char* s, int len) {
	Stack stack;
	char ch;

	initstack(&stack);
	for (int i = 0; i < len; i++)
		push(&stack, s[i]);

	while (!isempty(&stack)) {
		ch = peek(&stack);
		printf("%c", ch);
		pop(&stack);
	}
}

int main() {
	char s[6] = { 'a','b','c','d','e','f' };
	reverseprint(s, 6);
}


