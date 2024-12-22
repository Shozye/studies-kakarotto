%{
    int doxygen_flag = 0;
%}

%x STRING
%x MULTILINE_DOCSTRING
%x MULTILINE
%x LINE_DOCSTRING
%x LINE
%%


<INITIAL>{
    "/\\\n/"        {BEGIN(LINE);}
    "\""            {BEGIN(STRING); ECHO;}
    "///"|"//!"     {
        if(doxygen_flag == 1){
            ECHO;
        }
        BEGIN(LINE_DOCSTRING);
        }
    "/**"|"/*!"     {
        if(doxygen_flag == 1){
            ECHO;
        }
        BEGIN(MULTILINE_DOCSTRING);
        }
    "//"            {BEGIN(LINE);}
    "/*"            {BEGIN(MULTILINE);}
}

<STRING>{
    \\"\""          {ECHO;}
    "\""            {BEGIN(INITIAL); ECHO;}
}

<LINE_DOCSTRING>{
    "\n"            {BEGIN(INITIAL); ECHO;}
    .               {
        if(doxygen_flag == 1){
            ECHO;
        }
    }
}

<MULTILINE_DOCSTRING>{
    .               {
        if(doxygen_flag == 1){
            ECHO;
        }
    }
    "*/"            {
        if(doxygen_flag){
            ECHO;
        }
        BEGIN(INITIAL);
    }
}

<LINE>{
    "\\\n"          
    "\n"            {BEGIN(INITIAL); ECHO;}
    .            
}

<MULTILINE>{
    "*/"            {BEGIN(INITIAL);}
    .               
}

%%
  
int yywrap(){}
int main(int argc, char ** argv){

    if ( argc > 1 && ! strcmp(argv[1], "--doxygen")){
        doxygen_flag = 1;
    }
    yylex();
    return 0;
}