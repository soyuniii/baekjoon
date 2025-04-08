#include <stdio.h>

int main() {
    int a, b, c, d, e;
    scanf("%d %d %d %d %d", &a, &b, &c, &d, &e);

    int num = (a*a + b*b + c*c + d*d + e*e) % 10;

    printf("%d\n", num);
    return 0;
}