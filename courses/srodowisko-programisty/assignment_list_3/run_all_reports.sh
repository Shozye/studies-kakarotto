for file in *.cast; 
do
    echo START $file, Mateusz Pelechaty, 261737
    asciinema play $file -i 0.02
    echo KONIEC $file
done