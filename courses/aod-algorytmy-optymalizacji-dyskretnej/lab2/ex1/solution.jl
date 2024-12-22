using JuMP
using GLPK

function main() 
    model = Model(GLPK.Optimizer)

    costs = [
        [10 7 8],
        [10 11 14],
        [9 12 4],
        [11 13 9]
    ]
    companies_upper_bounds = [
        275_000 
        550_000 
        660_000 
    ]

    airports_lower_bounds = [
        110_000 
        220_000
        330_000
        440_000
    ]

    amount_airports = length(costs)
    amount_companies = length(costs[1])

    @variable(model, x[1:amount_airports, 1:amount_companies] >= 0)
    @objective(model, Min, sum(x[i, j] * costs[i][j] for i in 1:amount_airports for j in 1:amount_companies))
    @constraint(model, [i in 1:amount_companies], sum(x[:, i]) <= companies_upper_bounds[i])
    @constraint(model, [i in 1:amount_airports], sum(x[i, :]) >= airports_lower_bounds[i])

    println(model)
    optimize!(model)
    if termination_status(model) != OPTIMAL
        @warn("The model was not solved correctly.")
        return
    end
    println(solution_summary(model))
    println("Minimal cost of deliveries: ")
    @show objective_value(model)


    per_company_deliveries = [
        sum(
            value(x[airport, i]) 
            for airport in 1:amount_airports
        ) 
        for i=1:amount_companies
    ]
    println(per_company_deliveries)


    println("Is every company delivering fuel?")
    println(all(per_company_deliveries .> 0))

    println("Are possibilities of delivering fuel exploited?")
    println(per_company_deliveries .== companies_upper_bounds)

end

main()