#include <stdio.h>
#include <string.h> 

//HEREDOC \N BAK

int main(int argc, char *argv[]) {
    int i, j, max_length = 0;

    // Check if any strings are provided
    if (argc == 1) {
        return 0;
    }

    // Find the longest string
    for (i = 1; i < argc; i++) {
        int len = strlen(argv[i]);
        if (len > max_length) {
            max_length = len;
        }
    }

    // Print the top border of the frame
    for (i = 0; i < max_length + 4; i++) {
        printf("*");
    }
    printf("\n");

    // Print each string within the frame
    for (i = 1; i < argc; i++) {
        printf("* %s", argv[i]);
        for (j = strlen(argv[i]); j < max_length; j++) {
            printf(" ");
        }
        printf(" *\n");
    }

    // Print the bottom border of the frame
    for (i = 0; i < max_length + 4; i++) {
        printf("*");
    }
    printf("\n");

    return 0;
}