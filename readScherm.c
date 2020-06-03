#include <stdio.h>
#include <stdlib.h>

int main()
{
   int res = read_init_display();
   printf("NumDisplay=%d", res + 1);
   return 0;
}

int read_init_display() 
{
   int numDisplay;
   FILE *fptr;

   if ((fptr = fopen(".\\schermata.txt","r")) == NULL){
       printf("Error! opening file");

       // Program exits if the file pointer returns NULL.
       exit(1);
   }

   fscanf(fptr,"%d", &numDisplay);

   //printf("NumDisplay=%d", numDisplay);
   fclose(fptr); 
  
   return numDisplay;
}