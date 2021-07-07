#include <stdio.h>
#define MAX 24
#define START_ID 1

typedef struct {
	char name[MAX];
	int id;
	int score;
}student;

int main(int argc, char *argv[]) {
	student rec;
	FILE *fp;
	
	if (argc != 2) {
		fprintf(stderr, "USE : %s file \n", argv[0]);
		return 1;
	}

	fp = fopen(argv[1], "w");
	printf("%s %-6s %-4s\n", "num", "name", "score");
	
	while(scanf("%d %s %d", &rec.id, rec.name, &rec.score) == 3){ 
//		__fpurge(stdin);
		fprintf(fp, "%d %s %d ", rec.id, rec.name, rec.score);
	}
	
	fclose(fp);	
	return 0;
}
