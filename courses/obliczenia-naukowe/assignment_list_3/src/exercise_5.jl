# Mateusz Pełechaty, 261737
using Printf

include("roots.jl")
include("plot_helpers.jl")

f(x) = exp(x) - 3x

maxit = 100000
accuracy = Float64(10^(-4))

tests = (
    (Roots.bisection, (f, Float64(0), Float64(1), accuracy, accuracy)),
    (Roots.bisection, (f, Float64(1), Float64(2), accuracy, accuracy)),
)

results = []

open("results/data_5.csv", "w") do io
    write(io, @sprintf("%s,%s,%s,%s,%s,%s\n", "start_range", "end_range", "found root", "f(root)", "iterations", "error"))
    for (method, args) in tests
        output = method(args...)
        push!(results, output)

        write(io, @sprintf("%s,%s,%s,%s,%s,%s\n", args[2], args[3], output...))
    end
end

function draw_point_with_accuracy(p, x, fx, delta, epsilon)
    scatter!(p, [x], [fx], label="Real Root", color=:red, markersize=10)
    plot!(p, 
        [x-delta, x-delta, x+delta, x+delta, x-delta], 
        [fx-epsilon, fx+epsilon, fx+epsilon, fx-epsilon, fx-epsilon], 
        label="Accuracy", 
        color=:violet, 
        linewidth=3
    )
    return p
end

root1= 0.6190612867359451121523269940209222333014717772629693524598360744929373522550887346110469261882588406588475092970521772616391443
root2= 1.5121345516578424738967396780720387046036503851353594542592854739989771605115748273242654881527798352683957198107193203478259518

xs = LinRange(0.6189, 0.6192, 100)
ys = [f(x) for x in xs]
p = plot(xs, ys, label="e^x - 3x")
draw_point_with_accuracy(p, root1, 0, accuracy, accuracy)
scatter!(p, [results[1][1]], [results[1][2]], color=:green, markersize=7, label="Found root")
savefig("results/ex5_plot_1.png")

xs = LinRange(1.512, 1.51228, 100)
ys = [f(x) for x in xs]
p = plot(xs, ys, label="e^x - 3x")
draw_point_with_accuracy(p, root2, 0, accuracy, accuracy)
scatter!(p, [results[2][1]], [results[2][2]], color=:green, markersize=7, label="Found root")
savefig("results/ex5_plot_2.png")