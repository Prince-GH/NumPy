import numpy as np
import matplotlib.pyplot as plt  # ✅ Import for plotting

# Create grayscale image
img = np.random.randint(0, 226, (5, 5))

# Show grayscale image
print("\nGrayscale image:\n", img)
print(f"\nShape: {img.shape}")
# avg = np.mean(img)
# print(f"Average: {avg:.2f}")

thsval = float(input("Enter custom thsval: "))

# Convert to binary image
binImg = np.where(img >= thsval, 255, 0)
print(f"\nBinary image:\n{binImg}")

# ✅ Display both grayscale and binary images
plt.figure(figsize=(10, 4))

# Grayscale
plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.title("Grayscale Image")
plt.colorbar()

# Binary
plt.subplot(1, 2, 2)
plt.imshow(binImg, cmap='gray', vmin=0, vmax=255)
plt.title("Binary Image")
plt.colorbar()

plt.tight_layout()
plt.show()
