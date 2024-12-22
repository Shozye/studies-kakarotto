# Mateusz Pełechaty, 261737

module Roots
export bisection, newton, secant


"""
Function that finds root of given function by using bisection method
# Arguments
- `f`: Function that takes argument n::Integer
- `a`: start of range we want to get root of.
- `b`: end of range we want to get root of.
- `delta`: Accuracy of calculations for arguments. 
- `epsilon`: Accuracy of calculations for values.
# Output
Quadruple (r, v, it, err), where
- `r`: Approximation of a root found by bisection method
- `fr`: Contains f(r)
- `it`: Amount of iterations,
- `err`: Error signalisation:
        0 - No error,
        1 - Function doesn't change it's sign.
"""
function bisection(f, a::Float64, b::Float64, delta::Float64, epsilon::Float64)
    fa = f(a)
    fb = f(b)

    if sign(fa) == sign(fb)
        return Nothing, Nothing, Nothing, 1
    end

    diff = b - a
    it = 0
    while true
        it += 1
        diff /= 2
        r = a + diff
        fr = f(r)

        if abs(diff) < delta || abs(fr) < epsilon
            return r, fr, it, 0
        end
        if sign(fr) != sign(fa)
            b = r
            B = fr
        else
            a = r
            A = fr
        end
    end
end

"""
Function that finds root of given function by using Newton's method
# Arguments
- `f`: Function that takes argument n::Integer
- `pf`: Derivative of f
- `x0`: start approximation
- `delta`: Accuracy of calculations for arguments. 
- `epsilon`: Accuracy of calculations for values.
- `maxit`: Maximum possible amount of iterations
# Output
Quadruple (r, v, it, err), where
- `r`: Approximation of a root found by bisection method
- `v`: Contains f(r)
- `it`: Amount of iterations,
- `err`: Error signalisation:
        0 - No error,
        1 - Required accuracy wasn't reached in `maxit` iterations
        2 - Derivative is close to 0
"""
function newton(f, pf, x0::Float64, delta::Float64, epsilon::Float64, maxit::Int)
    fx = f(x0)
    if abs(fx) < epsilon
        return x0, v, 0, 0
    end

    for it in 1:maxit
        pfx = pf(x0)
        if abs(pfx) < epsilon
            return x0, fx, it, 2
        end

        x1 = x0 - fx/pfx
        fx = f(x1)
        if abs(x1 - x0) < delta || abs(fx) < epsilon
            return x1, fx, it, 0
        end
        x0 = x1
    end
    return x0, fx, maxit, 1
end

"""
Function that finds root of given function by using secant method
# Arguments
- `f`: Function that takes argument n::Integer
- `x0`, `x1`: Start approximation
- `delta`: Accuracy of calculations for arguments. 
- `epsilon`: Accuracy of calculations for values.
- `maxit`: Maximum possible amount of iterations
# Output
Quadruple (r, v, it, err), where
- `r`: Approximation of a root found by bisection method
- `v`: Contains f(r)
- `it`: Amount of iterations,
- `err`: Error signalisation:
        0 - No error,
        1 - Required accuracy wasn't reached in `maxit` iterations
"""
function secant(f, x0::Float64, x1::Float64, delta::Float64, epsilon::Float64, maxit::Int)
    fx0 = f(x0)
    fx1 = f(x1)
    for it in 1:maxit
        if abs(fx0) < abs(fx1)
            x0, x1 = x1, x0
            fx0, fx1 = fx1, fx0
        end
        s = (x1 - x0)/(fx1 - fx0)
        x0 = x1
        fx0 = fx1
        x1 = x1 - fx0 * s
        fx1 = f(x1)
        if abs(x1 - x0) < delta || abs(fx1) < epsilon
            return x1, fx1, it, 0
        end
    end
    return x1, fx1, maxit, 1
end

end # end 