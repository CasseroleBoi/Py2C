#include <stdio.h>
typedef unsigned long long type;
typedef int p2c_var;
typedef struct {
    char* data;
    type t;
} p2c_var;


void p2c_printInt(p2c_var arg){
    printf("%d", arg);
}