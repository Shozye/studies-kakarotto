% Rob reszte drzewa dopoki sa argumenty z których można ją robić. 
% Jeżeli argumenty (druga lista) jest pusta. To reszta drzewa tez jest juz pusta
zrob_reszte_drzewa([], []) :- !.

zrob_reszte_drzewa([DrzewoPierwszegoArgumentu | ResztaDrzewa], [PierwszyArgument | ResztaArgumentow]) :-
    make_tree(PierwszyArgument, DrzewoPierwszegoArgumentu),
    zrob_reszte_drzewa(ResztaDrzewa, ResztaArgumentow),!.

make_tree(Lisc, Drzewo) :-
    Lisc =.. [_ | []],
    Drzewo = [Lisc],!.

make_tree(Term, Drzewo) :-
    Term =.. [_ | ListaArgumentow],
    \+ (ListaArgumentow = []),
    Drzewo = [Term, ResztaDrzewa],
    zrob_reszte_drzewa(ResztaDrzewa, ListaArgumentow),!.

wypisz_indent(0) :- !.
wypisz_indent(Indent) :-
    write(" "),
    Indent__Minus__1 is Indent - 1,
    wypisz_indent(Indent__Minus__1).

wypisz_dzieci([], _).
wypisz_dzieci([Dziecko | ResztaDzieci], Indent) :-
    wypisz_drzewo(Dziecko, Indent),
    wypisz_dzieci(ResztaDzieci, Indent).

wypisz_drzewo(Drzewo, Indent) :-
    Drzewo = [Term],
    wypisz_indent(Indent),
    write(" -"),
    write(Term),
    write("\n"),!.
wypisz_drzewo(Drzewo, Indent) :-
    Drzewo = [Term, DzieciTermu],
    wypisz_indent(Indent),
    write("->"),
    write(Term),
    write("\n"),
    Indent__Plus__2 is Indent + 2,
    wypisz_dzieci(DzieciTermu, Indent__Plus__2),!.

walk_path(Drzewo, PathTaken, Daddies, TermFound) :-
    

proper_browse(Drzewo, PathTaken) :-
    walk_path(Drzewo, PathTaken, [], TermFound).
    write("command : "),
    get_char(Command),
    append(PathTaken, [Command], NewPathTaken),
    proper_browse(Drzewo, NewPathTaken).

browse(Term) :-
    make_tree(Term, Drzewo),
    wypisz_drzewo(Drzewo),
    proper_browse(Drzewo, []).
test :-
    Term = f1(f2(a2, a3), a1, f3(a4), f4(sandra, szwed, to, moja, kochana, dupera, kc(sana))),
    make_tree(Term, Drzewo),
    wypisz_drzewo(Drzewo, 0).

