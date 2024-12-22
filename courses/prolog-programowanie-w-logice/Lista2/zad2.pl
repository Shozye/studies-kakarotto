accCounter(X, [X|T], A, Acc) :-
    Anew is A+1,
    accCounter(X, T, Anew, Acc).

accCounter(X, [H|T], A, Acc) :-
    accCounter(X, T, A, Acc),
    \+ (X=H).

accCounter(_, [], Acc, Acc).

jednokrotnie(X, L) :-
    accCounter(X, L, 0, Acc),
    Acc is 1.

dwukrotnie(X, L) :-
    accCounter(X, L, 0, Acc),
    Acc is 2.