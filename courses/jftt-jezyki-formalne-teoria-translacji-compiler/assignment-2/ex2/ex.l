%{
%}

%x IN_STRING_0
%x IN_STRING_1
%x IN_STRING_2
%x COMMENT
%%

#           {BEGIN(COMMENT);}
'           {ECHO;BEGIN(IN_STRING_0);}
\"          {ECHO;BEGIN(IN_STRING_1);}
\"\"\"      {ECHO;BEGIN(IN_STRING_2);}

<COMMENT>{
    "\n"        {BEGIN(INITIAL);ECHO;}
    .           
}

<IN_STRING_0>{
    \\"'"       {ECHO;}
    "'"         {ECHO;BEGIN(INITIAL);}
}

<IN_STRING_1>{
    \\"\""      {ECHO;}
    "\""        {ECHO;BEGIN(INITIAL);}
}

<IN_STRING_2>{
    \\"\"\"\""  {ECHO;}
    "\"\"\""    {ECHO;BEGIN(INITIAL);}
}

%%
  
int yywrap(){}
int main(){
      yylex();
      return 0;
}