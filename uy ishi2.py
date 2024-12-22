def fibonaci(n):
    if n <= 0:
        return []
    f_list = [0, 1]
    for _ in range(2, n):
        f_list.append(f_list[-1] + f_list[-2])
    return f_list[:n]
n = 5
print(fibonaci(n))
