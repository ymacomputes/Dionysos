#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

int main()
{
    printf("rock \npaper \nscissors \nSHOOT! \n--> ");

    char move[20];
    scanf("%s", move);


    time_t t;
   
    /* Intializes random number generator */
    srand((unsigned) time(&t));

    int num = rand() % 3;
    printf("%d", num);

    if (num == 0)
    {
        printf("rock \n");
        if (strcmp(move, "scissors") == 0)
        {
            printf("you lose! \n");
        }
        else if (strcmp(move, "rock") == 0)
        {
            printf("draw \n");
        }
        else if (strcmp(move, "paper") == 0)
        {
            printf("you win! \n");
        }
    }
    else if (num == 1)
    {
        printf("scissors \n");
        if (strcmp(move,"scissors") == 0)
        {
            printf("draw \n");
        }
        else if (strcmp(move, "rock") == 0)
        {
            printf("you win! \n");
        }
        else if (strcmp(move, "paper") == 0)
        {
            printf("you lose! \n");
        }
    }
    else
    {
        printf("paper \n");
        if (strcmp(move, "scissors") == 0)
        {
            printf("you win! \n");
        }
        else if (strcmp(move, "rock") == 0)
        {
            printf("you lose! \n");
        }
        else if (strcmp(move, "paper \n") == 0)
        {
            printf("draw");
        }
    }
    return (0);
}