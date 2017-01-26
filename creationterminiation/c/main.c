#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define NUM_THREADS 5


void *WhoAmI(void *t_id)
{
   long my_id;
   my_id = (long)t_id;
   printf("I am thread #%ld!\n", my_id);

   pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
   pthread_t threads[NUM_THREADS];
   int rc;
   long t;   
   
   for (t = 0; t < NUM_THREADS; t++) {
      printf("In main: creating thread %ld\n", t);
      rc = pthread_create(&threads[t], NULL, WhoAmI, (void *)t);
      if (rc) {
         printf("ERROR: return code from pthread_create() is %d\n", rc);
         exit(-1);
      }
   }

   // That is all folks
   pthread_exit(NULL);
}
