mezczyzna(men1).
mezczyzna(men2).
mezczyzna(men3).
mezczyzna(men4).
mezczyzna(men5).
mezczyzna(men6).

kobieta(wom1).
kobieta(wom2).
kobieta(wom3).
kobieta(wom4).
kobieta(wom5).
kobieta(wom6).
kobieta(wom7).

ojciec(men1, men2).
ojciec(men1, men3).
ojciec(men1, wom1).
ojciec(men3, men4).
ojciec(men3, men6).
ojciec(men5, wom5).

matka(wom2, men2).
matka(wom3, men3).
matka(wom4, men4).
matka(wom5, men6).


rodzic(X, Y) :- matka(X, Y); ojciec(X, Y).
diff(X, Y) :- X \= Y.

