# Mateusz Pełechaty, indeks: 261737

"""
Calculate and return multiplication of num and it's reciprocal
"""
function calculate(num)
    return Float64(num*Float64(1/num))
end

function find()
    start = Float64(1.0)
    while true
        if calculate(start) != 1
            return start
        end
        amount += 1
        start = nextfloat(start)
    end
end
found = find()
println("Found: ", found, ", bitstring: ", bitstring(found))