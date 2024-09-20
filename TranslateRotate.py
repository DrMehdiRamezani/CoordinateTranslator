import math

def rotate_x(x, y, z, alpha):
    cos_alpha = math.cos(math.radians(alpha))
    sin_alpha = math.sin(math.radians(alpha))
    y_new = y * cos_alpha - z * sin_alpha
    z_new = y * sin_alpha + z * cos_alpha
    return x, y_new, z_new

def rotate_y(x, y, z, beta):
    cos_beta = math.cos(math.radians(beta))
    sin_beta = math.sin(math.radians(beta))
    x_new = x * cos_beta + z * sin_beta
    z_new = -x * sin_beta + z * cos_beta
    return x_new, y, z_new

def rotate_z(x, y, z, gamma):
    cos_gamma = math.cos(math.radians(gamma))
    sin_gamma = math.sin(math.radians(gamma))
    x_new = x * cos_gamma - y * sin_gamma
    y_new = x * sin_gamma + y * cos_gamma
    return x_new, y_new, z

def translate_coordinates(x, y, z, delta_x, delta_y, delta_z, delta_alpha=0, delta_beta=0, delta_gamma=0):
    x_new = x + delta_x
    y_new = y + delta_y
    z_new = z + delta_z

    x_new, y_new, z_new = rotate_x(x_new, y_new, z_new, delta_alpha)
    x_new, y_new, z_new = rotate_y(x_new, y_new, z_new, delta_beta)
    x_new, y_new, z_new = rotate_z(x_new, y_new, z_new, delta_gamma)

    return x_new, y_new, z_new

if __name__ == "__main__":
    x = 10.0
    y = 5.0
    z = 2.0
    alpha = 30.0
    beta = 45.0
    gamma = 60.0

    delta_x = 2.0
    delta_y = -1.0
    delta_z = 0.5
    delta_alpha = 5.0
    delta_beta = -2.0
    delta_gamma = 3.0

    x_new, y_new, z_new = translate_coordinates(x, y, z, delta_x, delta_y, delta_z, delta_alpha, delta_beta, delta_gamma)

    print("New coordinates (X, Y, Z) in the new coordinate system:")
    print(f"X: {x_new}, Y: {y_new}, Z: {z_new}")
