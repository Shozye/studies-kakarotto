using JuMP
using GLPK

function main() 
    model = Model(GLPK.Optimizer)

    containers = [
        (1, 1),
        (2, 5),
        (5, 5)
    ]
    n = 5
    m = 5
    k = 1
    

    println("Solving")
    solve(n, m, k, containers)
end

function solve(n, m, k, containers)
    model = Model(GLPK.Optimizer)

    @variable(model, x[1:n, 1:m], Bin)
    for container in containers
        row, col = container[1], container[2]
        
        @constraint(model, x[row, col] == 0)
        @constraint(
            model, 
            sum(
                sum(
                    [
                    x[min(row+i, n), col],
                    x[max(row-i, 1), col],
                    x[row, min(col+i, m)],
                    x[row, max(col-i, 1)]
                    ]
                )
                for i in 1:k
            ) >= 1
        )
    end

    @objective(model, Min, sum(x[:, :]))


    println(model)
    optimize!(model)
    println(solution_summary(model))

    println("Solution for given data")
    @show value.(x)
    
end

main()