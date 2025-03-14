#include <stdio.h>
int main()
{
    int idade;
    printf("Digite a idade: ");
    scanf("%d", &idade);

    printf("Idade: %d\n", idade);
    if (idade >= 18)
    {
        printf("Maior de idade\n");
    }
    else
    {
        printf("Menor de idade\n");
    }
}