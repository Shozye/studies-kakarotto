join([], Lista2, Lista2).
join(Lista1, Lista2, Output) :-
    Lista1 = [H|T],
    join(T, Lista2, Output2),
    Output = [H|Output2].

len([], N, N).
len([_|T], N, Acc) :-
    Nnew is N+1,
    len(T, Nnew, Acc).

insert(X, Lista, 0, Output) :-
    Output = [X|Lista].

insert(X, [Head|T], Index, Output) :-
    Index > 0,
    IndexNext is Index-1,
    insert(X, T, IndexNext, Output1),
    Output = [Head|Output1].
    
range(End, End, [End]).
range(Start, End, Output) :-
    Start =< End,
    NextStart is Start + 1,
    range(NextStart, End, Output2),
    Output = [Start|Output2].

bazowaLista(N, Lista) :-
    range(1, N, Range),
    join(Range, Range, PodwojneOdliczenie),
    Lista = PodwojneOdliczenie.


find(N, [N|T], 0, T).
find(N, [H|T], Output, Tail) :-
    find(N, T, Output2, Tail2),
    Output is Output2 + 1,
    Tail = [H|Tail2].

findOne(N, Lista, Output, Tail) :-
    find(N, Lista, Output, Tail),!.


lista(N, X) :-
    range(1, N, Range),
    join(Range, Range, Base),
    permutation(Base, PossibleX),
    \+ ( member(Num, Range),
    findOne(Num, PossibleX, IndexOfNum, Tail),
    findOne(Num, Tail, IndexOf2ndNum, _),
    Diff is IndexOf2ndNum - IndexOfNum,
    Diff mod 2 =:= 1 ),
    X = PossibleX.
    

    


