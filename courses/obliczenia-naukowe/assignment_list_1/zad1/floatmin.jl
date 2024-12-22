# Mateusz Pełechaty, indeks: 261737
floats = [Float16, Float32, Float64]
for float in floats
    println(float)
    println("floatmin: ", floatmin(float), " bity: ", bitstring(floatmin(float)))
end