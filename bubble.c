#include <stdio.h>

int bubble_sort(int arr[], int lenght);
int main(void)
{
    int arr[12] = {0,0,0,1,3,4,5,124,5,6,2,51,};
    int lenght = 12;
    bubble_sort(arr,lenght);
}

int bubble_sort(int arr[], int lenght)
{
    /** basically it will take a array with it's size and than it will try to find the smallest number. If it finds it, it will swap it with the i-th member(as the loop goes on).
     * it will continue doing the loop until the whole array is sorted out**/

     for (int i = lenght-1; i > 0; i--)
     {
         //int swap_value = -1 ;
         int carry = 0;
         for (int j = 0; j < i; j++)
         {
             if (arr[j] > arr[j+1])
             {
                 carry = arr[j];
                 arr[j] = arr[j + 1];
                 arr[j + 1] = carry;

             }

         }
     }
     for(int i = 0; i < lenght; i++)
    {
        printf("%i ", arr[i]);
    }
    printf("\n");
    return 0;
}