arc(1,2).
arc(1,3).
arc(2,3).
arc(2,4).
arc(3,5).
arc(5,4).
arc(4,6).
arc(6,7).
arc(7,5).
arc(10,11).
arc(11,12).

%% 1 ----> 2 ----> 3        10
%% |       |       |        |
%% \/      \/      \/       \/
%% 3       4 <---- 5        11
%%         |       ^        |
%%         \/      |        \/
%%         6 ----> 7        12

osiagalny_mem(Begin, PreviousVisited):-
    

osiagalny_mem(Begin, List) :-
    arc(Begin, X),
    osiagalny_mem(X, List2),
    member(Member, List2),
    member(Member, List).
