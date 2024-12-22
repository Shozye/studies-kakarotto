# Mateusz Pełechaty, 261737

struct OutputData
    r
    fr
    it
    err
end
OutputData(0, 0, Nothing, 0)

struct BTestData
    input::Tuple{Any, Float64, Float64, Float64, Float64}
    output::OutputData
end

struct NTestData
    input::Tuple{Any, Any, Float64, Float64, Float64, Int}
    output::OutputData
end

struct STestData
    input::Tuple{Any, Float64, Float64, Float64, Float64, Int}
    output::OutputData
end


linear1(x) = x
linear2(x) = 3x + 1
linear3(x) = 7x - 3

dlinear1(x) = 1
dlinear2(x) = 3
dlinear3(x) = 7

quadratic1(x) = x^2+2x+1
quadratic2(x) = x^2-x-1

dquadratic1(x) = 2x + 2
dquadratic2(x) = 2x - 1

factorized1(x) = (x-2.1113)*(x-10)*(x+1)*(x)

acc_XS = 1/2 * 10^(-15)
acc_S = 1/2 * 10^(-12)
acc_M = 1/2 * 10^(-9)
acc_L = 1/2 * 10^(-5)
Φ = 1.618033988749895

max_it_L = 1000
bisection_data = Base.Set()
newton_data = Base.Set()
secant_data = Base.Set()
push!(bisection_data, 
BTestData(
        (linear1, -10, 10, acc_XS, acc_XS),
        OutputData(0, 0, Nothing, 0)
    )
)
push!(bisection_data, 
BTestData(
        (linear1, -10, 10, acc_XS, acc_XS),
        OutputData(0, 0, Nothing, 0)
    )
)

push!(bisection_data, 
BTestData(
        (linear2, -1, 0, acc_XS, acc_XS),
        OutputData(-1/3, 0, Nothing, 0)
    )
)

push!(bisection_data, 
BTestData(
        (linear3, 0, 1, acc_XS, acc_XS),
        OutputData(3/7, 0, Nothing, 0)
    )
)

push!(bisection_data, 
BTestData(
        (linear2, 10, 15, acc_XS, acc_XS),
        OutputData(Nothing, Nothing, Nothing, 1)
    )
)


push!(bisection_data, 
BTestData(
        (quadratic2, 0, 10, acc_XS, acc_XS),
        OutputData(Φ, 0, Nothing, 0)
    )
)

push!(bisection_data, 
BTestData(
        (factorized1, 1, 3, acc_XS, acc_XS),
        OutputData(2.1113, 0, Nothing, 0)
    )
)

## END OF BISECTION

push!(newton_data, 
NTestData(
        (linear1, dlinear1, 1, acc_XS, acc_XS, max_it_L),
        OutputData(0, 0, Nothing, Nothing)
    )
)

push!(newton_data, 
NTestData(
        (linear2, dlinear2, -1/2, acc_XS, acc_XS, max_it_L),
        OutputData(-1/3, 0, Nothing, Nothing)
    )
)

push!(newton_data, 
NTestData(
        (linear3, dlinear3, 1/2, acc_XS, acc_XS, max_it_L),
        OutputData(3/7, 0, Nothing, Nothing)
    )
)

push!(newton_data, 
NTestData(
        (quadratic1, dquadratic1, -2, acc_XS, acc_XS, max_it_L),
        OutputData(-1, 0, Nothing, 0)
    )
)

push!(newton_data, 
NTestData(
        (quadratic2, dquadratic2, 1.5, acc_XS, acc_XS, max_it_L),
        OutputData(Φ, 0, Nothing, 0)
    )
)

# START OF SECANT DATA

push!(secant_data, 
STestData(
        (linear1, 1, -1, acc_XS, acc_XS, max_it_L),
        OutputData(0, 0, Nothing, Nothing)
    )
)

push!(secant_data, 
STestData(
        (linear2, -1/2, 0, acc_XS, acc_XS, max_it_L),
        OutputData(-1/3, 0, Nothing, Nothing)
    )
)

push!(secant_data, 
STestData(
        (linear3, 1/2, 1, acc_XS, acc_XS, max_it_L),
        OutputData(3/7, 0, Nothing, Nothing)
    )
)


push!(secant_data, 
STestData(
        (quadratic1, -2, 0, acc_XS, acc_XS, max_it_L),
        OutputData(-1, 0, Nothing, Nothing)
    )
)

push!(secant_data, 
STestData(
        (quadratic2, 1.5, 2, acc_XS, acc_XS, max_it_L),
        OutputData(Φ, 0, Nothing, Nothing)
    )
)

