input = [[1,3],[2,5]]
theta_0 = 0
theta_1 = 1
learning_rate = 0.1
for x,y in input:
    h_x = theta_0 + (theta_1 * x)
    error = (h_x - y)
    theta_0 = theta_0 - (learning_rate * error)
    theta_1 = theta_1 - (learning_rate * error * x)

print(f"theta_0: {theta_0}, theta_1: {theta_1}")
    
