len(Lista, N) :- len(Lista, 0, N).
len([], N, N).
len([_|T], N, Acc) :-
    Nnew is N+1,
    len(T, Nnew, Acc).

average(Lista, Output) :-
    len(Lista, N),
    average(Lista, N, 0, Output).
average([], N, Sum, Output) :-
    Output is Sum / N.
average([H|T], N, Sum, Output) :-
    NewSum is Sum + H,
    average(T, N, NewSum, Output).

variance(Lista, Output) :-
    average(Lista, Avg),
    len(Lista, N),
    licz_wariancje(Lista, Avg, N, 0, Output).

licz_wariancje([], _, Denominator, Sum, Output) :-
    Output is Sum / Denominator.

licz_wariancje([H|T], Avg, Denominator, Sum, Output) :-
    NewSum is Sum + (H - Avg)*(H-Avg),
    licz_wariancje(T, Avg, Denominator, NewSum, Output).