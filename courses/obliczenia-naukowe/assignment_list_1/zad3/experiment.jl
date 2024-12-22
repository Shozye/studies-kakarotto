# Mateusz Pełechaty, indeks: 261737

random_float = rand() + 1
next = nextfloat(random_float)
println("Random number: ", random_float, " type:", typeof(random_float))
println("num      : ", random_float)
println("next(num): ", next)
println("num:       ", bitstring(random_float))
println("next(num): ", bitstring(next))