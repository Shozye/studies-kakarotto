/*
 * Kod interpretera maszyny rejestrowej do projektu z JFTT2022
 *
 * Autor: Maciek Gębala
 * http://ki.pwr.edu.pl/gebala/
 * 2022-11-22
 * (wersja long long)
*/
#include <iostream>
#include <locale>

#include <utility>
#include <vector>
#include <map>

#include <cstdlib> 	// rand()
#include <ctime>

#include "instructions.hh"
#include "colors.hh"

using namespace std;

string enum_to_name(int e){
    switch(e)
    {
      case GET:	   return "GET";
      case PUT:	  return "PUT";

      case LOAD:return "LOAD";
      case STORE:	return "STORE";
      case LOADI:	 return "LOADI";
      case STOREI: return "STOREI";

      case ADD:	  return "ADD";
      case SUB:	 return "SUB";
      case ADDI: return "ADDI";
      case SUBI:   return "SUBI";
      case SET:	   return "SET";
      case HALF:	return "HALF";

      case JUMP: 	 return "JUMP";
      case JPOS:	return "JPOS";
      case JZERO:	return "JZERO";
      case JUMPI: 	return "JUMPI";
      default: return "LOLE";
    }
}

void run_machine( vector< pair<int,long long> > & program )
{
  map<long long,long long> p;

  int lr;

  long long io, ari, mem, jump;

  cout << cBlue << "Uruchamianie programu." << cReset << endl;
  lr = 0;
  io = 0;
  ari = 0;
  mem = 0;
  jump = 0;
  while( program[lr].first!=HALT )	// HALT
  {
     if( program[lr].second<0 )
     {
         cerr << cRed << "Błąd: ujemny adres pamięci lub skoku." << cReset << endl;
         exit(-1);
     }
     cout << enum_to_name(program[lr].first) <<" "<< program[lr].second << " line: " << lr << endl;
     switch( program[lr].first )
     {
      case GET:	   cout << "? ";    cin >> p[program[lr].second];                        io+=100; lr++;  break;
      case PUT:	   cout << "> " << p[program[lr].second] << endl;                        io+=100; lr++;  break;

      case LOAD:	 p[0]                     = p[program[lr].second];                     mem+=10; lr++;  break;
      case STORE:	 p[program[lr].second]    = p[0];                                      mem+=10; lr++;  break;
      case LOADI:	 p[0]                     = p[p[program[lr].second]];                  mem+=10; lr++; break;
      case STOREI: p[p[program[lr].second]] = p[0];                                      mem+=10; lr++;  break;

      case ADD:	   p[0] += p[program[lr].second];                                        ari+=10; lr++;  break;
      case SUB:	   p[0] -= p[0]>=p[program[lr].second]?p[program[lr].second]:p[0];       ari+=10; lr++;  break;
      case ADDI:   p[0] += p[p[program[lr].second]];                                     ari+=10; lr++; break;
      case SUBI:   p[0] -= p[0]>=p[p[program[lr].second]]?p[p[program[lr].second]]:p[0]; ari+=10; lr++; break;
      case SET:	   p[0]  = program[lr].second;                                           ari+=10; lr++; break;
      case HALF:	 p[0] /= 2;                                                            ari+= 5; lr++; break;

      case JUMP: 	              lr = program[lr].second;                                 jump+=1; break;
      case JPOS:	if( p[0]>0 )  lr = program[lr].second; else lr++;                      jump+=1; break;
      case JZERO:	if( p[0]==0 ) lr = program[lr].second; else lr++;                      jump+=1; break;
      case JUMPI: 	            lr = p[program[lr].second];                              jump+=1; break;
      default: break;
    }
    if( lr<0 || lr>=(int)program.size() )
    {
      cerr << cRed << "Błąd: Wywołanie nieistniejącej instrukcji nr " << lr << "." << cReset << endl;
      exit(-1);
    }
  }
  cout.imbue(std::locale(""));
  cout << cBlue << "Skończono program (koszt: " << cRed << io + ari + mem + jump << ""
    "" << cBlue << "; io:" << io << ""
                   "; ari:" << ari << ""
                   "; mem:" << mem << ""
                   "; jump:" << jump << ""
                   "" << cReset << endl;
}
