#include <stdio.h>
#include <stdlib.h>
#define MAX_STACK 100

typedef struct _GNode {
	int id;
	struct _GNode* next;
} GNode;

typedef struct {
	int num;
	GNode** heads;
}Graph;

typedef int Data;

typedef enum {
	false, true
}bool;

typedef struct {
	Data items[MAX_STACK];
	int top;
}Stack;

void initstack(Stack* pstack) {
	pstack->top = -1;
}

bool isempty(Stack* pstack) {
	return pstack->top == -1;
}

bool isfull(Stack* pstack) {
	return pstack->top == MAX_STACK - 1;
}


void creategraph(Graph* pgraph, int num) {
	pgraph->num = num;
	pgraph->heads = (GNode**)malloc(sizeof(GNode*)* num);

	for (int i = 0; i < num; i++) {
		pgraph->heads[i] = (GNode*)malloc(sizeof(GNode));
		pgraph->heads[i]->next = NULL;
	}
}

void destroygraph(Graph* pgraph) {
	for (int i = 0; i < pgraph->num; i++) {
		GNode* cur = pgraph->heads[i];
		while (cur != NULL) {
			GNode* temp = cur;
			cur = cur->next;
			free(temp);
		}
	}
	free(pgraph->heads);
}

void addedge(Graph* pgraph, int src, int dest) {
	GNode* newnode1, * newnode2, *cur;

	newnode1 = (GNode*)malloc(sizeof(GNode));
	newnode1->id = dest;
	newnode1->next = NULL;

	cur = pgraph->heads[src];
	while (cur->next != NULL)
		cur = cur->next;
	cur->next = newnode1;

	newnode2 = (GNode*)malloc(sizeof(GNode));
	newnode2->id = src;
	newnode2->next = NULL;

	cur - pgraph->heads[dest];
	while (cur->next != NULL)
		cur = cur->next;
	cur->next = newnode2;
}

Data push(Stack* stack, Data item) {
	if (isfull(stack))
		exit(1);
	stack->items[++(stack->top)] = item;
}

void pop(Stack* stack) {
	if (isempty(stack))
		exit(1);
	--(stack->top);
}

Data peek(Stack* stack) {
	if (isempty(stack))
		exit(1);
	return stack->items[stack->top];
}

void DFS(Graph* pgraph) {
	Stack stack;
	bool* visited = (bool*)malloc(sizeof(bool) * pgraph->num);

	for (int i = 0; i < pgraph->num; i++)
		visited[i] = false;

	initstack(&stack);
	push(&stack, 0);
	while (!isempty(&stack)) {
		GNode* cur;
		int vtx = peek(&stack);
		pop(&stack);

		if (visited[vtx]) continue;
		else {
			visited[vtx] = true;
			printf("%d ", vtx);
		}
		cur = pgraph->heads[vtx]->next;
		while (cur != NULL) {
			if (!visited[cur->id])
				push(&stack, cur->id);
			cur = cur->next;
		}
	}
}

int main() {
	Graph g;
	creategraph(&g, 5);
	addedge(&g, 0, 1);
	addedge(&g, 0, 2);
	addedge(&g, 0, 4);
	addedge(&g, 1, 2);
	addedge(&g, 2, 3);
	addedge(&g, 2, 4);
	addedge(&g, 3, 4);
	DFS(&g);
	destroygraph(&g);
	return 0;
}