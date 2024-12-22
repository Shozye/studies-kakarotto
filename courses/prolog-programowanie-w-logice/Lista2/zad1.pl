
mid([_|SlowTail], [_, _|FastTail], Mid) :-
    mid(SlowTail, FastTail, Mid).


mid([Slow|_], [_|Fast], Mid) :- 
    \+ (Fast = [_|_]),

    Slow = Mid.

srodkowy(L, X) :-
    mid(L, L, X).