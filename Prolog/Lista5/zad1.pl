% Splits String to list of chars and 
% checks for every char if it is specified type
string_type(String, Type) :-
    string_chars(String, Chars),
    \+ (member(Char, Chars), \+(char_type(Char, Type))).

space(X) :- string_type(X, space). % it is \n \t and ' '
sep_part(X) :- string_type(X, punct), string_type(X, graph). % letters of separator
upper(X) :- string_type(X, upper).
lower(X) :- string_type(X, lower).
int(X) :- string_type(X, digit).

% True if type(S1) == type(S2)
same_type(S1, S2) :-
    ((space(S1), space(S2))
    ;(sep_part(S1), sep_part(S2))
    ;(upper(S1), upper(S2))
    ;(lower(S1), lower(S2))
    ;(int(S1), int(S2))),!.


% Function to read file to stream of characters. 
% Read characters till end of file is added to list. 
% If it is added, then get all other letters and 
% reverse order to get proper order.
% WORKS GOOD
readfile(_, [end_of_file|Tail], Output) :- 
    reverse(Tail, Output).
readfile(InputFile, ListOfCharacters, Output) :- 
    get_char(InputFile, Character),
    readfile(InputFile, [Character | ListOfCharacters], Output).

% if file is empty then splitted types is also empty
join([], []) :- !.
% if file is nonempty then take first character and start the parsing with it.
join([FirstCharacter | Rest], ListOfSplittedWords) :-
    parse(Rest, [FirstCharacter], ListOfSplittedWords),!.

% As we are adding to the List of splitted types on the beginning, 
% we have to reverse it
parse([], ListOfSplittedWordsReversed, ListOfSplittedWords) :-
    reverse(ListOfSplittedWordsReversed, ListOfSplittedWords).

% Get next character and join it with previous type or not.
% If join then add to RestSplitted. If not then add it as another term
parse([NextCharacter | Rest], [LastSplittedType | RestSplitted], ListOfSplittedWords) :-
    same_type(NextCharacter, LastSplittedType),
    string_concat(LastSplittedType, NextCharacter, Concatenated),
    parse(Rest, [Concatenated | RestSplitted], ListOfSplittedWords).

parse([NextCharacter | Rest], [LastSplittedType | RestSplitted], ListOfSplittedWords) :-
    \+ (same_type(NextCharacter, LastSplittedType)),
    parse(Rest, [NextCharacter, LastSplittedType | RestSplitted], ListOfSplittedWords).

% Add types depending to what function it reacts to
% upper -> id
% lower -> key
% int -> int
% sep_part -> sep
% space -> space
addTypes([], ListOfSplittedTypesTillNow, ListOfSplittedTypes) :-
    reverse(ListOfSplittedTypesTillNow, ListOfSplittedTypes).
addTypes([Word | RestWords], ListOfSplittedTypesTillNow, ListOfSplittedTypes) :-
    upper(Word),
    Term =.. [id, Word],
    NewListOfSplittedTypesTillNow = [Term | ListOfSplittedTypesTillNow],
    addTypes(RestWords, NewListOfSplittedTypesTillNow, ListOfSplittedTypes).

addTypes([Word | RestWords], ListOfSplittedTypesTillNow, ListOfSplittedTypes) :-
    lower(Word),
    Term =.. [key, Word],
    NewListOfSplittedTypesTillNow = [Term | ListOfSplittedTypesTillNow],
    addTypes(RestWords, NewListOfSplittedTypesTillNow, ListOfSplittedTypes).

addTypes([Word | RestWords], ListOfSplittedTypesTillNow, ListOfSplittedTypes) :-
    int(Word),
    Term =.. [int, Word],
    NewListOfSplittedTypesTillNow = [Term | ListOfSplittedTypesTillNow],
    addTypes(RestWords, NewListOfSplittedTypesTillNow, ListOfSplittedTypes).

addTypes([Word | RestWords], ListOfSplittedTypesTillNow, ListOfSplittedTypes) :-
    sep_part(Word),
    Term =.. [sep, Word],
    NewListOfSplittedTypesTillNow = [Term | ListOfSplittedTypesTillNow],
    addTypes(RestWords, NewListOfSplittedTypesTillNow, ListOfSplittedTypes).

addTypes([Word | RestWords], ListOfSplittedTypesTillNow, ListOfSplittedTypes) :-
    space(Word),
    Term =.. [space, Word],
    NewListOfSplittedTypesTillNow = [Term | ListOfSplittedTypesTillNow],
    addTypes(RestWords, NewListOfSplittedTypesTillNow, ListOfSplittedTypes).

% Get type from list one by one and add to the output list if it isn't space
deleteSpaces([], ListOfSplittedTypesWithoutSpacesReversed, ListOfSplittedTypesWithoutSpaces) :-
    reverse(ListOfSplittedTypesWithoutSpacesReversed, ListOfSplittedTypesWithoutSpaces).

deleteSpaces([Type | Rest], ListOfSplittedTypesWithoutSpacesReversed, ListOfSplittedTypesWithoutSpaces) :-
    Type =.. [space | _],
    deleteSpaces(Rest, ListOfSplittedTypesWithoutSpacesReversed, ListOfSplittedTypesWithoutSpaces).

deleteSpaces([Type | Rest], ListOfSplittedTypesWithoutSpacesReversed, ListOfSplittedTypesWithoutSpaces) :-
    \+(Type =.. [space | _]),
    deleteSpaces(Rest, [Type | ListOfSplittedTypesWithoutSpacesReversed], ListOfSplittedTypesWithoutSpaces).
    
scanner(InputFile, ListOfSplittedTypesWithoutSpaces) :- 
    % read file to List Of Characters
    readfile(InputFile, [], ListOfCharacters),
    % then join list of characters to make separated types
    % keys, ints, ids, and separators are differentiated.
    join(ListOfCharacters, ListOfSplittedWords),
    % Then add types to List of splitted words
    addTypes(ListOfSplittedWords, [], ListOfSplittedTypes),
    % Then delete spaces
    deleteSpaces(ListOfSplittedTypes, [], ListOfSplittedTypesWithoutSpaces).

% Running function
scan(Filename) :-
    open(Filename, read, File), 
    scanner(File, ScannedData),
    close(File), 
    write(ScannedData),!.
