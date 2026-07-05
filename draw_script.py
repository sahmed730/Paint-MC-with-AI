from server import create_canvas, draw_rectangle, draw_circle, draw_line, draw_text, save_canvas

print("Initializing canvas...")
create_canvas(800, 400, "white")

print("Drawing glass tube...")
# Left narrow cylinder
draw_rectangle(100, 150, 400, 250, outline_color="black", width=3)
# Flared part using lines
draw_line(400, 150, 700, 50, fill_color="black", width=3)
draw_line(400, 250, 700, 350, fill_color="black", width=3)
draw_line(700, 50, 700, 350, fill_color="black", width=3) # Flat screen at the end

print("Drawing components...")
# Draw Cathode (left side)
draw_rectangle(110, 170, 130, 230, fill_color="silver", outline_color="black", width=2)
draw_text(80, 260, "Cathode (-)", fill_color="black")

# Draw Anode (middle with slit)
draw_rectangle(300, 150, 320, 190, fill_color="silver", outline_color="black", width=2)
draw_rectangle(300, 210, 320, 250, fill_color="silver", outline_color="black", width=2)
draw_text(290, 260, "Anode (+)", fill_color="black")

# Draw Deflecting Plates
draw_rectangle(450, 100, 550, 120, fill_color="red", outline_color="black", width=2)
draw_text(470, 75, "+ Plate", fill_color="red")

draw_rectangle(450, 280, 550, 300, fill_color="blue", outline_color="black", width=2)
draw_text(470, 310, "- Plate", fill_color="blue")

print("Drawing electron beam...")
# Draw Electron Beam
draw_line(130, 200, 500, 200, fill_color="green", width=3) # straight through slit
draw_line(500, 200, 690, 100, fill_color="green", width=3) # deflected towards positive plate

# Dot on screen
draw_circle(690, 100, 6, fill_color="lime", outline_color="green", width=1)
draw_text(580, 80, "Electron Beam", fill_color="green")
draw_text(710, 200, "Fluorescent Screen", fill_color="black")

# Main Title
draw_text(300, 20, "Cathode Ray Tube Experiment", fill_color="black")

print("Saving image...")
# Save to Downloads
save_path = "C:/Users/AHMED/Downloads/cathode_ray_paint.png"
save_canvas(save_path)
print(f"Successfully saved to {save_path}")
