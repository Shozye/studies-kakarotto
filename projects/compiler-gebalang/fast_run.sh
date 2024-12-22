echo "TEST: Procedury. Oczekiwano 46368 28657"
python run.py tests/test_data/test_gebala/example2.imp compiled.out -o output -v
echo "0 1" | ./vms/vm-original/maszyna-wirtualna-cln output/compiled.out
