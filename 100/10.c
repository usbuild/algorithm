#include <stdio.h>
#include <string.h>
void reverse_part(char str[], int start, int end) {
    int i = start, j = end - 1;
    for(;i < j; ++i, --j){
        char tmp = str[i];
        str[i] = str[j];
        str[j] = tmp;
    }
}
void reverse(char str[]) {
    reverse_part(str, 0, strlen(str));
    int start = 0, end = 1;
    for(; ; ++end) {
        if (str[end] == ' ') {
            reverse_part(str, start, end);
            start = end + 1;
        }
        if (str[end] == '\0') {
            reverse_part(str, start, end);
            start = end + 1;
            break;
        }
    }
}
int main(int argc, const char *argv[])
{
    char str[] = "I am a student.";
    reverse(str);
    puts(str);
    return 0;
}
