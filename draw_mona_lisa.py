from server import create_canvas, save_canvas, sketch_image

print("Preparing canvas...")
create_canvas(600, 900, "white")

print("Sketching Mona Lisa from reference photo using computer vision contour tracing...")
# Using the new sketch_image tool created by the user!
sketch_image("mona_lisa.jpg")

print("Saving masterpiece...")
save_canvas("C:/Users/AHMED/Downloads/mona_lisa_pencil.png")
print("Saved to Downloads as mona_lisa_pencil.png!")
