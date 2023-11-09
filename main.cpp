#include <stdio.h>

int main (){
    char* str = "Nvidia Tegra";
    void *ptr = &str;
    printf("%s", *(char**)ptr);
    //printf("%s", ??ptr??);//print the string changing only this line
    return 0;
}