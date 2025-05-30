import numpy as np
from PIL import Image

# Load both images
original = Image.open("input.jpg.jpg").convert("RGB")
colorized = Image.open("grayscale(AI).png")

# Ensure both are RGB
colorized = colorized.convert("RGB")

# Resize to match original
colorized = colorized.resize(original.size)

# Convert to NumPy arrays and normalize
original_np = np.asarray(original, dtype=np.float32) / 255.0
colorized_np = np.asarray(colorized, dtype=np.float32) / 255.0

# Compute BCE loss manually
def bce_loss(y_true, y_pred):
    eps = 1e-7  # to prevent log(0)
    y_true = y_true.flatten()
    y_pred = y_pred.flatten()
    loss = -np.mean(y_true * np.log(y_pred + eps) + (1 - y_true) * np.log(1 - y_pred + eps))
    return loss

# Compute and print loss
loss_value = bce_loss(original_np, colorized_np)
print("✅ BCE Loss:", loss_value)
