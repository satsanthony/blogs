"""Draw a pelican riding a bicycle with matplotlib."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.set_aspect("equal")
ax.axis("off")
fig.patch.set_facecolor("#0b0f14")
ax.set_facecolor("#0b0f14")

# Ground
ax.plot([0, 10], [1.5, 1.5], color="#3a4a5a", lw=3)

# Wheels
for cx in (3, 7):
    ax.add_patch(plt.Circle((cx, 2.2), 1.1, fill=False, color="#9fd3e8", lw=3))
    ax.add_patch(plt.Circle((cx, 2.2), 0.12, color="#9fd3e8"))
    for a in np.linspace(0, np.pi, 6, endpoint=False):
        ax.plot([cx - np.cos(a) * 1.05, cx + np.cos(a) * 1.05],
                [2.2 - np.sin(a) * 1.05, 2.2 + np.sin(a) * 1.05],
                color="#5a7a8a", lw=0.8)

# Frame
frame = [[3, 2.2, 5, 2.2], [5, 2.2, 4.3, 4.0], [3, 2.2, 4.3, 4.0],
         [5, 2.2, 6.6, 4.1], [6.6, 4.1, 7, 2.2], [4.3, 4.0, 4.1, 4.6]]
for x1, y1, x2, y2 in frame:
    ax.plot([x1, x2], [y1, y2], color="#7ab8d4", lw=3)
ax.plot([6.4, 6.8], [4.4, 4.1], color="#7ab8d4", lw=3)   # handlebar stem
ax.plot([6.1, 6.5], [4.7, 4.4], color="#9fd3e8", lw=4)   # handlebar
ax.plot([3.7, 4.5], [4.7, 4.7], color="#9fd3e8", lw=5)   # seat

# Pedals
ax.add_patch(plt.Circle((5, 2.2), 0.35, fill=False, color="#9fd3e8", lw=2))
ax.plot([4.75, 5.25], [1.95, 2.45], color="#9fd3e8", lw=3)

# Pelican body
ax.add_patch(mpatches.Ellipse((4.4, 5.4), 2.2, 1.5, angle=15, color="#f2f5f7"))
# Tail
ax.add_patch(mpatches.Polygon([[3.3, 5.2], [2.6, 5.9], [3.5, 5.8]], color="#dfe6ea"))
# Neck
ax.plot([5.2, 5.9, 6.0], [5.7, 6.3, 6.9], color="#f2f5f7", lw=14,
        solid_capstyle="round")
# Head
ax.add_patch(plt.Circle((6.05, 7.0), 0.42, color="#f2f5f7"))
# Eye
ax.add_patch(plt.Circle((6.18, 7.12), 0.07, color="#101417"))
# Beak with pouch
ax.add_patch(mpatches.Polygon([[6.35, 7.05], [7.9, 6.75], [6.4, 6.7]],
                              color="#f5a623"))
ax.add_patch(mpatches.Polygon([[6.4, 6.7], [7.9, 6.75], [6.7, 6.25]],
                              color="#e08c1a"))
# Wing reaching the handlebar
ax.plot([4.8, 6.2], [5.4, 4.6], color="#dfe6ea", lw=10, solid_capstyle="round")
# Leg to pedal
ax.plot([4.6, 5.0, 5.2], [4.9, 3.4, 2.5], color="#f5a623", lw=5,
        solid_capstyle="round")
ax.plot([5.0, 5.45], [2.45, 2.45], color="#f5a623", lw=4)  # webbed foot

ax.set_title("Pelican on a Bicycle", color="#9fd3e8", fontsize=16,
             fontfamily="serif", pad=12)
plt.savefig(r"C:\Projects\test\fable5\pelican_bike.png", dpi=110,
            bbox_inches="tight", facecolor="#0b0f14")
print("saved")
