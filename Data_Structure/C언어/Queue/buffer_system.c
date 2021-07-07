#include <stdio.h>
#include <ctype.h>

#define MAX_QUEUE   100

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

void producer(Queue* buffer, Data data) {
    if (lock(buffer) == false) {
        if (!isfull(buffer))
            enqueue(buffer, data);
        unlock(buffer);
    }
}

void consumer(Queue* buffer, Data data) {
    if (lock(buffer) == false) {
        if (!isempty(buffer)) {
            Data data = Peek(buffer);
            dequeue(buffer);
        }
        unlock(buffer);
    }
}

int main() {
    Queue buffer;
    initqueue(&buffer);
}