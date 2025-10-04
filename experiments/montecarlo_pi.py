import random
import matplotlib.pyplot as plt

def estimate_pi(num_samples=10000):
    inside_circle = 0
    x_inside, y_inside = [], []
    x_outside, y_outside = [], []

    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

if __name__ == "__main__":
    samples = 10000
    pi, xi, yi, xo, yo = estimate_pi(samples)
    print(f"Estimated π after {samples} samples = {pi:.5f}")

    # Plotting
    plt.figure(figsize=(6,6))
    plt.scatter(xi, yi, color="blue", s=1, label="Inside Circle")
    plt.scatter(xo, yo, color="red", s=1, label="Outside Circle")
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(f"Monte Carlo π Estimate: {pi:.5f}")
    plt.legend()
    plt.show()
