### Drzewo BST
#### Kod
Kod można zobaczyć w plikach BST.h oraz BST.cpp
Zaimplementowane sa nastepujace funkcje
- insert
- height
- delete  
- print  
Znajduje się tam główna klasa drzewa.  
Drzewo mozemy przetestowac za pomocą programu BST_test
### Przykladowe dzialanie
```bash
./rand_gen n (distinct|whatever) 
```  
generuje n losowych liczb distinct lub nie i wyrzuca na standardowe wyjscie  
```bash
./BST_test (RANDOM|ASCENDING) (PRINT|WHATEVER)  
```
inserts numbers in RANDOM/ASCENDING mode, then deletes them in RANDOM order and prints every step if PRINT.   
Also outputs amount of comparisons and amount of displacements in tree  

Po wpisaniu
```bash
./rand_gen 5 distinct | ./BST_test RANDOM PRINT
```
output
```bash
========== INSERTING ======== 
-[0]
HEIGHT: 1

-[0]
 \-[4]
HEIGHT: 2

-[0]
 \-[4]
  \-[6]
HEIGHT: 3

-[0]
 \-[4]
  \-[6]
   \-[8]
HEIGHT: 4

-[0]
| /-[2]
 \-[4]
  \-[6]
   \-[8]
HEIGHT: 4

======= REMOVING ======
 /-[2]
-[4]
 \-[6]
  \-[8]
HEIGHT: 3

 /-[2]
-[6]
 \-[8]
HEIGHT: 2

 /-[2]
-[8]
HEIGHT: 2

-[2]
HEIGHT: 1

HEIGHT: 0

23 40 
```