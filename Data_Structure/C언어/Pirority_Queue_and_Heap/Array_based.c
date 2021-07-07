#include <stdio.h>
#define MAX_HEAP	100

typedef enum {
	false, true
} bool;

typedef char Data;

typedef struct {
	Data data;
	int priority;
} HNode;

typedef struct {
	HNode items[MAX_HEAP - 1];
	int num;
} Heap;

void initheap(Heap* pheap) {
	pheap->num = 0;
}

bool isempty(Heap* pheap) {
	return pheap->num == 0;
}

bool isfull(Heap* pheap) {
	return pheap->num == MAX_HEAP;
}

int getparent(int idx) {
	return idx / 2;
}

int getlchild(int idx) {
	return 2 * idx;
}

int getrchild(int idx) {
	return 2 * idx + 1;
}

int gethighprioritychild(Heap* pheap, int idx) {
	if (getlchild(idx) > pheap->num)
		return 0;
	else if (getlchild(idx) == pheap->num)
		return getlchild(idx);
	else {
		int left = getlchild(idx), right = getrchild(idx);
		if (pheap->items[left].priority > pheap->items[right].priority)
			return left;
		else
			return right;
	}
}

void insert(Heap* pheap, Data data, int priority) {
	HNode newnode;
	int idx = pheap->num + 1;

	if (isfull(&pheap))
		exit(1);
	
	while (idx > 1) {
		if (pheap->items[getparent(idx)].priority < priority) {
			pheap->items[idx] = pheap->items[getparent(idx)];
			idx = getparent(idx);
		}
		else break;
	}
	newnode.data = data;
	newnode.priority = priority;

	pheap->items[idx] = newnode;
	pheap->num++;
}

Data delete(Heap* pheap) {
	Data max = pheap->items[1].data;
	HNode last = pheap->items[pheap->num];

	int parent = 1, child;
	while (child = gethighprioritychild(pheap, parent)) {
		if (last.priority < pheap->items[child].priority) {
			pheap->items[parent] = pheap->items[child];
			parent = child;
		}
		else break;
	}
	pheap->items[parent] = last;
	pheap->num--;

	return max;
}

void heapsort(Data a[], int n) {
	Heap heap;
	initheap(&heap);

	for (int i = 0; i < n; i++) 
		insert(&heap, a[i], a[i] - '0');
	for (int i = n - 1; i >= 0; i--) 
		a[i] = delete(&heap);
}

int main() {
	Heap heap;
	initheap(&heap);
	insert(&heap, 't', 28);
	insert(&heap, 'u', 7);
	insert(&heap, 'w', 6);
	insert(&heap, 'y', 5);
	insert(&heap, 'v', 4);

	
	//char a[5] = { '2','1','4','3','5' };
	//heapsort(a, 5);
	//printf("%s", a);
}