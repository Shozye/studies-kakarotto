n =     [10000,       50000,       100000,     300000,     500000]
times = [0.031*0.012, 0.033*0.052, 0.035*0.12, 0.042*0.24 ,0.049*0.35]

using Plots

plot(n, times, label="Gauss", xlabel="n", ylabel="time [s]", legend=:topleft, title="Gauss time complexity")
savefig("gauss_time_complexity.png")