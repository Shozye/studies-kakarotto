# Mateusz Pełechaty, 261737

module Interpolation
export dividedDifference, valueNewton, general, drawInterpolation
using Plots

"""
Function calculating the divided differences needed to represent the
interpolating polynomial in the Newton form.
# Arguments
- 'x' - vector of length n containing nodes x_0, ..., x_n-1, where 
    x[i] = x_{i-1}
- 'f' - vector of length n containing values of the interpolated function at
    nodes, where f[i] = f(x_{i-1})
# Output
fx - vector of length n containing calculated difference quotients, where
    fx[i] = f[x_0, ..., x_{i-1}]
"""
function dividedDifference(x::Vector{Float64}, f::Vector{Float64})
    n = length(x)
    fx = [f[i] for i in 1:n]
    for j in 2:n
        for i in n:-1:j
            fx[i] = (fx[i] - fx[i-1])/(x[i]-x[i-j+1])
        end
    end
    return fx
end


"""
Function that calculates the value of the interpolating polynomial in the Newton form.
# Arguments
- 'x' - vector of length n containing nodes x_0, ..., x_n-1, where 
    x[i] = x_{i-1}
- 'fx' - vector of length n containing calculated difference quotients, where
    fx[i] = f[x_0, ..., x_{i-1}]
- 't' - point at which the value of the polynomial is to be calculated
# Output
- 'nt' - value of the polynomial in point t
"""
function valueNewton(x::Vector{Float64}, fx::Vector{Float64}, t::Float64)
    n = length(x)
    nt = fx[n]
    for i in (n-1):-1:1
        nt = fx[i] + (t - x[i])*nt
    end
    return nt
end


"""
Function that calculates the coefficients of the interpolating polynomial in the general form.
# Arguments
- 'x' - vector of length n containing nodes x_0, ..., x_n-1, where 
    x[i] = x_{i-1}
- 'fx' - vector of length n containing calculated difference quotients, where
    fx[i] = f[x_0, ..., x_{i-1}]
# Output
- 'a' - vector of length n containing calculated coefficients of the polynomial, where
    a[i] is the coefficient of x^{i-1}
"""
function general(x::Vector{Float64}, fx::Vector{Float64})
    n = length(x)
    coefficients = Array{Float64}(undef, n, n)
    coefficients[1,1] = 1
    for i in 2:n
        for j in 1:n
            coefficients[i,j] = 0
            if j != 1
                coefficients[i, j] += coefficients[i-1, j-1]
            end
            coefficients[i, j] -= coefficients[i-1, j]*x[i-1]
        end
    end
    a = zeros(n)
    for j in 1:n
        for i in 1:n
            a[j] += coefficients[i, j]*fx[i]
        end
    end
    return a
end

"""
Function draws the interpolating polynomial and the interpolated function
in the range [a, b] on n+1 equally spaced points.
# Arguments
- 'f' - function to be interpolated (given as an anonymous function)
- 'a' - left endpoint of the interval
- 'b' - right endpoint of the interval
- 'n' - degree of the interpolating polynomial
# Output
- 'p' - object containing the plot
"""
function drawInterpolation(f,a::Float64,b::Float64,n::Int)
    nodes = collect(LinRange(a, b, n+1))
    fnodes = [f(nodes[i]) for i in 1:(n+1)]
    coefficients = dividedDifference(nodes, fnodes)
    xs = LinRange(a, b, 100)
    fx = [f(x) for x in xs]
    px = [valueNewton(nodes, coefficients, x) for x in xs]
    
    p = plot(xs, fx, label="Function f(x)", linewidth=3, legend=:top)
    plot!(p, xs, px, label="Interpolated p(x)", linewidth=3, legend=:top)
    scatter!(nodes, fnodes, label="nodes", color=:red, markersize=4, legend=:top)
    return p
end 
end # module