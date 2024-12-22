mały(0,3,4,7).
mały(1,4,5,8).
mały(2,5,6,9).
mały(7,10,11,14).
mały(8,11,12,15).
mały(9,12,13,16).
mały(14,17,18,21).
mały(15,18,19,22).
mały(16,19,20,23).

średni(0,1,3,5,10,12,14,15).
średni(1,2,4,6,11,13,15,16).
średni(7,8,10,12,17,19,21,22).
średni(8,9,11,13,18,20,22,23).

duży(0,1,2,3,6,10,13,17,20,21,22,23).

małe(_, [], IleJest, IleJest).
małe(Lista, DoSprawdzenia, IleJest, IleOstatecznie) :-
    DoSprawdzenia = [[A, B, C ,D] | Ogon],
    ((nth0(A, Lista, zapałka), 
     nth0(B, Lista, zapałka), 
     nth0(C, Lista, zapałka), 
     nth0(D, Lista, zapałka)) ->
     (IleJest2 is IleJest + 1)
    ; IleJest2 is IleJest ),
    małe(Lista, Ogon, IleJest2, IleOstatecznie).

liczmale(Lista, IleMalych) :-
    DoSprawdzenia = [[0,3,4,7], [1,4,5,8], [2,5,6,9],
            [7,10,11,14], [8,11,12,15], [9,12,13,16],
            [14,17,18,21], [15,18,19,22], [16,19,20,23]],
    małe(Lista, DoSprawdzenia, 0, IleMalych).

średnie(_, [], IleJest, IleJest).
średnie(Lista, DoSprawdzenia, IleJest, IleOstatecznie) :-
    DoSprawdzenia = [[Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8] | Ogon],
    ((nth0(Z1, Lista, zapałka), 
     nth0(Z2, Lista, zapałka), 
     nth0(Z3, Lista, zapałka), 
     nth0(Z4, Lista, zapałka),
     nth0(Z5, Lista, zapałka),
     nth0(Z6, Lista, zapałka),
     nth0(Z7, Lista, zapałka),
     nth0(Z8, Lista, zapałka)) ->
     IleJest2 is IleJest + 1
    ; IleJest2 is IleJest ),
    średnie(Lista, Ogon, IleJest2, IleOstatecznie).

liczśrednie(Lista, Ile) :-
    DoSprawdzenia = [[0,1,3,5,10,12,14,15],
                    [1,2,4,6,11,13,15,16],
                    [7,8,10,12,17,19,21,22],
                    [8,9,11,13,18,20,22,23]],
    średnie(Lista, DoSprawdzenia, 0, Ile).

duże(_, [], IleJest, IleJest).
duże(Lista, DoSprawdzenia, IleJest, IleOstatecznie) :-
    DoSprawdzenia = [[Z1, Z2, Z3, Z4, Z5, Z6, Z7, Z8, Z9, Z10, Z11, Z12] | Ogon],
    ((nth0(Z1, Lista, zapałka), 
     nth0(Z2, Lista, zapałka), 
     nth0(Z3, Lista, zapałka), 
     nth0(Z4, Lista, zapałka),
     nth0(Z5, Lista, zapałka),
     nth0(Z6, Lista, zapałka),
     nth0(Z7, Lista, zapałka),
     nth0(Z8, Lista, zapałka),
     nth0(Z9, Lista, zapałka),
     nth0(Z10, Lista, zapałka),
     nth0(Z11, Lista, zapałka),
     nth0(Z12, Lista, zapałka)) ->
     IleJest2 is IleJest + 1
    ; IleJest2 is IleJest ),
    duże(Lista, Ogon, IleJest2, IleOstatecznie).

liczduże(Lista, Ile) :-
    DoSprawdzenia = [[0,1,2,3,6,10,13,17,20,21,22,23]],
    duże(Lista, DoSprawdzenia, 0, Ile).



generuj(0, ListaWyjscie, 24, ListaWyjscie).
generuj(IleZapalek, ListaWejscie, Dlugosc, ListaWyjscie) :-
    append(ListaWejscie, [zapałka], Wyjscie),
    Dlugosc2 is Dlugosc + 1,
    IleZapalek2 is IleZapalek - 1,
    Dlugosc2 =< 24, IleZapalek2 >= 0,
    generuj(IleZapalek2, Wyjscie, Dlugosc2, ListaWyjscie).
generuj(IleZapalek, ListaWejscie, Dlugosc, ListaWyjscie) :-
    append(ListaWejscie, [pusto], Wyjscie),
    Dlugosc2 is Dlugosc + 1,
    IleZapalek2 is IleZapalek,
    Dlugosc2 =< 24, IleZapalek2 >= 0,
    generuj(IleZapalek2, Wyjscie, Dlugosc2, ListaWyjscie).

pion(3).
pion(4).
pion(5).
pion(6).

pion(10).
pion(11).
pion(12).
pion(13).

pion(17).
pion(18).
pion(19).
pion(20).

poziom(Liczba) :-
    \+ pion(Liczba).


narysujJeden(zapałka, Licznik) :-
    pion(Licznik),
    write("|   ").
narysujJeden(pusto, Licznik) :-
    pion(Licznik),
    write("    ").

narysujJeden(zapałka, Licznik) :-
    poziom(Licznik),
    write("+---").

narysujJeden(pusto, Licznik) :-
    poziom(Licznik),
    write("+   ").


narysuj([Elem | Tail], Licznik) :-
    narysujJeden(Elem, Licznik),
    ((Licznik=2; Licznik=9; Licznik=16; Licznik=23) -> write("+\n"); write("")),
    ((Licznik=6; Licznik=13; Licznik=20) -> write("\n"); write("")),
    Licznik2 is Licznik + 1,
    narysuj(Tail, Licznik2).
narysuj([], 24).


zapałki(KChosen, D, S, M, Lista) :-
    between(0, 24, K),
    KChosen = K,
    IleZapalek is 24-K,
    generuj(IleZapalek, [], 0, Lista),
    
    liczmale(Lista, M),
    liczśrednie(Lista, S),
    liczduże(Lista, D),
    narysuj(Lista, 0).

test(Lista) :-
    generuj(24, [], 0, Lista),
    write("OK"),
    narysuj(Lista, 0).

test2(Lista) :-
    generuj(24, [], 0, Lista),
    write("OK").

test3(Lista) :-
    Lista = [pusto, zapałka, zapałka, zapałka, zapałka, pusto, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka, zapałka],
    write("OK\n"),
    narysuj(Lista, 0).

test4(D, S, M) :-
    Lista = [zapałka, zapałka, zapałka, 
            zapałka, zapałka, zapałka, zapałka,
            pusto, pusto, zapałka,
            zapałka, zapałka, zapałka, zapałka,
            zapałka, zapałka, zapałka,
            zapałka, pusto, pusto, zapałka,
            zapałka, zapałka, zapałka
            ],
    liczduże(Lista, D),
    liczśrednie(Lista, S),
    liczmale(Lista, M),
    narysuj(Lista, 0).