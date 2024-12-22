# Mateusz Pełechaty, 261737
include("../src/interpolation.jl")
using .Interpolation

using Plots
p = drawInterpolation(sin, -1.0, 1.0, 6)
savefig("results/test_plot1.png")

function f(x)
    return abs(abs(abs(x)-1)-1)
end
p = drawInterpolation(f, -2.0, 2.0, 10)
savefig("results/test_plot2.png")
