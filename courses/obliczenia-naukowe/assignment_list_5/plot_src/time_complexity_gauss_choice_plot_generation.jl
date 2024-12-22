n =     [10000,       50000,       100000,     300000,     500000]
times = [0.065*0.011, 0.071*0.055, 0.075*0.14, 0.088*0.26 ,0.105*0.37]

using Plots

plot(n, times, label="Gauss", xlabel="n", ylabel="time [s]", legend=:topleft, title="Gauss partial choosing time complexity")
savefig("gauss_choice_time_complexity.png")