# Mateusz Pełechaty, 261737
include("../src/interpolation.jl")

using .Interpolation
using Plots

function plotInterpolations(f, a, b, ns, filename)
    plots = [drawInterpolation(f, a, b, n) for n in ns]
    p = plot(plots..., layout=(1, length(ns)), size=(1200, 400))
    savefig(filename)
end