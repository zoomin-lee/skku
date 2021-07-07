#include<stdio.h>

typedef enum {
	false, true
} bool;

typedef int Data;

typedef struct _Node {
	Data item;
	struct _Node* next;
}Node;

typedef struct {
	Node* front;
	Node* rear;
}Dqueue;

void initqueue(Dqueue* pqueue) {
	pqueue->front = pqueue->rear = NULL;
}

bool isempty(Dqueue* pqueue) {
	return pqueue->front == NULL;
}

Data peek(Dqueue* pqueue) {
	if (isempty(pqueue))
		exit(1);
	return pqueue->front->item;
}

void enqueue(Dqueue* pqueue, Data item) {
	Node* newnode = (Node*)malloc(sizeof(Node));
	newnode->item = item;

	if (isempty(pqueue))
		pqueue->front = pqueue->rear = newnode;
	else {
		pqueue->rear->next = newnode;
		pqueue->rear = newnode;
	}
}

void dequeue(Dqueue* pqueue) {
	Node* temp;
	if (isempty(pqueue))
		exit(1);

	temp = pqueue->front;
	if (temp->next == NULL)
		pqueue->front = pqueue->rear = NULL;
	else
		pqueue->front = temp->next;
	free(temp);
}