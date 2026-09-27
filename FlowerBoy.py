def eq_value(n):
    arr = [1]*n + [n] + [1]*n
    size = len(arr)
    for i in range(size):
        left_sum = 0 
        right_sum = 0
        for j in range(i):
            left_sum += arr[j]
        for k in range(i + 1, size):
            right_sum += arr[k]
        if left_sum == right_sum:
            return arr[i]
    return -1

n = int(input("Enter (try 5 or 6): "))
guess = input("What is eq_value(" + str(n) + ")? ")
print("  eq_value(" + str(n) + ") =", eq_value(n), "  your guess", guess)