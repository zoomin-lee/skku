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
	Node* head;
	int len;
} LinkedList;

void initlist(LinkedList* plist) {
	plist->head = (Node*)malloc(sizeof(Node));
	plist->head->next = NULL;
	plist->len = 0;
}

bool isempty(LinkedList* plist) {
	return plist->len == 0;
}

void insertmiddle(LinkedList* plist, int pos, Data item) {
	Node* cur, * newnode;

	if (pos<0 || pos>plist->len)
		exit(1);

	newnode = (Node*)malloc(sizeof(Node));
	newnode->item = item;
	newnode->next = NULL;

	cur = plist->head;
	for (int i = 0; i < pos; i++)
		cur = cur->next;

	newnode->next = cur->next;
	cur->next = newnode;
	plist->len++;
}

void removemiddle(LinkedList* plist, int pos) {
	Node* cur, * temp;
	if (isempty(plist) || pos < 0 || pos >= plist->len)
		exit(1);

	cur = plist->head;
	for (int i = 0; i < pos; i++)
		cur = cur->next;

	temp = cur->next;
	cur->next = cur->next->next;
	plist->len--;
	free(temp);
}

Data readitem(LinkedList* plist, int pos) {
	Node* cur;
	if (isempty(plist) || pos < 0 || pos >= plist->len)
		exit(1);

	cur = plist->head->next;
	for (int i = 0; i < pos; i++)
		cur = cur->next;

	return cur->item;
}

void printlist(LinkedList* plist) {
	for (Node* cur = plist->head->next; cur != NULL; cur = cur->next)
		printf("%d\n", cur->item);
}

void clearlist(LinkedList* plist) {
	while (plist->head->next != NULL)
		removemiddle(plist, 0);
	free(plist->head);
}

LinkedList* concatenate(LinkedList* plist1, LinkedList* plist2) {
	if (plist1->head->next == NULL)
		return plist2;
	else if (plist2->head->next == NULL)
		return plist1;
	else {
		Node* cur = plist1->head->next;
		while (cur->next != NULL)
			cur = cur->next;
		cur->next = plist2->head->next;
		free(plist2->head);
		return plist1;
	}
}

void reverse(LinkedList* plist) {
	Node* prev = NULL, * cur = NULL;
	Node* next = plist->head->next;

	while (next != NULL) {
		prev = cur;
		cur = next;
		next = next->next;
		cur->next = prev;
	}
	plist->head->next = cur;
}