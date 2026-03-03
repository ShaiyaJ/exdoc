#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    // Getting file extension 
    char* ext = NULL;
    size_t len;
    int ext_len = getline(&ext, &len, stdin);
    int no_nl = ext_len - 1;                    // Size without newline

    if (ext_len == -1)                          // Error checking
        return 1;

    // Getting the rest of the text
    char* content = "hello";
    
    // Printing out bold character based on ext
    if      (strncmp(ext, ".txt",  no_nl) == 0) printf("**%s**", content);
    else if (strncmp(ext, ".md",   no_nl) == 0) printf("**%s**", content);
    else if (strncmp(ext, ".html", no_nl) == 0) printf("<strong>%s</strong>", content);

    // Cleanup
    free(ext);

    return 0;
}
