# Mateusz Pełechaty, 261737
using Printf
include("roots.jl")

f(x) = exp(1-x) - 1
df(x) = -exp(1-x)

g(x) = x*exp(-x)
dg(x) = -exp(-x)*(x-1)
accuracy = 10^(-5)
maxit = 10000

tests = (
    (Roots.bisection, (f, Float64(0), Float64(2), accuracy, accuracy)),
    (Roots.newton, (f, df, Float64(0.9), accuracy, accuracy, maxit)),
    (Roots.newton, (f, df, Float64(100), accuracy, accuracy, maxit)),
    (Roots.secant, (f, Float64(0.9), Float64(1.1), accuracy, accuracy, maxit)),

    (Roots.bisection, (g, Float64(-1), Float64(1), accuracy, accuracy)),
    (Roots.newton, (g, dg, Float64(0.5), accuracy, accuracy, maxit)),
    (Roots.newton, (g, dg, Float64(1.1), accuracy, accuracy, maxit)),
    (Roots.newton, (g, dg, Float64(1), accuracy, accuracy, maxit)),
    (Roots.secant, (g, Float64(0.1), Float64(0.2), accuracy, accuracy, maxit))
)  

results = []

open("results/data_bisect_6.csv", "w") do iob
    write(iob, @sprintf("%s,%s,%s,%s,%s,%s,%s,%s\n", "function", "start_range", "end_range", "delta/epsilon", "found root", "f(root)", "iterations", "error"))
    open("results/data_newton_6.csv", "w") do ion
        write(ion, @sprintf("%s,%s,%s,%s,%s,%s,%s\n", "function", "x_0", "delta/epsilon", "found root", "f(root)", "iterations", "error"))
        open("results/data_secant_6.csv", "w") do ios
            write(ios, @sprintf("%s,%s,%s,%s,%s,%s,%s,%s\n", "function", "x_0", "x_1", "delta/epsilon", "found root", "f(root)", "iterations", "error"))
            for (method, args) in tests
                output = method(args...)
                push!(results, output)
                if method == Roots.bisection 
                    write(iob, @sprintf("%s,%s,%s,%s,%s,%s,%s,%s\n", String(Symbol(args[1])), args[2], args[3], args[4], output...))
                elseif method == Roots.newton
                    write(ion, @sprintf("%s,%s,%s,%s,%s,%s,%s\n", String(Symbol(args[1])), args[3], args[4], output...))
                elseif method == Roots.secant
                    write(ios, @sprintf("%s,%s,%s,%s,%s,%s,%s,%s\n", String(Symbol(args[1])), args[2], args[3], args[4], output...))
                end
            end
        end
    end
end
