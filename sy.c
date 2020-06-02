#include <unistd.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>

char main()
{
   char cwd[PATH_MAX];
   getcwd(cwd, sizeof(cwd));
   char *result = malloc(strlen(cwd) + strlen("\\config\\remaps\\custom\\90deg\\90deg.rmp") + 1); // +1 for the null-terminator
   // in real code you would check for errors in malloc here
   strcpy(result, cwd);
   strcat(result, "\\config\\remaps\\custom\\90deg\\90deg.rmp");
   printf("Current working dir: %s\n", result);
   return *result;
}
