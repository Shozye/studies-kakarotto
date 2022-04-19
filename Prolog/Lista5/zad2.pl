% Funkcja z listy 4 od dr. Kobylanskiego
hetmany(N, P) :-
    numlist(1, N, L),
    permutation(L, P),
    dobra(P).
dobra(P) :-
    \+ zla(P).
zla(P) :-
    append(_, [Wi | L1], P),
    append(L2, [Wj | _], L1),
    length(L2, K),
    abs(Wi - Wj) =:= K + 1.

is_queen_on_tile(QueenPlacements, RowNumber, ColNumber, BoardSize) :-
    nth0(ColNumber, QueenPlacements, QueenRowPlacement), 
    % now we need to change 1 to 11, 2 to 10, 3 to 9
    RowNumber is BoardSize - QueenRowPlacement,!.

get_tile_color(RowNumber, ColNumber, Color) :-
    Rest is mod((RowNumber + ColNumber), 2),
    (Rest = 1 -> Color = black; Color = white),!.

draw_tile_with_queen(white) :-
    write("| ### ").
draw_tile_with_queen(black) :-
    write("|:###:").
draw_tile_without_queen(white) :-
    write("|     ").
draw_tile_without_queen(black) :-
    write("|:::::").

draw_horizontal_border(0) :-
    write("+\n"),!.
draw_horizontal_border(N) :-
    write("+-----"),
    N__Minus__1 is N-1,
    draw_horizontal_border(N__Minus__1).

draw_tile_row(_, _, BoardSize, BoardSize) :-
    write("|\n"),!.
draw_tile_row(QueenPlacements, RowNumber, ColNumber, BoardSize) :-
    is_queen_on_tile(QueenPlacements, RowNumber, ColNumber, BoardSize),
    get_tile_color(RowNumber, ColNumber, Color),
    draw_tile_with_queen(Color),
    ColNumber__Plus__1 is ColNumber + 1,
    draw_tile_row(QueenPlacements, RowNumber, ColNumber__Plus__1, BoardSize),!.
draw_tile_row(QueenPlacements, RowNumber, ColNumber, BoardSize) :-
    \+ (is_queen_on_tile(QueenPlacements, RowNumber, ColNumber, BoardSize)),
    get_tile_color(RowNumber, ColNumber, Color),
    draw_tile_without_queen(Color),
    ColNumber__Plus__1 is ColNumber + 1,
    draw_tile_row(QueenPlacements, RowNumber, ColNumber__Plus__1, BoardSize),!.

draw_tiles(_, BoardSize, BoardSize) :-
    draw_horizontal_border(BoardSize),!.
draw_tiles(QueenPlacements, RowNumber, BoardSize) :-
    draw_horizontal_border(BoardSize),
    draw_tile_row(QueenPlacements, RowNumber, 0, BoardSize),
    draw_tile_row(QueenPlacements, RowNumber, 0, BoardSize),
    RowNumber__Plus__1 is RowNumber + 1,
    draw_tiles(QueenPlacements, RowNumber__Plus__1, BoardSize).

board(QueenPlacements) :-
    max_list(QueenPlacements, BoardSize),
    draw_tiles(QueenPlacements, 0, BoardSize).


test :-
    hetmany(5, QueenPlacements), 
    board(QueenPlacements).

