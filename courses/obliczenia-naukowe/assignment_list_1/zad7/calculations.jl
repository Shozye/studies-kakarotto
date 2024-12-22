# Mateusz Pełechaty, indeks: 261737

function f(x)
    return sin(x) + cos(3x)
end

function derivative_f(x)
    return cos(x) - 3sin(3x)
end

function approx_derivative_f(x, h)
    return (f(x + h) - f(x)) / h
end

function abs_error(a, b)
    return abs(a-b)
end

function make_tests(max_n)
    println("f'(x) = ", derivative_f(1))
    println("\$n\$ & approximate derivative & error & 1+h \\\\ \\hline")
    for n in 0:max_n
        h = 2.0^(-n)
        derivative = derivative_f(1)
        approx = approx_derivative_f(1, h)
        err = abs_error(derivative, approx)
        println(n, " & ", approx, " & ", err, " & ", 1+h, " \\\\ \\hline")
    end
end

make_tests(54)

