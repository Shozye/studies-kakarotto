jest_matka(X) :- matka(X, _).
jest_ojcem(X) :- ojciec(X, _).

jest_synem(X) :- mezczyzna(X), rodzic(_, X).
siostra(X, Y) :- kobieta(X), rodzic(Rodzic, Y), rodzic(Rodzic, X), diff(X, Y).
dziadek(X, Y) :- mezczyzna(X), rodzic(Rodzic, Y), ojciec(X, Rodzic).
rodzenstwo(X, Y) :- rodzic(Z, X), rodzic(Z, Y), diff(X, Y).
