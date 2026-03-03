#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    // Getting file extension 
    char* ext;
    size_t ext_len;

    if (getline(&ext, &ext_len, stdin) == -1)   // Error code
        return 1;

    // Getting the rest of the text
    char* content;
    
    // Printing out bold character based on ext
    if      (strncmp(ext, ".txt",  len)) printf("**%s**", content);
    else if (strncmp(ext, ".md",   len)) printf("**%s**", content);
    else if (strncmp(ext, ".html", len)) printf("<strong>%s</strong>", content);

    // Cleanup
    free(ext);

    return 0;
}
