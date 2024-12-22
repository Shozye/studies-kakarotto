/*
 * Kod maszyny wirtualnej do projektu z JFTT2022
 *
 * Autor: Maciek Gębala
 * http://ki.pwr.edu.pl/gebala/
 * 2022-11-22
*/
#include <iostream>

#include <utility>
#include <vector>

#include "colors.hh"

using namespace std;

extern void run_parser( vector< pair<int,long long> > & program, FILE * data );
extern void run_machine( vector< pair<int,long long> > & program );

int main( int argc, char const * argv[] )
{
  vector< pair<int,long long> > program;
  FILE * data;

  if( argc!=2 )
  {
    cerr << "ERROR: 0" << endl;
    return -1;
  }

  data = fopen( argv[1], "r" );
  if( !data )
  {
    cerr << cRed << "ERROR: 0" << endl;
    return -1;
  }

  run_parser( program, data );

  fclose( data );

  run_machine( program );

  return 0;
}
