#include <stdio.h>

typedef enum {
	false, true
} bool;

typedef int Data;

typedef struct _Node{
	Data item;
	struct _Node* next;
} Node;

typedef struct {
	Node* top;
}Dstack;

void initstack(Dstack* pstack) {
	pstack->top = NULL;
}

bool isempty(Dstack* pstack) {
	return pstack->top == NULL;
}

Data peek(Dstack* pstack) {
	if (isempty(pstack))
		exit(1);
	return pstack->top->item;
}

void push(Dstack* pstack, Data item) {
	Node* newnode = (Node*)malloc(sizeof(Node));
	newnode->item = item;
	newnode->next = pstack->top;
	pstack->top = newnode;
}

void pop(Dstack* pstack) {
	if (isempty(pstack))
		exit(1);
	Node* temp = pstack->top;
	pstack->top = temp->next;
	free(temp);
}

