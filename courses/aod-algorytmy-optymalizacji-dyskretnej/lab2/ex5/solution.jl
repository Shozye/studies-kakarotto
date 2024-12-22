using JuMP
using GLPK

function main() 
    model = Model(GLPK.Optimizer)

    income_product = [9,7,6,5]
    cost_product = [4,1,1, 1]
    time = 60
    cost_machine = [2,2,3]
    processing = [
        [5,10,6],
        [3,6,4],
        [4,5,3],
        [4,2,1]
    ]
    demand = [
        400, 100, 150, 500
    ]

    println("Solving")
    solve(processing, income_product, cost_product, cost_machine, demand, time)
end

function solve(A, Ip, Cp, Cm, d, T)
    model = Model(GLPK.Optimizer)

    N = length(Ip)
    M = length(Cm)
    MT = 60*T # Minute Time

    # x[i] - we have processed x[i] kg of Product i, demand is upper bound
    @variable(model, d[i] >= x[i=1:N] >= 0)

    # Every machine is free MT minutes so sum of machine use <= MT
    @constraint(model, [machine in 1:M], sum(x[i]*A[i][machine] for i in 1:N) <= MT)



    # Every product i can be sold with profit = Ip[i] - Cp[i] Profit = Income - Cost
    Pp = (Ip .- Cp)
    # TotalIncome is amount of sold * profit from selling
    TotalIncome = sum(x .* Pp)
    # machine X works for sum(x[i]*A[i][X] for i in 1:N)/60 hours
    TotalMachineCost = sum( 
        (
            sum(
                x[i]*A[i][machine] for i in 1:N
            )/60.0
        ) * Cm[machine] 
        for machine in 1:M
    )
    # TotalProfit is TotalIncome - TotalMachineCost
    @objective(model, Max, TotalIncome - TotalMachineCost)

    
    println(model)
    optimize!(model)
    println(solution_summary(model))

    println("Solution for given data")
    @show value.(x)
    
end

main()