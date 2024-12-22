# Mateusz Pełechaty, indeks: 261737
using Printf
using Plots

function x_next(x_n, c)
    return x_n^2 + c
end        

function generate_graphic_iteration(x_0, c, n)
    xs = [Float64(x_0)]
    ys = [Float64(0)]
    x = x_0
    y = 0
    for i in 1:n
        y = x_next(x, c)
        push!(xs, x)
        push!(ys, y)

        x = y
        push!(xs, x)
        push!(ys, y)
    end
    return [xs, ys]
end

function generate_quadratic_formula(c)
    xs = LinRange(-2,2,100)
    ys = [x_next(x, c) for x in xs]
    return [xs, ys]
end

function generate_line()
    xs = LinRange(-2,2,100)
    ys = copy(xs)
    return [xs, ys]
end

function generate_plot(c, x_0, n)
    quadratic = generate_quadratic_formula(c)
    line = generate_line()
    goal = generate_graphic_iteration(x_0, c, n)
    

    p = plot(line[1], line[2], color=:violet, linewidth=2.5, label="y=x", legend=:top)
    plot!(p, quadratic[1], quadratic[2], color=:purple, linewidth=2.5, label=@sprintf("y=x²+%s", c))
    plot!(p, goal[1], goal[2], color=:green, linewidth=2, label="Graphic Iteration")
    plot!(p, [goal[1][1], goal[1][1] + 0.000000001], [goal[2][1], goal[2][1] + 0.000000001], color=:darkgreen, markersize=20, linewidth=10, label="(x_0, 0)")
    plot!(p, [goal[1][length(goal[1])], goal[1][length(goal[1])] + 0.000000001], [goal[2][length(goal[2])], goal[2][length(goal[2])] + 0.000000001], color=:lime, markersize=20, linewidth=10, label="(x_40, x_40)")
end

input_data = [  
                [-2,1], 
                [-2,2],
                [-2,1.99999999999999],
                [-1,1],
                [-1,-1],
                [-1,0.75],
                [-1,0.25]
             ]

for (c, x_0) in input_data
    generate_plot(c, x_0, 40)
    savefig(@sprintf("c=%s_x0=%s.png", c, x_0))
end