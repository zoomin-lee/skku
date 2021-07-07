#include <stdio.h>

typedef enum {
	false, true
} bool;

typedef int Data;

typedef struct _Node {
	Data item;
	struct _Node* next;
} Node;

typedef struct {
	Node* tail;
	int len;
} Circularlist;

void insertinititem(Circularlist* plist, Data item) {
	Node* newnode = (Node*)malloc(sizeof(Node));
	newnode->item = item;
	newnode->next = newnode;

	plist->tail = newnode;
	plist->len++;
}

void insertfirst(Circularlist* plist, Data item) {
	if (plist->len == 0)
		insertinititem(plist, item);
	else {
		Node* newnode = (Node*)malloc(sizeof(Node));
		newnode->item = item;
		newnode->next = plist->tail->next;

		plist->tail->next = newnode;
		plist->len++;
	}
}

void insertlast(Circularlist* plist, Data item) {
	if (plist->len == 0)
		insertinititem(plist, item);
	else {
		Node* newnode = (Node*)malloc(sizeof(Node));
		newnode->item = item;
		newnode->next = plist->tail->next;

		plist->tail->next = newnode;
		plist->tail = newnode;
		plist->len++;
	}
}

void insertmiddle(Circularlist* plist, int pos, Data item) {
	if (plist->len == 0)
		insertinititem(plist, item);
	else {
		Node* newnode = (Node*)malloc(sizeof(Node));
		newnode->item = item;

		Node* cur = plist->tail;
		for (int i = 0; i < pos; i++)
			cur = cur->next;

		newnode->next = cur->next;
		cur->next = newnode;
		plist->len++;
	}
}

void removeinititem(Circularlist* plist) {
	if (isempty(plist))
		exit(1);

	if (plist->len == 1) {
		free(plist->tail);
		plist->len--;
		plist->tail = NULL;
	}
}

void removefirst(Circularlist* plist) {
	if (plist->len == 1)
		removeinititem(plist);
	else {
		Node* temp = plist->tail->next;
		plist->tail->next = temp->next;
		free(temp);
		plist->len--;
	}
}

void removelast(Circularlist* plist) {
	if (plist->len == 1)
		removeinititem(plist);
	else {
		Node* cur, * temp;
		cur = plist->tail;
		for (int i = 0; i < plist->len - 1; i++)
			cur = cur->next;
		temp = cur->next;
		cur->next = temp->next;
		free(temp);
		plist->tail = cur;
		plist->len--;
	}
}

void removemiddel(Circularlist* plist, int pos) {
	if (plist->len == 1)
		removeinititem(plist);
	else {
		Node* cur, * temp;
		cur = plist->tail;
		for (int i = 0; i < pos; i++)
			cur = cur->next;
		temp = cur->next;
		cur->next = temp->next;
		free(temp);
		plist->len--;
	}
}