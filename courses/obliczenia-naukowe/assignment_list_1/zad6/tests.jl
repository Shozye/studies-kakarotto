# Mateusz Pełechaty, indeks: 261737

function f(x)
    return sqrt(x^2 + 1) - 1
end

function g(x)
    return x^2 / (sqrt(x^2 + 1) + 1)
end

x = 1
println("\$x\$ & \$f(x)\$ & \$g(x)\$ \\\\ \\hline")
for i in 1:12
    global x
    x /= 8
    println("\$8^{-",i ,"}\$ & ", f(x)," & ", g(x), " \\\\ \\hline")
end