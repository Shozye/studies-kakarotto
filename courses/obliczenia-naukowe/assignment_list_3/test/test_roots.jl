# Mateusz Pełechaty, 261737
using Test

include("../src/roots.jl")
include("utils.jl")

function test_output(name, r, fr, it, err, expected, delta, epsilon, accuracy_flag)
    @testset "$name" begin
        if expected.it != Nothing
            @test expected.it == it
        end
        if (expected.err != Nothing)
            @test expected.err == err
        end
        if (expected.r != Nothing && expected.fr != Nothing)
            @test (err == accuracy_flag) || abs(r - expected.r) < delta || abs(fr - expected.fr) < epsilon
        end
    end
end

function test_method(method, f, delta, epsilon, input, expected, bad_accuracy_flag)
    test_output(String(Symbol(f)), method(input...)..., expected, delta, epsilon, bad_accuracy_flag)
end


@testset "Bisection" begin
    for data in bisection_data
        (f, _, _, delta, epsilon) = data.input
        test_method(Roots.bisection, f, delta, epsilon, data.input, data.output, -1)
    end
end

@testset "Newton" begin
    for data in newton_data
        (f, _, _, delta, epsilon, _) = data.input
        test_method(Roots.newton, f, delta, epsilon, data.input, data.output, 1)
    end
end

@testset "Secant" begin
    for data in secant_data
        (f, _, _, delta, epsilon, _) = data.input
        test_method(Roots.secant, f, delta, epsilon, data.input, data.output, 1)
    end
end