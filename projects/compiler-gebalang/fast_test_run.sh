
echo "TEST: Rozklad na czynniki pierwsze. Oczekiwano: 3 1 4115226301 1"
python run.py tests/test_data/test_gebala/program2.imp compiled.out -o output -v
echo 12345678903 | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out

echo "TEST: Kombinacje. Oczekiwano 167960"
python run.py tests/test_data/test_gebala/example4.imp compiled.out -o output -v
echo "20 9" | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out

echo "TEST: Fibbonaci 26. Oczekiwano 121393"
python run.py tests/test_data/test_gebala/example3.imp compiled.out -o output -v
echo 1 | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out

echo "TEST: GCD 4 liczb. Oczekiwano 523"
python run.py tests/test_data/test_gebala/program1.imp compiled.out -o output -v
echo "3814532926 1065023079 3875997978 1438730637" | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out

echo "TEST: Krzywa Eliptyczna. Oczekiwano 43 21"
python run.py tests/test_data/test_slowik/test4b.imp compiled.out -o output -v
echo "71 70 5 7 32 17" | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out

echo "TEST: Procedury. Oczekiwano 46368 28657"
python run.py tests/test_data/test_gebala/example2.imp compiled.out -o output -v
echo "0 1" | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out

echo "TEST: Modulo. Oczekiwano 674106858"
python run.py tests/test_data/test_gebala/example5.imp compiled.out -o output -v
echo "1234567890 1234567890987654321 987654321" | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out
