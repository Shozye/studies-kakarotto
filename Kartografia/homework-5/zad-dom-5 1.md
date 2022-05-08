# Zadanie Domowe 5.

1. Wygeneruj\* po 1000 par liczb pierwszych `p` i `q` długości 128, 256, 512, 1024, 1536, 2048, 3072, 4096-bitów
   takich, aby wartości `p-1` i `q-1` były względnie pierwsze z 65537 (`2^(16)+1` względnie pierwsze z `φ(N)` dla `N = pq`).
2. Dla każdej z par oblicz
    * `N = pq`
    * `d = e^(-1) mod φ(N)` (gdzie `e = 65537`)
    * `dp = d mod (p-1)`
    * `dq = d mod (q-1)`
    * `qi = q^(-1) mod p`
  
    (klucz prywatny RSA).

3. Przygotuj implementacje funkcji RSA z i bez wykorzystania CRT, możesz wykorzystać rozwiązanie z 1. zadania domowego.
4. Dla obu implementacji zmierz średni czas działania funkcji odwrotnej (tj. z wykorzystaniem `d` jako wykładnika, czyli jak w deszyfrowaniu) dla każdej z długości
   podanej w podpunkcie 1 (średnią policz po parametrach z podpunktów 1. i 2.). Wejście do funkcji powinno być losową wartością z przedziału `{2, ..., N-1}`. Wyniki przedstaw za pomocą tabelki lub wykresu.

W rozwiązaniu nie trzeba zamieszczać wygenerowanych liczb pierwszych oraz wartości obliczonych w podpunkcie 2, wystarczą same średnie czasy działania + kod.

**\* Generacja liczb pierwszych długości 3072 i 4096 bitów może zająć dużo czasu. Jeśli jest za wolna, możesz skorzystać z załączonych plików, które zawierają po 8000 liczb pierwszych danej długości (wybierz liczby losowo).**