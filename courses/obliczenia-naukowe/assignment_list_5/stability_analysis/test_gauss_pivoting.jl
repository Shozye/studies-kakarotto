# Mateusz Pełechaty, 261737
include("../src/gauss.jl")
using .blocksys
using BenchmarkTools
include("../src/utils.jl")
using LinearAlgebra
using Plots
xs = []
values = []

for size in LinRange(1.0, 1000, 50)
    global xs, values
    sm = 0
    for i in 1:10
        matrix_filepath = "./creations/A_" * string(floor(size)) * "_"*string(i)*".txt"
        matrix, n, l  = read_matrix(matrix_filepath)
        b = get_b(matrix, ones(n), n, l)
        matrix, b = gauss_choice(matrix, b, n, l)
        curr_xs = get_solution_from_triangle_gauss_choice(matrix, b, n, l)
        sm += norm(curr_xs - ones(n)) / norm(curr_xs)
    end
    push!(xs, size)
    push!(values, sm/10)
end
plot(xs, values, xlabel="condition", ylabel="error", title="Error of Gauss with partial pivoting")
savefig("gauss_pivot.png")