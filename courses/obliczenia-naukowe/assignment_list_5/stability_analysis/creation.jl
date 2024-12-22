include("../src/matrixgen.jl")
using .matrixgen

for size in LinRange(1.0, 1000, 50)
    for i in 1:10
        matrix_filepath = "./creations/A_" * string(floor(size)) * "_"*string(i)*".txt"
        blockmat(20000, 4, size, matrix_filepath)
    end
end