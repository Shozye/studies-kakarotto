%% join/3 to reguła łącząca listy. 
%% Output - 3 argument
join([], Lista2, Lista2).
join(Lista1, Lista2, Output) :-
    Lista1 = [H|T],
    join(T, Lista2, Output2),
    Output = [H|Output2].

%% len/3 to szybkie liczenie dlugosci listy.
%% Output - 3 argument
len([], N, N).
len([_|T], N, Acc) :-
    Nnew is N+1,
    len(T, Nnew, Acc).

%% insert/4 to funkcja wsadzająca element w dane miejsce
%% 1 argument - element do wsadzenia
%% 2 argument - lista w którą wsadzamy
%% 3 argument - index w którą wsadzamy
%% 4 argument - Output
insert(X, Lista, 0, Output) :-
    Output = [X|Lista].
insert(X, [Head|T], Index, Output) :-
    Index > 0,
    IndexNext is Index-1,
    insert(X, T, IndexNext, Output1),
    Output = [Head|Output1].

%% range/3 Funkcja zwracająca listę z liczbami pokolei
%% 1 argument - start
%% 2 argument - end
%% 3 argument - output
range(End, End, [End]).
range(Start, End, Output) :-
    Start =< End,
    NextStart is Start + 1,
    range(NextStart, End, Output2),
    Output = [Start|Output2].

%% find/4 to funkcja znajdująca elementy i zwracające ich index i ogon
%% 1 argument - Element szukany
%% 2 argument - Lista, po której szukamy
%% 3 argument - Index znalezionego elementu
%% 4 argument - Ogon od znalezionego elementu
%% example: find(1,[1,2,1],Output,Tail).
%% Output=0, Tail = [2,1];
%% Output=2, Tail = [];
%% false.
find(N, [N|T], 0, T).
find(N, [H|T], Output, Tail) :-
    find(N, T, Output2, Tail2),
    Output is Output2 + 1,
    Tail = [H|Tail2].

%% findOne/4 to funkcja przyjmująca te same argumenty co find
%% ale znajduje tylko jeden, pierwszy element i dalej nie szuka.
%% example: find(1,[1,2,1],Output,Tail).
%% Output=0, Tail = [2,1];
%% false.
findOne(N, Lista, Output, Tail) :-
    find(N, Lista, Output, Tail),!.

%% Funkcja sprawdzajaca czy X spelnia wymogi Listy z zadania
%% Zmienna Base posiada 2*N elementow oraz Kazdy element jest dwukrotnie
%% Nastepnie funkcja permutation dobieramy sobie permutacje tego Base
%% zauwazamy ze powyzsze wlasnosci sie zachowuja
%% wiec PossibleX zawsze je spelnia
%% Nastepnie jest sprawdzenie że nie istnieje taki element
%% ktory jest oddalony od drugiego tego samego
%% o nieparzysta ilosc
listaPowtarzana(N, X) :-
    range(1, N, Range),
    join(Range, Range, Base), % dla range = [1,2,3] to Base = [1,2,3,1,2,3]
    permutation(Base, PossibleX), % PossibleX to dowolna permutacja Base
    \+ ( member(Num, Range),
    findOne(Num, PossibleX, IndexOfNum, Tail),
    findOne(Num, Tail, IndexOf2ndNum, _),
    Diff is IndexOf2ndNum - IndexOfNum,
    Diff mod 2 =:= 1 ),
    X = PossibleX.
    
%% Wrapper na ListaPowtarzana zeby nie duplikowala wartosci
lista(N, X) :-
    distinct(listaPowtarzana(N, X)).
    


