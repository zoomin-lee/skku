#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

typedef int Key;

typedef enum {
	false, true
} bool;

typedef struct _BSTnode {
	Key KEY;
	struct _BSTnode* left_child;
	struct _BSTnode* right_child;
}BSTnode;

BSTnode* createnode(Key key) {
	BSTnode* node = (BSTnode*)malloc(sizeof(BSTnode));
	node->KEY = key;
	node->left_child = NULL;
	node->right_child = NULL;
	return node;
}

void deletetree(BSTnode* node) {
	if (node != NULL) {
		deletetree(node->left_child);
		deletetree(node->right_child);
		free(node);
	}
}

void destroynode(BSTnode* node) {
	free(node);
}

void createleftsubtree(BSTnode* root, BSTnode* left) {
	if (root->left_child != NULL)
		exit(1);
	root->left_child = left;
}

void createrightsubtree(BSTnode* root, BSTnode* right) {
	if (root->right_child != NULL)
		exit(1);
	root->right_child = right;
}

bool verify(BSTnode* root, int min, int max) {
	if (root != NULL) {
		if (root->KEY < min || root->KEY>max)
			return false;
		else
			return verify(root->left_child, min, root->KEY) && verify(root->right_child, root->KEY, max);
	}
	else
		return true;
}

BSTnode* rsearch(BSTnode* root, Key key) {
	if (root == NULL || root->KEY == key)
		return root;
	else if (root->KEY > key)
		return rsearch(root->left_child, key);
	else
		return rsearch(root->right_child, key);
}

BSTnode* search(BSTnode* root, Key key) {
	BSTnode* cur = root;
	while (cur != NULL) {
		if (key > cur->KEY)
			cur = cur->left_child;
		else if (key < cur->KEY)
			cur = cur->right_child;
		else
			break;
	}
	return cur;
}

void rinsert(BSTnode* root, Key key) {
	if (root == NULL) {
		BSTnode* new = createnode(key);
	}
	else if (root->KEY == key) {
		printf("same node already exist\n");
	}
	else if (root->KEY < key) {
		if (root->right_child == NULL) {
			BSTnode* new = createnode(key);
			createrightsubtree(root, new);
		}
		else
			rinsert(root->right_child, key);
	}
	else if (root->KEY > key) {
		if (root->left_child == NULL) {
			BSTnode* new = createnode(key);
			createleftsubtree(root, new);
		}
		else
			rinsert(root->left_child, key);
	}
}

void insert(BSTnode* root, Key key) {
	BSTnode* cur = root;
	while (cur != NULL) {
		if (cur->KEY == key) {
			printf("same none exisit already\n");
		}
		else if (cur->KEY > key) {
			if (cur->left_child == NULL) {
				BSTnode* new = createnode(key);
				createleftsubtree(cur, new);
				break;
			}
			else
				cur = cur->left_child;
		}
		else if (cur->KEY < key) {
			if (cur->right_child == NULL) {
				BSTnode* new = createnode(key);
				createrightsubtree(root, new);
				break;
			}
			else
				cur = cur->right_child;
		}
	}
}

void remove(BSTnode* root, Key key) {
	BSTnode* cur = root, * parent = NULL;
	while (cur != NULL && cur->KEY != key) {
		parent = cur;
		if (cur->KEY > key)
			cur = cur->left_child;
		else
			cur = cur->right_child;
	}

	if (cur == NULL)
		printf("it is empty\n");

	if (cur->left_child == NULL && cur->right_child == NULL) {
		if (parent != NULL) {
			if (parent->left_child == cur)
				parent->left_child = NULL;
			else
				parent->right_child = NULL;
		}
		else
			cur = NULL;
	}

	else if (cur->left_child == NULL || cur->right_child == NULL) {
		BSTnode* child;
		if (cur->left_child != NULL)
			child = cur->left_child;
		else
			child = cur->right_child;

		if (parent != NULL) {
			if (parent->left_child == cur)
				parent->left_child = child;
			else
				parent->right_child = child;
		}
	}

	else {
		BSTnode* succ_parent = cur, * succ = cur->right_child;
		while (succ->left_child != NULL) {
			succ_parent = succ;
			succ = succ->left_child;
		}
		if (succ_parent->right_child == succ)
			succ_parent->right_child = succ->right_child;
		else
			succ_parent->left_child = succ->right_child;

		cur->KEY = succ->KEY;
		cur = succ;
	}
	destroynode(cur);
}

void rinorder(BSTnode* root) {
	if (root != NULL) {
		rinorder(root->left_child);
		printf("%d ", root->KEY);
		rinorder(root->right_child);
	}
}

int main() {
	BSTnode* node1 = createnode(20);
	BSTnode* node2 = createnode(10);
	BSTnode* node3 = createnode(30);
	BSTnode* node4 = createnode(5);
	BSTnode* node5 = createnode(15);
	BSTnode* node6 = createnode(25);
	
	createleftsubtree(node1, node2);
	createrightsubtree(node1, node3);
	
	createleftsubtree(node2, node4);
	createrightsubtree(node2, node5);
		
	createleftsubtree(node3, node6);
	

	//bool verf = verify(node1, INT_MIN, INT_MAX);
	//printf("%s\n", verf ? "true" : "false");   

	//int a = search(node1, 20);
	//printf("%d\n", a);

	remove(node1, 20);

	rinorder(node1);

	deletetree(node1);

	return 0;
}