# Mateusz Pełechaty, indeks: 261737

x = [2.718281828,-3.141592654,1.414213562,0.5772156649,0.3010299957]
y = [1486.2497,878366.9879,-22.37492,4773714.647,0.000185049]

function get_product(type)
    product = Array{type}(undef, 5) 
    for i in 1:length(x)
        product[i] = type(x[i]) * type(y[i])
    end
    return product
end

function relative_error(expected, actual)
    return round((100*abs(actual - expected) / expected); digits=2)
end


function sum(array, reverse, type)
    S::type = 0
    rng = undef
    if reverse
        rng = collect(length(array):-1:1)
    else
        rng = collect(1:length(array))
    end

    for i in rng
        S = S + type(array[i])
    end
    
    return S
end