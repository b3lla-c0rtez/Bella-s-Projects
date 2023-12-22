#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <dirent.h>
#include <errno.h>
#include <string.h>
#include <linux/limits.h>

void usage(int argc, char** argv);
void find_file(char* dir_name, char* file_to_find);

int main(int argc, char** argv)
{
	DIR* dp;
	struct dirent* dirp;

	// check if this application is being used properly
	usage(argc, argv);

	// check to see if provided directory is accessible
	errno = 0;
	dp = opendir(argv[1]);
	if(dp == NULL) {
		switch(errno) {
			case EACCES:
				fprintf(stderr, "Permission denied\n");
				break;
			case ENOENT:
				fprintf(stderr, "Directory does not exist\n");
				break;
			case ENOTDIR:
				fprintf(stderr, "'%s' is not a directory\n", argv[1]);
				break;	
		}
	}

	// print all files in the directory
	int cnt = 0;
	while((dirp = readdir(dp)) != NULL) {
		fprintf(stdout, "%d: %s", cnt, dirp->d_name);
		if(dirp->d_type == DT_DIR) {
			printf("\t directory");
		}
		printf("\n");
		cnt++;
	}

	// close the directory 
	closedir(dp);


	// now, recursivey traverse the directory structure to find the provided
	// file name
	char* file_to_find = argv[2];
	find_file(argv[1], file_to_find);

	return 0;
}


void usage(int argc, char** argv)
{
    if (argc != 3) {
        fprintf(stderr, "Usage: ./%s directory_name file_to_find\n", argv[0]);
        exit(EXIT_FAILURE);
    }
}

void find_file(char* dir_name, char* file_to_find)
{
	// recursively search directory and subdirectory
	// find file that matches file name
	
	char name_dir[PATH_MAX];
	struct dirent *dp;
	DIR *dirp = opendir(dir_name);


	while((dp = readdir(dirp)) != NULL) {
		if(dp->d_type == DT_DIR) {
			if(strcmp(dp->d_name, ".") == 0 || strcmp(dp->d_name, "..") == 0) {
				continue;
			} else {
				
				strcpy(name_dir, dir_name);
				//strcat(name_dir, "/");
				//strcat(name_dir, dp->d_name);
				name_dir[strlen(dir_name)] = '/';
				strcpy(name_dir + strlen(dir_name) + 1, dp->d_name);

				find_file(name_dir, file_to_find);
			}
		} else {
			if (strcmp(file_to_find, dp->d_name) == 0) {
				printf("found %s in %s\n", file_to_find, dir_name);
			}
		}
	}
}

