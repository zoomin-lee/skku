#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

#define ARRAY_SIZE	5

// 1-2
void inputNumbers(int num[], int len);
double computeAverage(int num[], int len);

// 1-6
void swap1(int x, int y);
void swap2(int* px, int* py);

// 1-9
void printArray(int* pa, int len);
void multiply4(int* pa, int len);

// 1-11
int* genNumbers(int size);

// 1-12
typedef struct {
	char name[10];
	int scores[3];
	int total;
} STUDENT;

// 1-15
typedef struct {
	int numerator;
	int denominator;
} FRACTION;

// 1-16
double f(double);
double sum_square(double(*)(double), int, int);
// double sum_square(double f(double x), int m, int n);
// double sum_square(double f(double), int m, int n);
// double sum_square(double f(double), int, int);
// double sum_square(double (*f)(double), int, int);
// 전부 가능


int main() {
	// 1-1
	int numbers[ARRAY_SIZE], i;
	printf("Input five numbers\n");

	for (i = 0; i < ARRAY_SIZE; i++)
		scanf("%d", &numbers[i]);
	
	for (i = ARRAY_SIZE - 1; i >= 0; i--)
		printf("%d", numbers[i]);
	

	// 1-2
	inputNumbers(numbers, ARRAY_SIZE);
	printf("average : %.31f", computeAverage(numbers, ARRAY_SIZE));


	// 1-3
	int row, col, matrix[6][6];
	for (row = 0; row < 6; row++) {
		for (col = 0; col < 6; col++) {
			if (row < col)
				matrix[row][col] = 1;
			else if (row == col)
				matrix[row][col] = 0;
			else
				matrix[row][col] = -1;
		}
	}

	// 1-4
	char c = 'A';
	char* pc = &c;
	char** ppc = &pc;

	int n = 3;
	int* pn = &n;
	int** ppn = &pn;

	printf("%c %p\n", c, pc);
	printf("%c %c\n", c, *pc);
	printf("%p %p\n", &c, &pc);
	printf("%d %d\n\n", sizeof(c), sizeof(pc));

	printf("%p %p\n", pc, ppc);
	printf("%d %d\n\n", sizeof(pc), sizeof(ppc));

	printf("%p %p\n", pc + 1, ppc + 1);
	//pc+1은 c의 주소가 1bit이므로 주소가 1늘어나지만, ppc+1은 주소가 4늘어남 이는 pc가 4bits 주소를 가지기 때문임
	printf("%p %p\n", &c, &c + 1);
	printf("%p %p\n", &pc, &ppc);
	printf("%p %p\n\n", &pc + 1, &ppc + 1);

	*pc = 'B';
	printf("%c %p\n", c, pc);
	printf("%c %c\n", c, *pc);
	printf("%p %p\n", &c, &pc);
	printf("%d %d\n\n", sizeof(c), sizeof(pc));

	c = 'C';
	printf("%c %p\n", c, pc);
	printf("%c %c\n", c, *pc);
	printf("%p %p\n", &c, &pc);
	printf("%d %d\n\n", sizeof(c), sizeof(pc));

	printf("%d %p\n", n, pn);
	printf("%p %p\n", &n, &pn);
	printf("%d %d\n\n", sizeof(n), sizeof(pn));

	printf("%p %p\n", pn, ppn);
	printf("%p %p\n", pn + 1, ppn + 1);
	//둘다 4씩 늘어남
	printf("%p %p\n", &n, &n + 1);
	printf("%p %p\n", &pn, &ppn);
	printf("%p %p\n", &pn + 1, &ppn + 1);

	// 1-5 
	int a, b, d;
	int* p, * q, * r;
	a = 6, b = 10;
	p = &b, q = p, r = &d;
	p = &a, * q = 8, * r = *p;
	*r = a + *q + *&d;

	printf("%d %d %d", a, b, d);

	
	// 1-6
	int x = 5, y = 7;
	swap1(x, y);
	printf("%d %d\n", x, y);
	// swap 되지 않음 call by value

	swap2(&x, &y);
	printf("%d %d\n", x, y);
	// swap 됨 call by reference


	// 1-7
	int z[6] = { 5,3,2,1,4,6 };
	int* pz = z;
	 
	printf("%d %d\n", *z, *pz);
	printf("%p %p\n", z, pz);
	printf("%p %p\n", &z, &pz);
	printf("%d %d\n", z[0], pz[0]);
	printf("%d %d\n", z[1], pz[1]);


	// 1-8
	int a[6] = { 32,12,31,42,15,24 };
	int* pend = a + 6;
	int* psmallest = a;
	int* pi = NULL;

	for (pi = a; pi < pend; pi++)
		printf("%d ", *pi);
	printf("\n");

	for (pi = a + 1; pi < pend; pi++)
		if (*pi < *psmallest)
			psmallest = pi;

	printf("%d", *psmallest);


	// 1-9
	int w[5] = { 5,3,2,1,4 };
	printArray(w, 5);
	multiply4(w, 5);
	printArray(w, 5);

	// 1-10
	int size, i;
	scanf("%d", &size);

	int* pn = malloc(sizeof(int) * size);
  //operating system인 malloc을 이용해서 heap의 크기 정의
	for (i = 0; i < size; i++)
		scanf("%d", &pn[i]);

	for (i = 0; i < size; i++)
		printf("%d\n", pn[i]);

	free(pn);


	// 1-11
	int size, i;
	scanf("%d", &size);

	int* pn = genNumbers(size);
	for (i = 0; i < size; i++)
		printf("%d\n", pn[i]);

	free(pn);

	// 1-12
	STUDENT s1 = { "Alice", 80,70,90 };
	STUDENT* s2 = &s1; //pointer to student1

	printf("%s\n", s1.name);
	for (int i = 0; i < 3; i++)
		printf("%d\n", s1.scores[i]);

	printf("%s\n", s2->name); // arrow를 쓰기 위해선 pointer를 써야함
	for (int i = 0; i < 3; i++)
		printf("%d\n", s2->scores[i]);


	// 1-13
	STUDENT stu[1];
	for (int i = 0; i < 1; i++) {
		stu[i].total = 0;
		scanf("%s", stu[i].name);//pointer
		for (int j = 0; j < 3; j++) {
			scanf("%d", &stu[i].scores[j]); //provide pointer
			stu[i].total += stu[i].scores[j];
		}
	}
	
	for (int i = 0; i < 1; i++) {
		printf("%s\n", stu[i].name);//pointer
		for (int j = 0; j < 3; j++)
			printf("%d\n", stu[i].scores[j]); // provide value
		printf("%d\n", stu[i].total);
	}


	// 1-14
	int n;
	scanf("%d", &n);

	STUDENT* s = malloc(sizeof(STUDENT) * n);
	for (int i = 0; i < n; i++) {
		scanf("%s", s[i].name);
		s[i].total = 0;
		for (int j = 0; j < 3; j++) {
			scanf("%d", &s[i].scores[j]);
			s[i].total += s[i].scores[j];
		}
		printf("%d\n", s[i].total);
	}

	free(s);

	// 1-15
	FRACTION f1 = { 4,5 };
	FRACTION f2 = { 3,7 };
	FRACTION f3;

	f3.numerator = f1.numerator * f2.numerator;
	f3.denominator = f1.denominator * f2.denominator;

	printf("%d / %d", f3.numerator, f3.denominator);

	// 1-16
	printf("%s%.7f\n%s%,7\n", "first computation : ", sum_square(f, 1, 10000), "second computation : ", sum_square(sin, 2, 13));
	return 0;
}

