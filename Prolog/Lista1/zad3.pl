
member(X, [X|_]).
member(X, [_|T]) :- member(X, T).

isCompound(P, List) :-
    member(PrevPrime, List),
    0 is P mod PrevPrime,
    !.

createPrimeList(2, [2]).

createPrimeList(HI, List) :-
    Lower is HI-1,
    Lower > 1,
    createPrimeList(Lower, ListLower),
    (
        (
            isCompound(HI, ListLower),
            List = ListLower
        );
        ( 
            (\+isCompound(HI, ListLower)),
            List = [HI|ListLower]
        )
    ).

prime(LO, HI, N) :-
    NewHI is floor(sqrt(HI)),
    createPrimeList(NewHI, List),
    member(N, List),
    N >= LO,
    N =< HI.


