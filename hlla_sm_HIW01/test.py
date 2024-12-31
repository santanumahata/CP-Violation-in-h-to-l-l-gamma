import numpy as np

# Define the vectors
vector_a = np.array([-0.1742313221245323, 0.101860753449044, -0.2034796030405206])
vector_b = np.array([0.1553510235580065, -0.8156728502952673, 0.5572646708652533])

# Compute the dot product and magnitudes
dot_product = np.dot(vector_a, vector_b)
magnitude_a = np.linalg.norm(vector_a)
magnitude_b = np.linalg.norm(vector_b)

# Compute the cosine of the angle, ensuring it stays within [-1, 1]
cos_theta = dot_product / (magnitude_a * magnitude_b)
cos_theta = np.clip(cos_theta, -1.0, 1.0)  # Handle potential floating-point errors

# Compute the angle in radians and degrees
angle_rad = np.arccos(cos_theta)
angle_deg = np.degrees(angle_rad)

print(f"The angle between the vectors is {angle_deg:.2f} degrees.")
