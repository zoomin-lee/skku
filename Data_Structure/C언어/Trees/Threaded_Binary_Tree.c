#include <stdio.h>

typedef enum {
	false, true
} bool;

typedef int BData;

typedef struct _btreenode {
	BData item;
	struct _btreenode* left_child;
	struct _btreenode* right_child;
	bool istheaded;
} Btreenode;

Btreenode* leftmost(Btreenode* node) {
	if (node == NULL)
		return NULL;

	while (node->left_child != NULL)
		node = node->left_child;
	
	return node;
}

void inorder(Btreenode* node) {
	Btreenode* cur = leftmost(node);
	while (cur != NULL) {
		printf("%d ", cur->item);
		if (cur->istheaded)
			cur = cur->right_child;
		else
			cur = leftmost(cur->right_child);
	}
}

Btreenode* createnode(BData item) {
	Btreenode* node = (Btreenode*)malloc(sizeof(Btreenode));
	node->item = item;
	node->left_child = NULL;
	node->right_child = NULL;
	node->istheaded = false;
	return node;
}

void destorynode(Btreenode* node) {
	free(node);
}

void createleftsubtree(Btreenode* root, Btreenode* left) {
	if (root->left_child != NULL)
		exit(1);
	root->left_child = left;
}

void createrightsubtree(Btreenode* root, Btreenode* right) {
	if (root->right_child != NULL)
		exit(1);
	root->right_child = right;
}

Btreenode* find_successor(Btreenode* root) {
	Btreenode* succ;
	succ = root->left_child;
	while (1) {
		if (succ->right_child == NULL)
			break;
		succ = succ->right_child;
	}
	return succ;
}

int main() {
	Btreenode* node1 = createnode(10);
	Btreenode* node2 = createnode(20);
	Btreenode* node3 = createnode(30);
	Btreenode* node4 = createnode(40);
	Btreenode* node5 = createnode(50);
	Btreenode* node6 = createnode(60);

	createleftsubtree(node1, node2);
	createrightsubtree(node1, node3);

	createleftsubtree(node2, node4);
	createrightsubtree(node2, node5);

	createleftsubtree(node3, node6);

	node4->istheaded = true;
	node5->istheaded = true;
	node6->istheaded = true;

	Btreenode * succ = find_successor(node2);
	createrightsubtree(succ, node2);
	Btreenode* succ = find_successor(node1);
	createrightsubtree(succ, node1);	
	Btreenode* succ = find_successor(node3);
	createrightsubtree(succ, node3);
	inorder(node1);

	return 0;
}