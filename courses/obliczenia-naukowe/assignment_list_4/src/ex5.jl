# Mateusz Pełechaty, 261737
include("utils.jl")

function test1()
    f = x -> exp(x)
    a = 0.0
    b = 1.0
    ns = [5,10,15]
    filename = "results/ex5_plot1.png"
    plotInterpolations(f, a, b, ns, filename)
end

function test2()
    f = x -> x^2 * sin(x)
    a = -1.0
    b = 1.0
    ns = [5,10,15]
    filename = "results/ex5_plot2.png"
    plotInterpolations(f, a, b, ns, filename)
end

function main()
    test1()
    test2()
end

main()