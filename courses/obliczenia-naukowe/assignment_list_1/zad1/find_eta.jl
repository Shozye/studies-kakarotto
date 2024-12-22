# Mateusz Pełechaty, indeks: 261737

"""
:param type: IS a type of eta to calculate
"""
function find_eta(type)
    eta = type(1) / 2
    prev_eta = type(1)
    while(eta > 0)
        prev_eta = eta
        eta /= 2
    end
    return prev_eta
end

floats = [Float16, Float32, Float64]
for float in floats
    println(float)
    println("Eta:       ", find_eta(float), "\nnextFloat: ", nextfloat(float(0.0)), " bits: ", bitstring(find_eta(float)))
end