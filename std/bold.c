#include <stdio.h>

int main(void) {
    char** format = NULL;
    char content[256];

    getline(format, NULL, stdin);

    for (int i = 0; i < 256; i++) {
        int temp = fgetc(stdin);

        if (temp == EOF)
            break;

        content[i] = (char) temp; 
    }

    printf("**%s**", content);

    return 0;
}
