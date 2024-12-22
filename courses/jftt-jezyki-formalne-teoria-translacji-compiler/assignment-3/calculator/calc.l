/* Mateusz Pełechaty, 261737 */

%option noyywrap
%{
  #include "calc.tab.hpp"
  extern int yylex();
%}

%%
\\\n ;
[[:digit:]]+ { 
    yylval = atoi(yytext); 
    return NUM; 
}
[ \t]  ;
"(" {return LBR;}
")" {return RBR;}
"+" {return ADD;}
"-" {return SUB;}
"*" {return MUL;}
"/" {return DIV;}
"^" {return POW;}
\n  {return '\n';}
^#(.|\\\n)*\n {}
.   {return ERR;}
%%
