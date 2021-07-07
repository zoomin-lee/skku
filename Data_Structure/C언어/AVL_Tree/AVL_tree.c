#include<stdio.h>
#include<stdlib.h>

typedef struct _avltree {
	int key;
	struct _avltree* left_child;
	struct _avltree* right_child;
}AVL;

int height(AVL* node) {
	if (node == NULL)
		return 0;
	int r = 0, l = 0;
	r = height(node->right_child);
	l = height(node->left_child);
	return 1 + max(r, l);
}

AVL* createnode(int key) {
	AVL* node = (AVL*)malloc(sizeof(AVL));
	node->key = key;
	node->left_child = NULL;
	node->right_child = NULL;
	return node;
}

void deletetree(AVL* node) {
	if (node != NULL) {
		if(node->right_child)
			deletetree(node->right_child);
		if(node->left_child)
			deletetree(node->left_child);
		free(node);
	}
}

void destroynode(AVL* node) {
	free(node);
}

void createleftsubtree(AVL* root, AVL* left) {
	if (root->left_child != NULL)
		exit(1);
	root->left_child = left;
}

void createrightsubtree(AVL* root, AVL* right) {
	if (root->right_child != NULL)
		exit(1);
	root->right_child = right;
}

int balance_factor(AVL* node) {
	AVL* left = node->left_child;
	AVL* right = node->right_child;
	if (node != NULL)
		return height(left) - height(right);
	else
		return 0;
}

void LLrotation(AVL* node) {
	AVL* A = node;
	AVL* B = node->right_child;
	AVL* T = B->left_child;

	node = B;
	B->left_child = A;
	A->right_child = T;
}

void RRrotation(AVL* node) {
	AVL* A = node;
	AVL* B = node->left_child;
	AVL* T = node->right_child;

	node = B;
	B->right_child = A;
	A->left_child = T;
}

void balance(AVL* node) {
	int bf1 = balance_factor(node);
	while (bf1 > 1 || bf1 < -1) {
		if (bf1 > 1) {
			if (balance_factor(node->left_child) < 0)
				LLrotation(node->left_child);
			RRrotation(node);
		}
		else if (bf1 < -1) {
			if (balance_factor(node->right_child) > 0)
				RRrotation(node->right_child);
			LLrotation(node);
		}
		bf1 = balance_factor(node);
	}
}

int main() {
	AVL* node1 = createnode(10);
	AVL* node2 = createnode(13);
	AVL* node3 = createnode(7);
	AVL* node4 = createnode(5);
	AVL* node5 = createnode(4);

	createrightsubtree(node1, node2);
	createleftsubtree(node1, node3);
	createleftsubtree(node3, node4);
	createleftsubtree(node4, node5);

	balance(node1);
	int b = balance_factor(node1);
	printf("%d \n", b);

	deletetree(node1);
	return 0;
}