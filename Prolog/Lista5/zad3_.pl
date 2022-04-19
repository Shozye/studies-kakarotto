in(i).
out(o).
next(n).
prev(p).

browse(Drzewo):-
    browse(Drzewo,[],[]).

% Korzen to Term glowny. 
% Lewo to Tablica z termami z lewej strony,
% Prawo to Tablica z termami z prawej strony
browse(Korzen,Lewo,Prawo):-
    writeln(Korzen),
    write('command: '),
    get_char(Polecenie),
    % jeżeli Polecenie to IN i Korzen ma Argument Korzen1 To Wyszukuj w nim
    % Wszystkie nastepne sa w Lewo1. Po prawej nic nie, bo bierzemy pierwszy z brzegu.
    % Jeżeli to nie jest polecenie IN to idz dalej.
    (   in(Polecenie) ->( Korzen =.. [_,Korzen1 | Lewo1] ->
                            (   browse(Korzen1,Lewo1, [])) 
                            ; true ) 
                        ; true
    ),
    % Jeżeli Polecenie Next to idziemy w lewo. 
    % Czyli rozdzielamy to co po Lewej na to co po lewej i reszte.
    % Natomiast Korzen doklejamy do prawej strony na poczatek.
    % I przeszukujemy Drzewo z korzeniem H2
    (   next(Polecenie) ->
           (Lewo = [H2|R2] ->
                        (   I2 is 1,
                            append([Korzen],Prawo,Prawo2),
                            browse(H2, R2, Prawo2)
                        ) ; I2 is 0
           ) ; I2 is 0
    ),
    % Jezeli polecenie prev to idziemy w prawo i w zasadzie to robimy to samo co z next.
    (   prev(Polecenie) ->
           (Prawo = [H3|R3] ->
                        (   I3 is 1,
                            append([Korzen], Lewo, Lewo3),
                            browse(H3, Lewo3, R3)
                        ) ;   I3 is 0
           ) ; I3 is I2
    ),
    % Jezeli polecenie out lub wlasnie wyszlismy z polecenia next/prev
    % to wtedy zwroc true, czyli sie cofnij do tylu.
    % A jezeli nie czyli polecenie inne niz out i I3 = 0 to wtedy przeszukujemy 
    % Korzen w prawa strone
    (   (out(Polecenie); I3 = 1)-> true; browse(Korzen,Lewo,Prawo)).