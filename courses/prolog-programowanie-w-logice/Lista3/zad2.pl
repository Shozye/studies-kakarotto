max_sum(List, MaxSum) :-
    max_sum(List, 0, 0, MaxSum).

max_sum([], _, GlobalMax, GlobalMax).
max_sum([H|T], MaxBefore, GlobalMax, Output) :-
    MaxBeforePlusH is MaxBefore + H,
    (MaxBeforePlusH > H -> NewMaxBefore is MaxBeforePlusH; NewMaxBefore is H),
    (MaxBefore > GlobalMax -> NewGlobalMax is MaxBefore; NewGlobalMax is GlobalMax),
    max_sum(T, NewMaxBefore, NewGlobalMax, Output).
