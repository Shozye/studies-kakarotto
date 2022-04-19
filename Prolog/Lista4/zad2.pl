obok(X, Y, List) :- po_prawej(X, Y, List).
obok(X, Y, List) :- po_prawej(Y, X, List).
po_prawej(L, R, [L, R | _]).
po_prawej(L, R, [_ | Rest]) :- po_prawej(L, R, Rest).
% NAROD, KOLOR, ZWIERZE, PALI, PIJE
rybki(Kto) :-
    Osiedle = [Dom1, _, Dom3, _, _],
    Dom1 = [norweg, _, _, _, _], % hint 1
    member([anglik, czerwony, _, _, _], Osiedle), % hint2
    po_prawej([_, zielony, _,_,_], [_, biały, _, _, _], Osiedle), % hint3
    member([dunczyk, _, _, _, herbatka], Osiedle), %hint4
    obok([_, _, _, papierosy_light, _], [_, _, koty, _, _], Osiedle), %hint5
    member([_, żółty, _, cygaro, _], Osiedle), % hint6
    member([niemiec, _, _, fajka, _], Osiedle), %hint7
    Dom3 = [_, _, _, _, mleko], %hint8
    obok([_, _, _, papierosy_light, _], [_, _, _, _, woda], Osiedle), %hint9
    member([_, _, ptaki, papierosy_bez_filtra, _], Osiedle), %hint10
    member([szwed, _, psy, _, _], Osiedle), %hint11
    obok([norweg, _, _, _, _], [_, niebieski, _, _, _], Osiedle),
    obok([_, żółty, _, _, _], [_, _, konie, _, _], Osiedle), % hint13
    member([_, _, _, mentole, piwo], Osiedle),
    member([_, zielony, _, _, kawa], Osiedle),
    member([Kto, _, rybki, _, _], Osiedle).


rybki(Kto, Dom1, Dom2, Dom3, Dom4, Dom5) :-
    Osiedle = [Dom1, Dom2, Dom3, Dom4, Dom5],
    Dom1 = [norweg, _, _, _, _], % hint 1
    member([anglik, czerwony, _, _, _], Osiedle), % hint2
    po_prawej([_, zielony, _,_,_], [_, biały, _, _, _], Osiedle), % hint3
    member([dunczyk, _, _, _, herbatka], Osiedle), %hint4
    obok([_, _, _, papierosy_light, _], [_, _, koty, _, _], Osiedle), %hint5
    member([_, żółty, _, cygaro, _], Osiedle), % hint6
    member([niemiec, _, _, fajka, _], Osiedle), %hint7
    Dom3 = [_, _, _, _, mleko], %hint8
    obok([_, _, _, papierosy_light, _], [_, _, _, _, woda], Osiedle), %hint9
    member([_, _, ptaki, papierosy_bez_filtra, _], Osiedle), %hint10
    member([szwed, _, psy, _, _], Osiedle), %hint11
    obok([norweg, _, _, _, _], [_, niebieski, _, _, _], Osiedle),
    obok([_, żółty, _, _, _], [_, _, konie, _, _], Osiedle), % hint13
    member([_, _, _, mentole, piwo], Osiedle),
    member([_, zielony, _, _, kawa], Osiedle),
    member([Kto, _, rybki, _, _], Osiedle).