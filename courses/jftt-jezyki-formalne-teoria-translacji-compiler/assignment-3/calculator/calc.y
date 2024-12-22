
%{
  #include<iostream>
  #include<string>
  #include"../utils.hpp"
  #define P 1234577

  extern int yylex(void);
  extern int yyparse();
  void yyerror(std::string s);
  std::string notation = "";
%}
%define api.value.type { int }
%token NUM
%token LBR
%token RBR
%token ADD
%token SUB
%token MUL
%token DIV
%token POW
%token ERR
%type expr
%type number
%type line


%left ADD SUB
%left MUL DIV
%left NEG
%nonassoc POW


%%
input: 
    %empty
    | input line 
;
line: 
    expr '\n' { 
      std::cout << "Notation: " << notation << std::endl;
      std::cout << "Result: " << $1 << std::endl;
      notation = "";
    }
    | error '\n' { 
      yyerrok ;
    }
;
expr: 
    number { $$ = $1; notation += std::to_string($1) + " "; }
    | SUB LBR expr RBR %prec NEG { $$ = _neg(-$3, P); notation += "- "; }
    | LBR expr RBR { $$ = $2; }
    | expr ADD expr { $$ = _add($1, $3, P); notation += "+ "; }
    | expr SUB expr { $$ = _sub($1, $3, P); notation += "- "; }
    | expr MUL expr { $$ = _mul($1, $3, P); notation += "* "; }
    | expr DIV expr {
      int res = _div($1, $3, P);
      if (res == -1){
        yyerror("blad");
        YYERROR;
      } else {
        $$ = res; 
        notation += "/ ";
      }
    }
    | expr POW powexpr { $$ = _pow($1, $3, P); notation += "^ "; }
;

number: 
    NUM { $$ = $1 % P; }
    | SUB NUM %prec NEG { $$ = _neg(-$2, P); }

powexpr:
    pownumber { $$ = $1; notation += std::to_string($1) + " "; }
    | LBR powexpr RBR { $$ = $2; }
    | SUB LBR powexpr RBR %prec NEG { $$ = _neg(-$3, P-1); notation += "- "; }
    | powexpr ADD powexpr { $$ = _add($1, $3, P-1); notation += "+ "; }
    | powexpr SUB powexpr { $$ = _sub($1, $3, P-1); notation += "- "; }
    | powexpr MUL powexpr { $$ = _mul($1, $3, P-1); notation += "* "; }
    | powexpr DIV powexpr { 
      int res = _div($1, $3, P-1);
      if (res == -1){
        yyerror("blad"); 
        YYERROR;
      } else {
        $$ = res; 
        notation += "/ ";
      }
    }

pownumber: 
    NUM { $$ = $1 % (P-1); }
    | SUB NUM %prec NEG { $$ = _neg(-$2, P-1); }

%%

void yyerror(std::string s){
  std::cout << "Błąd" << std::endl;
}
int main(){
  yyparse();
  return 0;
}

