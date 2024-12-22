# Mateusz Pełechaty, 261737
using Printf

include("roots.jl")
include("plot_helpers.jl")

f(x) = sin(x) - (0.5x)^2
df(x) = cos(x) - x/2

maxit = 100000
accuracy = Float64(1/2 * 10^(-5))

tests = (
    (Roots.bisection, (f, Float64(1.5), Float64(2), accuracy, accuracy)),
    (Roots.newton, (f, df, Float64(1.5), accuracy, accuracy, maxit)),
    (Roots.secant, (f, Float64(1), Float64(2), accuracy, accuracy, maxit))
)

results = []

for (method, args) in tests
    push!(results, (String(Symbol(method)), method(args...)))
end

open("results/data_4.csv", "w") do io
    write(io, @sprintf("%s,%s,%s,%s,%s\n", "method", "root", "f(root)", "iterations", "error"))
    for (fname, result) in results
        write(io, fname)
        for output in result
            write(io, @sprintf(",%s", output))
        end
        write(io, "\n")
    end
end

function make_plot(accuracy, results)
    p = draw_point_with_accuracy(1.9337537628270212533, 0, accuracy, accuracy)
    for (fname, result) in results
        p = add_point(p, result[1], result[2], fname)
    end
    xs = LinRange(1.9337537628270212533 - accuracy*5/4, 1.9337537628270212533 + accuracy*5/4, 100)
    plot!(p, xs, [f(x) for x in xs], label="sin(x) - (0.5x)^2")
    savefig("results/ex4_plot.png")
end 

make_plot(accuracy, results)