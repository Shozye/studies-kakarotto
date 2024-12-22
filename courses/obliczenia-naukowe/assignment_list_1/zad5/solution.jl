# Mateusz Pełechaty, indeks: 261737

include("functions.jl")

"""
Calculates front sum of product asked in exercise 
:param type: either float32 or float64
"""
function front(type)
    product = get_product(type)
    return sum(product, false, type) # dodawaj z lewej do prawej
end
"""
Calculates bigtosmall sum of product asked in exercise 
:param type: either float32 or float64
"""
function big_to_small(type)
    product = get_product(type)
    nonnegative = sort(product[product .>= 0], rev=true) # dodatnie z gory na dol
    negative = sort(product[product .< 0]) # ujemne z dolu w gore
    return sum(nonnegative, false, type) + sum(negative, false, type) # dodawaj z duzych do malych

end
"""
Calculates small to big sum of product asked in exercise 
:param type: either float32 or float64
"""
function small_to_big(type)
    product = get_product(type)
    nonnegative = sort(product[product .>= 0], rev=true) # dodatnie z gory na dol
    negative = sort(product[product .< 0]) # ujemne z dolu w gore
    return sum(nonnegative, true, type) + sum(negative, true, type) # dodawaj z malych do duzych
    
end

"""
Calculates back sum of product asked in exercise 
:param type: either float32 or float64
"""
function back(type)
    product = get_product(type)
    return sum(product, true, type) # dodawaj z prawej do lewej
end

real = 1.00657107000000 * 10^(-11)
for float in [Float32, Float64]
    println("Testing ", float)
    global real
    println("Real value:  ", real)
    println("Front        ", front(float), " Error: ", relative_error(real, front(float)), "%")
    println("Back         ", back(float), " Error: ", relative_error(real, back(float)), "%")
    println("Big to small ", big_to_small(float), " Error: ", relative_error(real, big_to_small(float)), "%")
    println("Small to big ", small_to_big(float), " Error: ", relative_error(real, small_to_big(float)), "%")
    println("###==================================================###")
end