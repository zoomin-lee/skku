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
} Dequeue;

typedef struct {
    int front, rear;
    Data items[MAX_QUEUE];
} Queue;

typedef struct {
    int top;
    Data items[MAX_QUEUE];
} Stack;

void initqueue(Dequeue* p) {
    p->front = p->rear = 0;
}

bool isfull(Dequeue* p) {
    return p->front == (p->rear + 1) % MAX_QUEUE;
}

bool isempty(Dequeue* p) {
    return p->front == p->rear;
}

Data peekrear(Dequeue* p) {
    if (isempty(p))
        exit(1);
    return p->items[p->rear];
}

//front가 공백을 가르치고 있는 pointer
Data peekfront(Dequeue* p) {
    if (isempty(p))
        exit(1);
    return p->items[(p->front + 1) % MAX_QUEUE];
}

void addrear(Dequeue* p, Data item) {
    if (isfull(p))
        exit(1);
    p->items[p->rear] = item;
    p->rear = (p->rear + 1) % MAX_QUEUE;
}

void addfront(Dequeue* p, Data item) {
    if (isfull(p))
        exit(1);
    p->items[p->front] = item;
    p->rear = (p->front - 1 + MAX_QUEUE) % MAX_QUEUE;
}

void removerear(Dequeue* p) {
    if (isempty(p))
        exit(1);
    p->rear = (p->rear - 1 + MAX_QUEUE) % MAX_QUEUE;
}

void removefront(Dequeue* p) {
    if (isempty(p))
        exit(1);
    p->front = (p->front + 1) % MAX_QUEUE;
}


////////////////////////////stack////////////////////////////////
void initstack(Stack* pstack) {
    pstack->top = -1;
}

bool isfull(Stack* pstack) {
    pstack->top == MAX_QUEUE - 1;
}

bool isempty(Stack* pstack) {
    pstack->top == -1;
}

Data peek(Stack* pstack) {
    if (isempty(pstack))
        exit(-1);
    return pstack->items[pstack->top];
}

void push(Stack* pstack, Data item) {
    if (isfull(pstack))
        exit(-1);
    pstack->items[++(pstack->top)] = item;
}

void pop(Stack* pstack) {
    if (isempty(pstack))
        exit(-1);
    --(pstack->top);
}
//////////////////////////////////////////////////////////

bool checkpalindrome(char* str, int len) {
    Dequeue dep;

    initqueue(&dep);
    for (int i = 0; i < len; i++) {
        addrear(&dep, str[i]);
    }

    while (len > 1) {
        if (peekfront(&dep) == peekrear(&dep)) {
            removefront(&dep), removerear(&dep);
            len -= 2;
        }
        else
            return false;
    }
}

bool checkpalindrome2(char* str, int len) {
    Stack stack;
    Queue queue;

    initqueue(&queue);
    initstack(&stack);

    for (int i = 0; i < len; i++) {
        push(&stack, str[i]);
        addrear(&queue, str[i]);
    }

    while (!isempty(&queue)) {
        if (peek(&stack) == peekfront(&queue)) {
            pop(&stack);
            removefront(&queue);
        }
        else
            return false;
    }
    return true;
}
