# Mateusz Pełechaty, 261737
include("../src/gauss.jl")
using .blocksys
include("../src/utils.jl")



dir_name = "500000"
matrix_filepath = "../test_input/Dane" * dir_name * "_1_1/A.txt"
b_filepath= "../test_input/Dane" * dir_name * "_1_1/b.txt"

matrix, n, l  = read_matrix(matrix_filepath)
b = read_b(b_filepath)

@time begin
matrix, b = gauss_choice(matrix, b, n, l)
end
xs = get_solution_from_triangle_gauss_choice(matrix, b, n, l)

write_solution(xs, "solutions/gauss_choice"*dir_name*".txt", n, true)