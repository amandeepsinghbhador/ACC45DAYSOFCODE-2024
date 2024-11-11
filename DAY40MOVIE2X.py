
X, Y = map(int, input().split())


time_double_speed = Y // 2
time_normal_speed = X - Y


total_time = time_double_speed + time_normal_speed


print(total_time)
