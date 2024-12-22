include("../src/roots.jl")

f(x) = x^2 - 2

accuracy = 1e-6
maxit = 1000

r, v, it, err = Roots.bisection(f, Float64(0), Float64(2), accuracy, accuracy)
println("Bisection: r = $r, v = $v, it = $it, err = $err")

r, v, it, err = Roots.newton(f, x -> 2x, Float64(1), accuracy, accuracy, maxit)
println("Newton: r = $r, v = $v, it = $it, err = $err")

r, v, it, err = Roots.secant(f, Float64(0), Float64(2), accuracy, accuracy, maxit)
println("Secant: r = $r, v = $v, it = $it, err = $err")