# Mateusz Pełechaty, 261737
include("../src/interpolation.jl")
using .Interpolation

x = [1.0, 2.0, 3.0, 4.0]
f = [x^2 for x in x]
t = 10.0
output = valueNewton(x, dividedDifference(x, f), t)
println(output)

