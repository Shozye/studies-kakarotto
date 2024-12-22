using JuMP
using GLPK

function main() 
    model = Model(GLPK.Optimizer)

    N = 1:10

    edges = [
        [(1,2), 1, 1],
        [(2,3),  1, 1],
        [(3,4),  1, 1],
        [(4,5),  1, 1],
        [(5,6),  1, 1],
        [(6,7),  1, 1],
        [(7,8),  1, 1],
        [(8,9),  1, 1],
        [(9,10), 1, 1],
        [(10,1), 1, 1],
        [(1, 6), 5, 2],
        [(3, 9), 5, 2],
        [(4, 10), 6, 3],
    ]
    A = [edges[x][1] for x in 1:length(edges)]
    c = Dict(edges[x][1] => edges[x][2] for x in 1:length(edges))
    t = Dict(edges[x][1] => edges[x][3] for x in 1:length(edges))
    T = 8
    start=2
    goal = 10

    println("Solving")
    println(A)
    println(c)
    println(t)
    solve(N, A, c, t, T, start, goal)
end

function solve(N, A, c, t, T, start, goal)
    model = Model(GLPK.Optimizer)
    @variable(model, 1 >= x[ij in A] >= 0)

    function out(i)
        return sum(x[i_j] for i_j in A if i_j[1] == i)
    end
    function in(i)
        return sum(x[j_i] for j_i in A if j_i[2] == i)
    end
    function d(i)
        return in(i) - out(i)
    end

    for i in N
        if(i == start)
            @constraint(model, d(i) == -1)
        elseif (i == goal)
            @constraint(model, d(i) == 1)
        else
            @constraint(model, d(i) == 0)
        end
    end
    @constraint(model, sum([x[ij] * t[ij] for ij in A]) <= T)
    @objective(model, Min, sum([x[ij] * c[ij] for ij in A]))

    println(model)

    optimize!(model)
    println(solution_summary(model))

    println("Solution for given data")
    @show value.(x)
    println("Integer Linear Programming is not needed at all")



end

main()