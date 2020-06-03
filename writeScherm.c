#include <stdio.h>
#include <stdlib.h>

void main()
{
   write_init_display(8);
}

void write_init_display(int numDisplay) 
{
   FILE *fptr;

   fptr = fopen(".\\schermata.txt","w");

   if(fptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }

   fprintf(fptr,"%d", numDisplay);
   fclose(fptr);
}