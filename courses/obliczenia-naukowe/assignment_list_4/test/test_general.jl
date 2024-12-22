# Mateusz Pełechaty, 261737
include("../src/interpolation.jl")
using .Interpolation

x = [1.0, 2.0, 3.0, 4.0]
f = [x^2 for x in x]
output = general(x, dividedDifference(x, f))
println(output)
