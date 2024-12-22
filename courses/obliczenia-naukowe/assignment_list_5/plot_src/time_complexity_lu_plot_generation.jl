n =     [10000,       50000,       100000,     300000,     500000]
times = [0.034*0.01, 0.033*0.05, 0.035*0.11, 0.041*0.24 ,0.05*0.33]

using Plots

plot(n, times, label="Gauss", xlabel="n", ylabel="time [s]", legend=:topleft, title="LU decomposition time complexity")
savefig("lu_time_complexity.png")