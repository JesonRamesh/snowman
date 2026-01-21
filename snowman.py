import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# --- Body ---
# Bottom circle
bottom_circle = plt.Circle((0.5, 0.3), 0.25, color='white', ec='black')
ax.add_patch(bottom_circle)

# Middle circle
middle_circle = plt.Circle((0.5, 0.7), 0.2, color='white', ec='black')
ax.add_patch(middle_circle)

# Head circle
head_circle = plt.Circle((0.5, 1.0), 0.15, color='white', ec='black')
ax.add_patch(head_circle)

# --- Face ---
# Eyes
left_eye = plt.Circle((0.45, 1.05), 0.02, color='black')
right_eye = plt.Circle((0.55, 1.05), 0.02, color='black')
ax.add_patch(left_eye)
ax.add_patch(right_eye)

# Nose (a triangle)
nose = plt.Polygon([[0.5, 1.0], [0.5, 0.95], [0.6, 0.98]], color='orange')
ax.add_patch(nose)

# Mouth (a few small circles)
mouth_dot1 = plt.Circle((0.47, 0.92), 0.01, color='black')
mouth_dot2 = plt.Circle((0.5, 0.91), 0.01, color='black')
mouth_dot3 = plt.Circle((0.53, 0.92), 0.01, color='black')
ax.add_patch(mouth_dot1)
ax.add_patch(mouth_dot2)
ax.add_patch(mouth_dot3)

# --- Buttons ---
button1 = plt.Circle((0.5, 0.75), 0.02, color='black')
button2 = plt.Circle((0.5, 0.65), 0.02, color='black')
button3 = plt.Circle((0.5, 0.55), 0.02, color='black')
ax.add_patch(button1)
ax.add_patch(button2)
ax.add_patch(button3)

# --- Arms ---
# Left arm
ax.plot([0.3, 0.1], [0.7, 0.8], color='brown', linewidth=5)
ax.plot([0.1, 0.0], [0.8, 0.85], color='brown', linewidth=3) # Fingers
ax.plot([0.1, 0.05], [0.8, 0.75], color='brown', linewidth=3) # Fingers

# Right arm
ax.plot([0.7, 0.9], [0.7, 0.8], color='brown', linewidth=5)
ax.plot([0.9, 1.0], [0.8, 0.85], color='brown', linewidth=3) # Fingers
ax.plot([0.9, 0.95], [0.8, 0.75], color='brown', linewidth=3) # Fingers


# --- Hat ---
hat_bottom = plt.Rectangle((0.35, 1.1), 0.3, 0.05, color='black')
hat_top = plt.Rectangle((0.4, 1.15), 0.2, 0.15, color='black')
ax.add_patch(hat_bottom)
ax.add_patch(hat_top)


# Set plot limits and aspect ratio
ax.set_xlim(0, 1)
ax.set_ylim(0, 1.5)
ax.set_aspect('equal', adjustable='box')
ax.axis('off') # Hide the axes

# Add a title
plt.title("Snowman")

# Show the plot
plt.show()
