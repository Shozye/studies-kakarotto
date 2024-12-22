generuj([X], X).
generuj(Lista, Output) :-
    append(L, R, Lista),
    L = [_|_],
    R = [_|_],
    generuj(L, Lout),
    generuj(R, Rout),
    (
        Output = (Lout + Rout);
        Output  = (Lout - Rout);
        Output  = (Lout * Rout);
        Output  = (Lout / Rout)
    ).

wyrażenie(Lista, Value, Output):-
    generuj(Lista, Output),
    catch(Value is Output, _,fail),!.  
