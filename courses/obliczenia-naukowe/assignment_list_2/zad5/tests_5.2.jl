# Mateusz Pełechaty, indeks: 261737

include("utils.jl")
using Printf

function main()
    open("data_52.csv", "w") do io
        write(io, @sprintf("%s,%s,%s,%s\n", "i", "Float32", "Float64", "|Float32 - Float64|"))
        start = 0.01
        p_f32 = Float32(start)
        p_f64 = Float64(start)
        for i in 0:40
            write(io, @sprintf("%s,%s,%s,%s\n", i, p_f32, p_f64, abs(p_f32 - p_f64)))
            p_f32 = p_next(p_f32, Float32(3))
            p_f64 = p_next(p_f64, Float64(3))
        end
    end
end

main()