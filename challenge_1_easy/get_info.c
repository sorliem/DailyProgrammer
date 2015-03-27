/* Author: Miles Sorlie */

#include <stdio.h>

int main(int argc, char ** argv) {

	char name[64];
	char redditUname[64];
	int age;

	printf("Enter your name > ");
	fgets(&name, 256, stdin);
	if ((strlen(name)>0) && (name[strlen (name) - 1] == '\n'))
        name[strlen (name) - 1] = '\0';
	printf("Enter your age > ");
	scanf("%d", &age);
	printf("Enter your reddit username > ");
	scanf("%s", &redditUname);
	printf("Your name is %s, your age is %d, and your username is %s.\n", name, age, redditUname);
	return 0;
}