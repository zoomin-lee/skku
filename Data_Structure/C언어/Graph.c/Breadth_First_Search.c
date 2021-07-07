#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE 100

typedef struct _gnode {
	int id;
	struct _gnode* next;
} GNode;

typedef struct {
	int num;
	GNode** heads;
}Graph;

typedef enum {
	false, true
} bool;

typedef int Data;

typedef struct {
	int front, rear;
	Data items[MAX_QUEUE];
} Queue;

void initqueue(Queue* p) {
    p->front = p->rear = 0;
}

bool isfull(Queue* p) {
    return p->front == (p->rear + 1) % MAX_QUEUE;
}

bool isempty(Queue* p) {
    return p->front == p->rear;
}

Data peek(Queue* p) {
    if (isempty(p))
        exit(1);
    return p->items[p->front];
}

void enqueue(Queue* p, Data item) {
    if (isfull(p))
        exit(1);
    p->items[p->rear] = item;
    p->rear = (p->rear + 1) % MAX_QUEUE;
}

void dequeue(Queue* p) {
    if (isempty(p))
        exit(1);
    p->front = (p->front + 1) % MAX_QUEUE;
}

void creategraph(Graph* pgraph, int num) {
	pgraph->num = num;
	pgraph->heads = (GNode**)malloc(sizeof(GNode*) * num);

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
	GNode* newnode1, * newnode2, * cur;

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

void BFS(Graph* pgraph) {
	Queue queue;
	initqueue(&queue);

	bool* visited = (bool*)malloc(sizeof(bool) * pgraph->num);
	for (int i = 0; i < pgraph->num; i++)
		visited[i] = false;

	enqueue(&queue, 0);

	while (!isempty(&queue)) {
		GNode* cur;
		int vtx = peek(&queue);
		dequeue(&queue);

		if (visited[vtx]) continue;
		else {
			visited[vtx] = true;
			printf("%d ", vtx);
		}

		cur = pgraph->heads[vtx]->next;
		while (cur != NULL) {
			if (!visited[cur->id])
				enqueue(&queue, cur->id);
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
	BFS(&g);
	destroygraph(&g);
	return 0;
}