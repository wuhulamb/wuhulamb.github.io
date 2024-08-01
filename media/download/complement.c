#include <stdio.h>
#include <string.h>
#define N 8                       // 8位二进制数
// 计算十进制数int a的补码
                      
// 将十进制数int a转换为二进制并存入s
void binary (int a, char * s) {   // 0 <= a <= 127
    int m, i;
    for (i = 0; i < N ; i ++) {   // 8为字符数组长度
        s[i] = '0';               // 初始赋值为0
    }
    i = strlen(s) - 1;
    do {
        m = a % 2;
        s[i] = m + 48;            // '0'的ASCII码值是48，将int m转换为字符
        i --;
        a = a / 2;
    } while (a > 0);
}

// 将s里的二进制数转换为十进制数int k
int decimal (char * s) {
    int i, k = 0, p = 1;
    for (i = N - 1; i >= 0; i --) {
        k = k + (s[i] - 48) * p;
        p = p * 2;
    }
    return k;
}

// 计算十进制数int a的补码，并存入s
void complement(int a, char * s) {    // -128 <= a <= 127
    int i, k;
    if (a >= 0) {
        binary(a, s);
    }
    else {
        binary(-1 * a, s);
        for (i = 1; i < N; i ++) {    // 除第1位取反
            s[i] = '1' - s[i] + '0';
        }
        k = decimal(s) + 1;           // 加1
        binary(k, s);
        s[0] = '1';                   // 第1位赋值1
    }
}

int main(void) {
    int a;            // -128 <= a <= 127
    char s[N + 1];    // n + 1，最后一位是\0，表示终止
    printf("Input a (-128 <= a <= 127): ");
    scanf("%d", &a);
    complement(a, s);
    printf("Complement of a: %s\n", s);
    printf("Decimal of complement: %d\n", decimal(s));
    return 0;
}
