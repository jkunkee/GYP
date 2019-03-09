
#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    FILE* pFile;
    printf("Writing to '%s'...\n", argv[1]);
    pFile = fopen(argv[1], "w");
    if (pFile == 0)
    {
        printf("File open failed, errno=%d.\n", errno);
        return 16;
    }
    fprintf(pFile,
        "#include <stdio.h>\n"
        "int main(void)"
        "{"
        "    printf(\"Hello World!\\n\");"
        "    return 0;"
        "}"
        );
    fclose(pFile);
    return 0;
}