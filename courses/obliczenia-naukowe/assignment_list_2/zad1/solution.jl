# Mateusz Pełechaty, indeks: 261737

include("functions.jl")

function front(type)
    product = get_product(type)
    return sum(product, false, type) # dodawaj z lewej do prawej
end
function big_to_small(type)
    product = get_product(type)
    nonnegative = sort(product[product .>= 0], rev=true) # dodatnie z gory na dol
    negative = sort(product[product .< 0]) # ujemne z dolu w gore
    return sum(nonnegative, false, type) + sum(negative, false, type) # dodawaj z duzych do malych

end
function small_to_big(type)
    product = get_product(type)
    nonnegative = sort(product[product .>= 0], rev=true) # dodatnie z gory na dol
    negative = sort(product[product .< 0]) # ujemne z dolu w gore
    return sum(nonnegative, true, type) + sum(negative, true, type) # dodawaj z malych do duzych
    
end

function back(type)
    product = get_product(type)
    return sum(product, true, type) # dodawaj z prawej do lewej
end

for float in [Float32, Float64]
    println("Testing ", float)
    println("Front        ", front(float))
    println("Back         ", back(float))
    println("Big to small ", big_to_small(float))
    println("Small to big ", small_to_big(float))
    println("###==================================================###")
end