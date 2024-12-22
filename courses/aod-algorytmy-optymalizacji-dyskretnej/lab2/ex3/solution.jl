using JuMP
using GLPK

function main() 
    model = Model(GLPK.Optimizer)

    l = [
        [2,4,3],
        [3,6,5],
        [5,7,6]
    ]
    u = [
        [3,7,5],
        [5,7,10],
        [8,12,10]
    ]
    shift_l = [10,20,18]
    district_l = [10,14,13]

    println("Solving")
    solve(l, u, shift_l, district_l)
end

function solve(l, u, shift_l, district_l)
    model = Model(GLPK.Optimizer)
    amount_shifts = length(shift_l)
    amount_districts = length(district_l)

    @variable(
        model, 
        u[district][shift] >= x[district=1:amount_districts, shift=1:amount_shifts] >= l[district][shift]
        )

    @variable(model, car_amount)
    
    @constraint(model, [district in 1:amount_districts], sum(x[district, :]) >= district_l[district])
    @constraint(model, [shift    in 1:amount_shifts   ], sum(x[:, shift   ]) >= shift_l[shift      ])

    @constraint(model, [shift    in 1:amount_shifts   ], sum(x[:, shift   ]) <= car_amount          ) 
    @objective(model, Min, car_amount)

    println(model)
    optimize!(model)
    println(solution_summary(model))

    println("Solution for given data")
    @show value.(x)
    
end

main()