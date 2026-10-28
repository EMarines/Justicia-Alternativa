from PIL import Image
import numpy as np

# Load original logo
img_path = r"C:\Users\Propietario\.gemini\antigravity-ide\brain\0eae5e56-2a52-42a8-b877-9f36292e7173\media__1786212628445.png"
img = Image.open(img_path).convert("RGBA")
data = np.array(img)

# R, G, B, A
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# The checkerboard consists of neutral greys/whites where R, G, B are all high and close to each other
# e.g., min(r,g,b) > 170 and max(r,g,b) - min(r,g,b) < 20 (neutral grey/white)
is_grey_white = (r > 170) & (g > 170) & (b > 170) & (np.maximum(np.maximum(r, g), b) - np.minimum(np.minimum(r, g), b) < 25)

# Make checkerboard background transparent
data[is_grey_white, 3] = 0

# For dark text (MASC / JUSTICIA ALTERNATIVA), since the landing page background is dark navy (#0a1628),
# dark text would be invisible! Let's make the text white/gold or create a high-contrast version for dark background.
# Dark text condition: R < 70, G < 70, B < 90
is_dark_text = (r < 70) & (g < 70) & (b < 90) & (a > 50)

# Create a dark-background optimized version where dark text becomes crisp white (#FFFFFF)
data_dark_bg = data.copy()
data_dark_bg[is_dark_text, 0] = 245 # R
data_dark_bg[is_dark_text, 1] = 240 # G
data_dark_bg[is_dark_text, 2] = 232 # B

# Save both clean transparent PNGs
img_clean = Image.fromarray(data)
img_clean.save(r"c:\Users\Propietario\Web Proyects\MascChih-LP\logo_original_clean.png")

img_dark_bg = Image.fromarray(data_dark_bg)
img_dark_bg.save(r"c:\Users\Propietario\Web Proyects\MascChih-LP\logo_transparent.png")

print("Successfully created logo_transparent.png!")
