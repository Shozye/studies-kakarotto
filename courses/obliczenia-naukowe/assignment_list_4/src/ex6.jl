# Mateusz Pełechaty, 261737
include("utils.jl")

function test1()
    f = x -> abs(x)
    a = -1.0
    b = 1.0
    ns = [5,10,15]
    filename = "results/ex6_plot1.png"
    plotInterpolations(f, a, b, ns, filename)
end

function test2()
    f = x -> 1/(1+x^2)
    a = -5.0
    b = 5.0
    ns = [5,10,15]
    filename = "results/ex6_plot2.png"
    plotInterpolations(f, a, b, ns, filename)
end

function main()
    test1()
    test2()
end

main()