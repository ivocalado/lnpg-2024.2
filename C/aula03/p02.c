// Ler a, b e c
// Calcular delta
// Se delta < 0, não tem raízes reais
// Se delta = 0, tem uma raiz real
// Se delta > 0, tem duas raízes reais
// Calcular as raízes reais
// Imprimir as raízes reais

#include <stdio.h>
#include <math.h>
int main()
{
    float a, b, c;
    float delta, x1, x2;
    printf("Digite a: ");
    scanf("%f", &a);
    printf("Digite b: ");
    scanf("%f", &b);
    printf("Digite c: ");
    scanf("%f", &c);

    delta = pow(b, 2) - 4 * a * c;
    if (delta < 0)
    {
        printf("Não tem raízes reais\n");
    }
    else if (delta == 0)
    {
        x1 = -b / (2 * a);
        printf("Tem uma raiz real: %.2f\n", x1);
    }
    else
    {
        x1 = (-b + sqrt(delta)) / (2 * a);
        x2 = (-b - sqrt(delta)) / (2 * a);
        printf("Tem duas raízes reais: %.2f e %.2f\n", x1, x2);
    }
}