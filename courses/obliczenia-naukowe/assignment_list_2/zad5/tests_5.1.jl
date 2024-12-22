# Mateusz Pełechaty, indeks: 261737

include("utils.jl")
using Printf

function main()
    open("data_51.csv", "w") do io
        write(io, @sprintf("%s,%s,%s,%s\n", "i", "normal", "interrupted", "|difference|"))

        p_1 = Float32(0.01)
        p_2 = Float32(0.01)
        for i in 0:40
            if i == 10
                p_2 = trunc(p_2; digits=3)
            end
            write(io, @sprintf("%s,%s,%s,%s\n", i, p_1, p_2, abs(p_1-p_2)))
            p_1 = p_next(p_1, Float32(3.0))
            p_2 = p_next(p_2, Float32(3.0))

        end
    end
end

main()