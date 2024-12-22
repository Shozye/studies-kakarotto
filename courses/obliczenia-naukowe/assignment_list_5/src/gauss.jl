# Mateusz Pełechaty, 261737

module blocksys
export gauss, gauss_choice, get_solution_from_triangle_gauss, get_solution_from_triangle_gauss_choice, write_solution, get_solution_from_lu, lu_
include("utils.jl")
using LinearAlgebra

function zero_cell(matrix, l, b, row, diag_i)
    d = matrix[indices(l, row, diag_i)...] / matrix[indices(l, diag_i, diag_i)...]
    b[row] -= d*b[diag_i]
    for col in (diag_i):(diag_i+l)
        matrix[indices(l, row, col)...] -= matrix[indices(l, diag_i, col)...]*d    
    end
    
end

function zero_cell_with_d_save(matrix, l, b, row, diag_i)
    d = matrix[indices(l, row, diag_i)...] / matrix[indices(l, diag_i, diag_i)...]
    matrix[indices(l, row, diag_i)...] = d
    for col in (diag_i+1):(diag_i+l)
        matrix[indices(l, row, col)...] -= matrix[indices(l, diag_i, col)...]*d    
    end
end

function gauss(matrix, b, n, l)
    for start_row in 0:l:n-1
        for diag_i in (start_row+1):(start_row+l-1)
            for row in (diag_i+1):min(start_row+l+1,n)
                zero_cell(matrix, l, b, row, diag_i)
            end
        end

        diag_i = start_row + l
        for row in (diag_i+1):min(diag_i+l,n)
            zero_cell(matrix, l, b, row, diag_i)
        end
    end
    return matrix, b
end

function lu_(matrix, b, n, l)
    for start_row in 0:l:n-1
        for diag_i in (start_row+1):(start_row+l-1)
            for row in (diag_i+1):min(start_row+l+1,n)
                zero_cell_with_d_save(matrix, l, b, row, diag_i)
            end
        end

        diag_i = start_row + l
        for row in (diag_i+1):min(diag_i+l,n)
            zero_cell_with_d_save(matrix, l, b, row, diag_i)
        end
    end
    return matrix, b
end

function gauss_choice(matrix, b, n, l)
    for start_row in 0:l:n-1
        for in_square in 1:l
            diag_i = start_row + in_square
            
            max_num_in_column = 0
            max_row = 0
            for row in diag_i:min(diag_i+l,n)
                temp = abs(matrix[indices(l, row, diag_i)...])
                if temp > max_num_in_column
                    max_num_in_column = temp
                    max_row = row
                end
            end
            swap_rows(matrix, l, diag_i, max_row)
            to_swap = b[max_row]
            b[max_row] = b[diag_i]
            b[diag_i] = to_swap

            for row in (diag_i+1):min(diag_i+l,n)
                d = matrix[indices(l, row, diag_i)...] / matrix[indices(l, diag_i, diag_i)...]
                b[row] -= d*b[diag_i]
                
                for col in (diag_i):(diag_i+2*l)
                    r1, c1 = indices(l, row, col)
                    if c1 > 4*l
                        break
                    end
                    matrix[r1, c1] -= matrix[indices(l, diag_i, col)...]*d    
                end
            end
        end
    end
    return matrix, b
end

function get_solution_from_triangle_gauss(matrix, b, n, l)
    for i in n:-1:1
        b[i] /= matrix[indices(l, i, i)...]     
        for upper in (i-1):-1:max(i-l,1)
            b[upper] -= matrix[indices(l, upper, i)...]*b[i]
        end
    end
    return b
end
function get_solution_from_triangle_gauss_choice(matrix, b, n, l)
    for i in n:-1:1
        b[i] /= matrix[indices(l, i, i)...]     
        for upper in (i-1):-1:max(i-2*l,1)
            b[upper] -= matrix[indices(l, upper, i)...]*b[i]
        end
    end
    return b
end
function get_solution_from_lu(matrix, b, n, l)
    for i in 1:n   
        for down in (i+1):min(i+l,n)
            b[down] -= matrix[indices(l, down, i)...]*b[i]
        end
    end
    return get_solution_from_triangle_gauss(matrix, b, n, l)
end
function write_solution(xs, filename, n, calculate_error)
    open(filename, "w") do file
        if calculate_error
            err = norm(xs - ones(n)) / norm(xs)
            write(file, string(err), "\n")
        end
        foreach(x->write(file, string(x), "\n"), xs)
    end
end
end # module