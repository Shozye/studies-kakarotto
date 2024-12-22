# Mateusz Pełechaty, indeks: 261737

"""
:param type: IS a type of max to calculate
"""
function getMax(type)
    max = type(4)
    prev_prev_max = type(1)
    prev_max = type(2)
    while (prev_max < max)
        prev_prev_max = prev_max
        prev_max = max
        max *= 2
    end
    return prev_prev_max
end

floats = [Float16, Float32, Float64]

for float in floats
    println(float)
    println(getMax(float))
    println(floatmax(float))
end
