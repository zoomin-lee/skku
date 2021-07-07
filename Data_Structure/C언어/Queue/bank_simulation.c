#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_QUEUE	100

typedef enum {
	false, true
} bool;

typedef struct {
	int id;
	int arrival_time;
	int service_time;
}Customer;

typedef Customer Data;

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

#define MAX_SERV_TIME	10

int waited_time = 0;
int served_customers = 0;
int num_customers = 0;

bool arrive_customer() {
	double prob = rand() / (double)RAND_MAX;
	if (prob > 0.5)
		return true;
	else
		return false;
}

void insertcustomer(Queue* queue, int id, int clock) {
	Customer c;

	if (isfull(queue))
		return;

	c.id = id;
	c.arrival_time = clock;
	c.service_time = rand() % RAND_MAX + 1;

	int service_time = c.service_time;
	printf("Customer %d enter. service time : %d mins", id, service_time);

	enqueue(queue, c);
	num_customers++;
}

int removecustomer(Queue* queue, int clock) {
	if (isempty(queue))
		return 0;
	Customer customer;
	customer = peek(queue);

	int service_time = customer.service_time;
	printf("Customer %d : %d mins service starts. waiting time : %d mins\n",
		customer.id, service_time, clock - customer.arrival_time);
	dequeue(queue);
	served_customers++;
	waited_time += clock - customer.arrival_time;

	return service_time;
}

int main() {
	Queue queue;
	initqueue(&queue);
	int service_time = 0, duration = 10;
	int clock = 0, id = 1;

	while (clock < duration) {
		clock++;
		printf("Time = %d\n", clock);

		if (arrive_customer())
			insertcustomer(&queue, id++, clock);

		if (service_time > 0)
			service_time--;
		else
			service_time = removecustomer(&queue, clock);
	}

	printf("Total waiting time = %d mins\n", waited_time);
	printf("Average waiting time per customer = %.2f mins\n", (double)waited_time / served_customers);
	printf("Number of served customer = %d\n", served_customers);
	printf("Number of waiting customers = %d\n", num_customers - served_customers);

	return 0;
}