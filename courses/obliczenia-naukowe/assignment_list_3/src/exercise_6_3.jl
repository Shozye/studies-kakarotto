# Mateusz Pełechaty 261737
include("roots.jl")
include("plot_helpers.jl")

g(x) = x*exp(-x)
dg(x) = -exp(-x)*(x-1)

function accuracy(coefficient, exponent)
    return Float64(coefficient) * 10^(Float64(-exponent))
end

function draw_point_with_accuracy(x, fx, delta, epsilon, label1, label2, p)
    println("___",x, "___",fx,"___")
    scatter!(p, [x], [fx], label=label1, color=:red, markersize=6)
    plot!(p, 
        [x-delta, x-delta, x+delta, x+delta, x-delta], 
        [fx-epsilon, fx+epsilon, fx+epsilon, fx-epsilon, fx-epsilon], 
        label=label2, 
        color=:violet, 
        linewidth=3
    )
    return p
end

function make_test(acc, p)
    output = Roots.newton(g, dg, Float64(1.1), acc, acc, 10000)
    println("Output1", output)
    return draw_point_with_accuracy(output[1], output[2], acc, acc, "", "", p)
end

xs = LinRange(13.6,21, 100)
ys = [g(x) for x in xs]
p = plot(xs, ys, label="g(x) = x*exp(-x)", color=:green, linewidth=:5)
scatter!(p, [15], [1.0e-7], color=:red, markersize=1, label="Found root")
plot!(p, [14, 14.00001], [1.0e-7, 1.0e-7], color=:violet, markersize=0.5, label="Accuracy for root")

for i in 5:7
    make_test(accuracy(1, i), p)
    make_test(accuracy(1/2, i), p)
end


savefig("results/ex6_3.png")

