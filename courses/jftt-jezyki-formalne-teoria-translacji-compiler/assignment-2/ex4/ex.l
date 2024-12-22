%{
    #define STACK_SIZE 100000
    int error = 0;
    void report_error(char* text){
        printf("Error: %s\n", text);
        error = 1;
    }
    // STACK RELATED FUNCTIONS START
    int ptr = 0;
    int stack[STACK_SIZE];
    void push(int num){
        stack[ptr] = num;
        if(ptr < STACK_SIZE-1){
            ptr++;
        } else {
            report_error("Too many numbers in stack!");
        }
    }
    int get(){
        ptr--;
        if(ptr < 0){
            report_error("Not enough numbers provided");
            return 0;
        }
        return stack[ptr];
    }
    // STACK RELATED FUNCTIONS END
    int left;
    int right;
    void restore(){
        ptr = 0;
        error = 0;
    }
    void get_args(){
        right = get();
        left = get();
    }

    void _add(){
        get_args(); if(error){return;};
        push(left + right);
    }
    void _sub(){
        get_args(); if(error){return;};
        push(left - right);
    }
    void _mul(){
        get_args(); if(error){return;};
        push(left * right);
    }
    void _div(){
        get_args(); if(error){return;};
        if(right == 0){
            report_error("Right side of division cannot be 0");
            return;
        }
        push(left / right);
    }
    void _exp(){
        get_args(); if(error){return;};
        if(right < 0){
            report_error("Right side of exponent cannot be negative");
            return;
        }
        int result = 1;
        for(int i = 0; i < right; i++){
            result *= left;
        }
        push(result);
    }
    void _mod(){
        get_args(); if(error){return;};
        if(right == 0){
            report_error("Right side of modulo cannot be 0");
            return;
        }
        push(left % right);
    }
    
    void print_result(){
        if(ptr != 1){
            if(ptr < 1){
                report_error("No numbers given. Can't print result");
            } else {
                report_error("Not enough operands");
            }
            return;
        }
        printf("= %d\n", get());
    }
%}

DIGIT   [0-9]
NUMBER  "-"*[0-9]+
%x OMIT
%%

{NUMBER}  {push(atoi(yytext));}
" "
\+ { _add(); if(error){BEGIN(OMIT);}; };
\- { _sub(); if(error){BEGIN(OMIT);}; };
\* { _mul(); if(error){BEGIN(OMIT);}; };
\/ { _div(); if(error){BEGIN(OMIT);}; };
\^ { _exp(); if(error){BEGIN(OMIT);}; };
\% { _mod(); if(error){BEGIN(OMIT);}; };
\n { print_result(); restore(); };
[^ 0123456789\+\-\*\/\^\%\n]  {
    char msg[30] = "Wrong symbol: ";
    strcat(msg, yytext);
    report_error(msg); 
    BEGIN(OMIT);
}

<OMIT>{
    .
    \n {BEGIN(INITIAL); restore();}
}

%%
  
int yywrap(){}
int main(){
      yylex();
      return 0;
}