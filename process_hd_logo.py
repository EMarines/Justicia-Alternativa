from PIL import Image
import numpy as np

# Load HD logo
img_path = r"C:\Users\Propietario\.gemini\antigravity-ide\brain\0eae5e56-2a52-42a8-b877-9f36292e7173\media__1786216213884.png"
img = Image.open(img_path).convert("RGBA")
data = np.array(img)

# Unpack channels
r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]

# Identify white/light background (R, G, B all > 235)
is_white_bg = (r > 235) & (g > 235) & (b > 235)

# Set alpha to 0 for background
data[is_white_bg, 3] = 0

# Create PIL image to trim whitespace
img_trans = Image.fromarray(data)

# Get bounding box of non-zero alpha pixels
bbox = img_trans.getbbox()
if bbox:
    img_cropped = img_trans.crop(bbox)
else:
    img_cropped = img_trans

# Now create dark-theme version:
# Where text is dark navy/black (R < 80, G < 80, B < 100 and Alpha > 50), turn text to bright crisp white (#FFFFFF)
crop_data = np.array(img_cropped)
cr, cg, cb, ca = crop_data[:,:,0], crop_data[:,:,1], crop_data[:,:,2], crop_data[:,:,3]

is_dark_text = (cr < 90) & (cg < 90) & (cb < 110) & (ca > 30)

crop_dark_bg = crop_data.copy()
# Set dark text pixels to pure white with anti-aliasing blending
crop_dark_bg[is_dark_text, 0] = 255
crop_dark_bg[is_dark_text, 1] = 255
crop_dark_bg[is_dark_text, 2] = 255

# Save HD PNGs
img_hd_dark = Image.fromarray(crop_dark_bg)
img_hd_dark.save(r"c:\Users\Propietario\Web Proyects\MascChih-LP\logo_hd_dark.png")

img_hd_light = Image.fromarray(crop_data)
img_hd_light.save(r"c:\Users\Propietario\Web Proyects\MascChih-LP\logo_hd_light.png")

print("Cropped size:", img_cropped.size)
print("Successfully generated logo_hd_dark.png and logo_hd_light.png!")
