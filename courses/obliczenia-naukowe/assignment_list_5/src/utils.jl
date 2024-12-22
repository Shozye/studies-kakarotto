# Mateusz Pełechaty, 261737

function indices(l, i, j)
    return i, l + j - l*div(i-1, l)
end

function read_matrix(filename)
    matrix = []
    n = 0
    l = 0
    open(filename) do f
        n, l = split(readline(f), " ")
        n = parse(Int64, n)
        l = parse(Int64, l)
        matrix = zeros(n, l*4)
        while ! eof(f)        
           i, j, aij = split(readline(f), " ")   
           i = parse(Int64, i)
           j = parse(Int64, j)
           aij = parse(Float64, aij)
           matrix[indices(l, i, j)...] = aij
        end
    end
    return matrix, n, l
end

function read_b(filename)
    b = []
    open(filename) do f
        n = parse(Int64, readline(f))
        b = zeros(n)
        i = 1
        while ! eof(f)        
            b[i] = parse(Float64, readline(f))
            i += 1
        end
    end
    return b
end

function get_b(matrix, xs, n, l)
    b = zeros(n)
    for tl_diag in 1:l:n
        for row in tl_diag:(tl_diag+l-1)
            for col in max(1,tl_diag-l):min(tl_diag+2*l-1, n)
                b[row] += matrix[indices(l,row, col)...] * xs[col]
            end
        end
    end
    return b
end

function swap_rows(matrix, l, i1, i2)
    if i1 == i2
        return
    end
    if i1 > i2
        i1 = i1 + i2
        i2 = i1 - i2
        i1 = i1 - i2
    end
    # i1 < i2
    matrix_difference = div(i2-1, l) - div(i1-1, l)
    bias = matrix_difference * l
    for j in 1:(4*l)
        r1 = i1
        c1 = j + bias
        if c1 > 4*l
            break
        end
        to_swap = matrix[i2, j]
        matrix[i2, j] = matrix[r1, c1]
        matrix[r1, c1] = to_swap
    end
end