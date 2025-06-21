input = [[1,3],[2,5]]
error_values: list[float] = []
theta_0 = 0
theta_1 = 1
learning_rate= 0.1
for x,y in input:
    h_x = theta_0 + (theta_1 * x)
    error = h_x - y
    error_values.append(error)

error_theta_0 = 0
error_theta_1 = 0
for (x,y),error_value in zip(input, error_values):
    print(f"Input: {x}, Error: {error_value}")
    error_theta_0 += error_value
    error_theta_1 += error_value *x 
 
theta_0 = theta_0 - learning_rate* error_theta_0 
theta_1 = theta_1 - learning_rate* error_theta_1 

print(f"Updated theta_0: {theta_0}, Updated theta_1: {theta_1}")

