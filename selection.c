#include <stdio.h>

int select_sort(int arr[], int lenght);
int main(void)
{
    int arr[19] = {8,3,1,4,6,10,12,34,6,8,0,3,5,7,9,2,35,78,2};
    int lenght = 19;
    select_sort(arr,lenght);
}

int select_sort(int arr[], int lenght)
{
    /** basically it will take a array with it's size and than it will try to find the smallest number. If it finds it, it will swap it with the i-th member(as the loop goes on).
     * it will continue doing the loop until the whole array is sorted out**/
    for(int i = 0; i < lenght; i++)
    {
        int min = arr[i] ;
        int carry = arr[i];
        int index = i;
        for (int j = i + 1; j < lenght; j++)
        {
            if (min > arr[j])
            {
                min = arr[j];
                index = j;
            }
        }
       arr[i] = min;
       arr[index] = carry;
    }
    for(int i = 0; i < lenght; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
