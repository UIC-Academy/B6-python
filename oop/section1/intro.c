#include <stdio.h>


typedef struct phone {
    char name[50];
    int year;
    int price;
    char color[20];

    void (*call)(struct phone* p);
    void (*play)(struct phone* p);
} Phone;

void call(Phone* p){
    printf("Calling...\n");
}

void play(Phone* p){
    printf("Playing...\n");
}

int main(void){
    Phone p1 = {
        .name="Honor",
        .year=2024,
        .price=180,
        .color="black"
    };

    printf("%s\n", p1.name);
    p1.call(&p1);

    return 0;
}