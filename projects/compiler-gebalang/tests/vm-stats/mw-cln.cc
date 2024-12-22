/*
 * Kod interpretera maszyny rejestrowej do projektu z JFTT2022
 *
 * Autor: Maciek Gębala
 * http://ki.pwr.edu.pl/gebala/
 * 2022-11-22
 * (wersja cln)
*/
#include <iostream>
#include <locale>

#include <utility>
#include <vector>
#include <map>

#include <cstdlib> 	// rand()
#include <ctime>

#include <cln/cln.h>

#include "instructions.hh"
#include "colors.hh"

using namespace std;
using namespace cln;

void run_machine( vector< pair<int,long long> > & program )
{
  map<cl_I,cl_I> p;

  int lr;

  long long io, ari, mem, jump;
  lr = 0;
  io = 0;
  ari = 0;
  mem = 0;
  jump = 0;
  while( program[lr].first!=HALT )	// HALT
  {
     if( program[lr].second<0 )
     {
         cerr << "ERROR: 2" << endl;
         exit(-1);
     }
     switch( program[lr].first )
     {
      case GET:	   cout << "? ";    cin >> p[program[lr].second];                        io+=100; lr++; break;
      case PUT:	   cout << "> " << p[program[lr].second] << endl;                        io+=100; lr++; break;

      case LOAD:	 p[0]                     = p[program[lr].second];                     mem+=10; lr++; break;
      case STORE:	 p[program[lr].second]    = p[0];                                      mem+=10; lr++; break;
      case LOADI:	 p[0]                     = p[p[program[lr].second]];                  mem+=10; lr++; break;
      case STOREI: p[p[program[lr].second]] = p[0];                                      mem+=10; lr++; break;

      case ADD:	   p[0] += p[program[lr].second];                                        ari+=10; lr++; break;
      case SUB:	   p[0] -= p[0]>=p[program[lr].second]?p[program[lr].second]:p[0];       ari+=10; lr++; break;
      case ADDI:   p[0] += p[p[program[lr].second]];                                     ari+=10; lr++; break;
      case SUBI:   p[0] -= p[0]>=p[p[program[lr].second]]?p[p[program[lr].second]]:p[0]; ari+=10; lr++; break;
      case SET:	   p[0]  = program[lr].second;                                           ari+=10; lr++; break;
      case HALF:	 p[0]  = floor1(p[0],2);                                               ari+= 5; lr++; break;

      case JUMP: 	              lr = program[lr].second;                                 jump+=1; break;
      case JPOS:	if( p[0]>0 )  lr = program[lr].second; else lr++;                      jump+=1; break;
      case JZERO:	if( p[0]==0 ) lr = program[lr].second; else lr++;                      jump+=1; break;
      case JUMPI:               lr = cl_I_to_int(p[program[lr].second]);                 jump+=1; break;
      default: break;
    }
    if( lr<0 || lr>=(int)program.size() )
    {
      cerr << "ERROR: 2" << endl;
      exit(-1);
    }
  }
  cout.imbue(std::locale(""));
  cout << "sum: "    << io + ari + mem + jump << " "
    "" << "; io: "   << io                    << " "
          "; ari: "  << ari                   << " "
          "; mem: "  << mem                   << " "
          "; jump: " << jump                  << endl;
}
