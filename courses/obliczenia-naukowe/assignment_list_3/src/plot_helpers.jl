# Mateusz Pełechaty, 261737
using Plots

function draw_point_with_accuracy(x, fx, delta, epsilon)
    return draw_point_with_accuracy(x, fx, delta, epsilon, "Root", "Accuracy")
end

function draw_point_with_accuracy(x, fx, delta, epsilon, label1, label2)
    print("___",x, "___",fx,"___")
    p = scatter([x], [fx], label=label1, color=:red, markersize=10)
    plot!(p, 
        [x-delta, x-delta, x+delta, x+delta, x-delta], 
        [fx-epsilon, fx+epsilon, fx+epsilon, fx-epsilon, fx-epsilon], 
        label=label2, 
        color=:violet, 
        linewidth=3
    )
    return p
end

function add_point(p, x, fx, label)
    plot!(p, [x], [fx], seriestype = :scatter, label=label, markersize=5)
    return p
end
