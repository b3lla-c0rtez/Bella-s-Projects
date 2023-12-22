#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <sys/stat.h>

int p1getline(int fd, char buf[], int size) {
    int i;
    char c;
    int max = size - 1; /* must leave room for EOS */

    i = 0;
    for (i = 0; i < max; i++) {
        if (read(fd, &c, 1) == 0)
            break;
        buf[i] = c;
        if (c == '\n') {
            i++;
            break;
        }
    }
    buf[i] = '\0';
    return i;
}


int p1strchr(char buf[], char c) {
    int i;

    for (i = 0; buf[i] != '\0'; i++)
        if (buf[i] == c)
            return i;
    return -1;
}


static char *singlequote = "'";
static char *doublequote = "\"";
static char *whitespace = " \t";

int p1getword(char buf[], int i, char word[]) {
    char *tc, *p;

    /* skip leading white space */
    while(p1strchr(whitespace, buf[i]) != -1)
        i++;
    /* buf[i] is now '\0' or a non-blank character */
    if (buf[i] == '\0')
        return -1;
    p = word;
    switch(buf[i]) {
    case '\'': tc = singlequote; i++; break;
    case '"': tc = doublequote; i++; break;
    default: tc = whitespace; break;
    }
    while (buf[i] != '\0') {
        if (p1strchr(tc, buf[i]) != -1)
            break;
        *p++ = buf[i];
        i++;
    }
    /* either at end of string or have found one of the terminators */
    if (buf[i] != '\0') {
        if (tc != whitespace) {
            i++;	/* skip over terminator */
        }
    }
    *p = '\0';
    return i;
}

void parse_through_file_for_words_by_line(int fd, char *buffer, int size) {
	int my_size = 1024;
	while (p1getline(fd, buffer, my_size) != -1) {
		int i = 0;
		if (buffer[0] == '\0') {
			break;
		}

		fprintf(stdout, "%s\n", buffer);
		char args[16][64];
		int j =0;
		while((j = p1getword(buffer, j, args[i])) != -1) {
			if (args[i][0] == '\0') {
				break;
			}
			fprintf(stdout, "\t%s\n", args[i]);
			i++;
		}
	}
}

int main(int argc, char** argv) {
	char *file_name = "/home/me/Documents/CS415/proj1/P1start/testing.txt";
	int fd = open(file_name, O_RDONLY);
	
	char c;
	char buffer[BUFSIZ];

	fprintf(stdout, "got here\n");
	//parse_through_file_for_words_by_line(fd, buffer, 1000);
	p1getline(STDIN_FILENO, buffer, 1024);
	printf("%s\n", buffer);
	close(fd);

	return EXIT_SUCCESS;
}
