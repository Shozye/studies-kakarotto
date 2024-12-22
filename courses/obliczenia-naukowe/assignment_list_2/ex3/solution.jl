using Printf

include("hilb.jl")
include("matcond.jl")

function gauss(A, b)
    return A\b
end

function inversion(A, b)
    return inv(A)*b
end

function relative_error(x_approx, x)
    return norm(x_approx - x) / norm(x)
end

hilbert_n = 1:20
random_n = [5,10,20]
possible_c = [1.0,10.0,10.0^3,10.0^7,10.0^12,10.0^16]

open("hilbert.csv", "w") do io
    write(io, @sprintf("%s,%s,%s,%s,%s\n", "n", "cond(A)", "rank(A)", "A\\b error", "inv(A)*b error"))
    for n in hilbert_n
        A = hilb(n)
        x, b = (ones(Float64, n), A * ones(Float64, n))
        write(io, @sprintf("%s,%s,%s,%s,%s\n", n, cond(A), rank(A), relative_error(gauss(A, b),x), relative_error(inversion(A, b), x)))
    end
end

open("random.csv", "w") do io
    write(io, @sprintf("%s,%s,%s,%s,%s,%s\n", "n", "c", "cond(A)", "rank(A)", "A\\b error", "inv(A)*b error"))
    for n in random_n
        for c in possible_c
            A = matcond(n,c)
            x, b = (ones(Float64, n), A * ones(Float64, n))
            write(io, @sprintf("%s,%s,%s,%s,%s,%s\n", n, c, cond(A), rank(A), relative_error(gauss(A, b),x), relative_error(inversion(A, b), x)))
        end
    end
end