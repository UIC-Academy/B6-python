#include <stdio.h>

int add(int a, int b);
int subtract(int a, int b);

int main(void){
    int (*add_ptr)(int x, int y);
    int (*subtract_ptr)(int x, int y);

    add_ptr = add;
    subtract_ptr = subtract;

    int (*operations[2])(int, int);
    operations[0] = add_ptr;
    operations[1] = subtract_ptr;

    int res = operations[0](2,3);

    printf("%d\n", res);

    return 0;
}


int add(int a, int b){
    return a + b;
}

int subtract(int a, int b){
    return a - b;
}