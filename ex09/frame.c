#include <stdio.h>
#include <string.h> 

int main(int argc, char *argv[]) {
    int i, j, max_length = 0;

    if (argc == 1) {
        return 0;
    }

    for (i = 1; i < argc; i++) {
        int len = strlen(argv[i]);
        if (len > max_length) {
            max_length = len;
        }
    }

    for (i = 0; i < max_length + 4; i++) {
        printf("*");
    }
    printf("\n");

    for (i = 1; i < argc; i++) {
        printf("* %s", argv[i]);
        for (j = strlen(argv[i]); j < max_length; j++) {
            printf(" ");
        }
        printf(" *\n");
    }

    for (i = 0; i < max_length + 4; i++) {
        printf("*");
    }
    printf("\n");

    return 0;
}