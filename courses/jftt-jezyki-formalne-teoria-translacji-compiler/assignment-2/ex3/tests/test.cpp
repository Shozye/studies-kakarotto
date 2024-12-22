#include "test/*asdf*/header.h"
#include <stdio.h>
//#include <foo/*bar*/baz.h>

/** \brief Java style Doc String - Foo function */
int foo(){printf("FOO\n"); return 0;};

int bar(); /**< Bar function */

/// .NET Style Doc String
int g_global_var = 1;

/* Hello
/* World
// */
int baz(){printf("BAZ\n");return 0;};
// */

/*! Global variable
 *  ... */
volatile int g_global;

//! Main
int main(int argc, char ** argv)
{
    printf("/* foo bar\n");
    //*/ bar();

    // \
    /*
    baz();
    /*/
    foo();
    //*/
/\
/*
    baz();
/*/
    foo();
//*/

    return 1;
}