// 1-2
void inputNumbers(int num[], int len) {
	int i;
	for (i = 0; i < len; i++)
		scanf("%d", &num[i]);
}

double computeAverage(int num[], int len) {
	int total = 0, i;
	for (i = 0; i < len; i++)
		total = total + num[i];

	return total / (double)len;
}


// 1-6
void swap1(int x, int y) {
	int temp = x;
	x = y;
	y = temp;
}

void swap2(int* px, int* py) {
	int temp = *px;
	*px = *py;
	*py = temp;
}


// 1-9
void printArray(int* pa, int len) {
	int i;
	for (i = 0; i < len; i++)
		printf("%d ", pa[i]);
	printf("\n");
}

void multiply4(int* pa, int len) {
	int i;
	for (i = 0; i < len; i++)
		pa[i] = pa[i] * 4;
}


// 1-11
int* genNumbers(int size) {
	int i;
	int* pn = malloc(4 * size);
	for (i = 0; i < size; i++)
		scanf("%d", &pn[i]);

	return pn;
}


// 1-16
double sum_square(double f(double), int m, int n) {
	int k;
	double sum = 0.0;

	for (k = m; k <= n; ++k)
		sum += f(k) * f(k);
	return sum;
}

double f(double x) {
	return 1.0 / x;
}