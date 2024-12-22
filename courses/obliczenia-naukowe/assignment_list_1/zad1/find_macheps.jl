# Mateusz Pełechaty, indeks: 261737
"""
:param type: IS a type of macheps to calculate
"""
function find_macheps(type)
    macheps = type(1)
    macheps_last = macheps
    one = type(1)
    
    while type(one + macheps) > one && type(one + macheps) == one + macheps
        macheps_last = macheps
        macheps = macheps / type(2)
    end
    return macheps_last
end

floats = [Float16, Float32, Float64]
for float in floats
    println(float)
    println(bitstring(find_macheps(float)))
    println("Macheps: ", find_macheps(float), "\nEpsilon: ", eps(float))
end