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
arc(11,10).

%% 1 ----> 2 ----> 3        10
%% |       |       |        |
%% \/      \/      \/       \/
%% 3       4 <---- 5        11
%%         |       ^        |
%%         \/      |        \/
%%         6 ----> 7        12

member(X, Lista) :-
    Lista = [H|T],
    (H = X; member(X, T)).

znajdz_zasieg(X, Visited, Lista) :- 
    arc(X, Y),
    \+ ( member(Y, Visited) ),
    VisitedY = [X|Visited],
    znajdz_zasieg(Y, VisitedY, Lista).

znajdz_zasieg(X, Visited, Lista) :-
    arc(X, Y),
    member(Y, Visited),
    Lista = Visited.

znajdz_zasieg(X, Visited, Lista) :-
    \+(arc(X,_)),
    Lista = [X|Visited].


zasieg(X, Lista) :-
    znajdz_zasieg(X, [], Lista).

osiagalnyBase(X,Y) :- 
    zasieg(X, Lista),
    member(Y, Lista).

osiagalny(X, Y) :-
    distinct(osiagalnyBase(X, Y)).
