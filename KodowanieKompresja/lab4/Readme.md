## Lista 4 
### Cel
Celem listy było napisanie programu liczący entropie dla plików formatu *.tga*  
W dodatku program miał znaleźć najlepsze kodowanie spośród kodowań predykcyjnych JPEG-LS pod względem Entropii
W tym celu wykonałem: 
1. Parser plików *.tga*
2. Koder kodowań predykcyjnych
3. Funkcje licząca entropie po wszystkich kolorach osobno jak i łącznie

### Działanie
Po skompilowaniu za pomocą 
```bash
g++ src/main.cpp src/Pixel.cpp -o programs/calc_entropy
```
a następnie
```bash 
./calc_entropy example1.tga
```
gdzie example1.tga to plik znajdujacy sie w pictures/,  
uzyskujemy nastepujacy output:
```bash
ID |  RED  | GREEN | BLUE  | ALL 
0  |  8.00 | 8.00  | 8.00  | 8.00
1  |  0.07 | 0.04  | 0.07  | 0.96
2  |  0.00 | 0.07  | 0.07  | 0.96
3  |  0.07 | 0.10  | 0.13  | 1.66
4  |  0.04 | 0.04  | 0.07  | 0.05
5  |  0.04 | 0.06  | 0.10  | 0.98
6  |  0.06 | 0.04  | 0.10  | 0.97
7  |  0.10 | 0.10  | 0.19  | 1.03
8  |  0.00 | 0.07  | 0.17  | 0.98
Best prediction for blue is 1 0.07
Best prediction for red is 2 0.00
Best prediction for green is 4 0.04
Best prediction for all is 4 0.05
```
Który mówi że plik bez kodowania (ID 0) ma entropie 8 dla kazdego rodzaju.  
Natomiast najlepsze kodowanie dla czerwonego mozna uzyskać stosując kodowanie predykcyjne 2.
