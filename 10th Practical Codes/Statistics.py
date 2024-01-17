import statistics

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 5, 6, 7, 7, 7]

print("Mean value: %.2f" % statistics.mean(l))
print("Median value: %.2f" % statistics.median(l))
print("Mode value: %.2f" % statistics.mode(l))
