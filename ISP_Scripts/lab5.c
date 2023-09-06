#include <stdio.h>

#define limit 15

int main() {
    int array[limit];
    int min, max; 

    printf("Enter up to %d numbers (enter -1 to stop).\n", limit);
    printf("Only enter numbers.\n");
    int n = 0;
    do {
        scanf("%d", &array[n]);
        n++;
    } while (array[n-1] != -1 && n < limit);

    if (array[n-1] != -1) {
        min = max = array[0];
        printf("Numbers entered: %d\n", n);
        
        for (int i = 1; i < n; i++) {
            if (array[i] < min) {
                min = array[i];
            }
            if (array[i] > max) {
                max = array[i];
            }
        }
        printf("Minimum number is: %d\n", min);
        printf("Maximum number is: %d\n", max);
    }
    else {
        if ((n-1)==0){
            printf("Numbers entered: %d\n", n-1);
            printf("Minimum number is: None\n");
            printf("Maximum number is: None\n");
        }
        else {

            min = max = array[0];
            printf("Numbers entered: %d\n", n-1);
        
            for (int i = 1; i < n-1; i++) {
                if (array[i] < min) {
                    min = array[i];
                }
                if (array[i] > max) {
                    max = array[i];
                }
            }
            
            printf("Minimum number is: %d\n", min);
            printf("Maximum number is: %d\n", max);
        }

    }
    
    return 0;
}