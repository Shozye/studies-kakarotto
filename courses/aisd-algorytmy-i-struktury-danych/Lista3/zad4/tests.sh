for n in 8 16 32
do
    # Dla 3 n sprawdzamy czy n wystepuje
    # wykonujemy na posortowanej rosnaco bo inaczej binary search nie ma sensu
    ../programs/gen_asc $n 0 0 | ../programs/binary_search $n
    # Zwracamy ilosc porownan i czas jaki sie wykonuje 
done