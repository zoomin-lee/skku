#include<stdio.h>

typedef enum {
	false, true
} bool;

typedef int Data;

typedef struct _Node {
	Data item;
	struct _Node* prev;
	struct _Node* next;
} Node;

typedef struct {
	Node* head;
	int len;
} Doublelinkedlist;

void initlist(Doublelinkedlist* plist) {
	Node* dummy1, * dummy2;
	dummy1 = (Node*)malloc(sizeof(Node));
	dummy2 = (Node*)malloc(sizeof(Node));

	dummy1->prev = NULL;
	dummy1->next = dummy2;
	dummy2->prev = dummy1;
	dummy2->next = NULL;

	plist->head = dummy1;
	plist->len = 0;
}

void insertmiddle(Doublelinkedlist* plist, int pos, Data item) {
	Node* cur, * newnode;
	newnode = (Node*)malloc(sizeof(Node));
	newnode->item = item;
	
	cur = plist->head;
	for (int i = 0; i < pos; i++)
		cur = cur->next;

	newnode->prev = cur;
	newnode->next = cur->next;
	cur->next->prev = newnode;
	cur->next = newnode;
	plist->len++;
}

void removemiddle(Doublelinkedlist* plist, int pos, Data item) {
	Node* cur, * temp;
	
	cur = plist->head;
	for (int i = 0; i < pos; i++)
		cur = cur->next;
	temp = cur->next;
	temp->next->prev = cur;
	cur->next = temp->next;

	plist->len--;
	free(temp);
}