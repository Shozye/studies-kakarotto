# Mateusz Pełechaty, 261737
include("../src/interpolation.jl")
using .Interpolation

x = [0, pi/4, pi/2, 3*pi/4]
f = [sin(x[i]) for i in 1:length(x)]
output = dividedDifference(x, f)
println(output)


x = [1.0, 2.0, 3.0, 4.0]
f = [x^2 for x in x]
output = dividedDifference(x, f)
println(output)
# Powinno wyjść [1.0, 3.0, 1.0, 0.0]
# x | fx| 1 | 2 | 3
# 1 | 1 |   |   |
#   |   | 3 |   |
# 2 | 4 |   | 1 |
#   |   | 5 |   | 0
# 3 | 9 |   | 1 |
#   |   | 7 |   |
# 4 | 16|   |   |