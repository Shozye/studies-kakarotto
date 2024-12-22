#include<string>
#include<iostream>
extern int yyerror(std::string s);

int _neg(int a, int P){
    while (a < 0){a += P;}
    return a;
}

int _add(int a, int b, int P){
    return (a + b)%P;
}
int _sub(int a, int b, int P){
    return _add(a, _neg(-b, P), P);
}
int _mul(int a, int b, int P){
    return (int)((long long)a*b % P);
}

int inverse(int a, int P){
    for(int i = 0; i < P; i++){
        if(_mul(a, i, P) == 1){return i;}
    }
    return -1;
}

int _div(int a, int b, int P){
    if (b == 0){return -1;}
    int inv = inverse(b, P);
    if (inv == -1){return -1;}
    return _mul(a, inv, P);
}
int _pow(int a, int pow, int P){
    if (pow == 0)
        return 1;
    int b = _pow(a, pow/2, P);
    b = _mul(b,b, P);
    if ( pow % 2 == 0 )
        return b;
    return _mul(b, a, P);
}