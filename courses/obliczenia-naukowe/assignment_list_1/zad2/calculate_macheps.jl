# Mateusz Pełechaty, indeks: 261737
function calculate(type)
    return type(3) * (type(4/3) - type(1)) - 1
end

floats = [Float16, Float32, Float64]
for float in floats
    macheps = calculate(float)

    println(float)
    println("Macheps by Kahan: ", macheps)
    println("Macheps real:     ", eps(float))
end

