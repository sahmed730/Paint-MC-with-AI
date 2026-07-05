import io
import base64
import cv2
import numpy as np
from mcp.server.fastmcp import FastMCP
from PIL import Image, ImageDraw

# Initialize the MCP Server
mcp = FastMCP("Paint")

# Global state for the canvas
canvas = None
draw = None

@mcp.tool()
def create_canvas(width: int, height: int, background_color: str = "white") -> str:
    """
    Create a new blank canvas with the given dimensions and background color.
    Background color can be a name (e.g. 'white', 'black', 'red') or hex (e.g. '#FFFFFF').
    """
    global canvas, draw
    canvas = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(canvas)
    return f"Created canvas {width}x{height} with background {background_color}."

@mcp.tool()
def draw_rectangle(x0: int, y0: int, x1: int, y1: int, fill_color: str = None, outline_color: str = None, width: int = 1) -> str:
    """
    Draw a rectangle on the canvas from top-left (x0, y0) to bottom-right (x1, y1).
    Colors can be names or hex codes. If fill_color is omitted, it will be transparent.
    """
    if not canvas: return "Error: Create a canvas first."
    draw.rectangle([x0, y0, x1, y1], fill=fill_color, outline=outline_color, width=width)
    return f"Drew rectangle from ({x0},{y0}) to ({x1},{y1})."

@mcp.tool()
def draw_circle(x: int, y: int, radius: int, fill_color: str = None, outline_color: str = None, width: int = 1) -> str:
    """
    Draw a circle on the canvas at center (x, y) with given radius.
    """
    if not canvas: return "Error: Create a canvas first."
    draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill=fill_color, outline=outline_color, width=width)
    return f"Drew circle at ({x},{y}) with radius {radius}."

@mcp.tool()
def draw_line(x0: int, y0: int, x1: int, y1: int, fill_color: str = "black", width: int = 1) -> str:
    """
    Draw a line on the canvas from (x0, y0) to (x1, y1).
    """
    if not canvas: return "Error: Create a canvas first."
    draw.line([x0, y0, x1, y1], fill=fill_color, width=width)
    return f"Drew line from ({x0},{y0}) to ({x1},{y1})."
    
@mcp.tool()
def draw_text(x: int, y: int, text: str, fill_color: str = "black") -> str:
    """
    Draw text on the canvas at (x, y). 
    """
    if not canvas: return "Error: Create a canvas first."
    draw.text((x, y), text, fill=fill_color)
    return f"Drew text '{text}' at ({x},{y})."

@mcp.tool()
def sketch_image(image_path: str, x_offset: int = 0, y_offset: int = 0, max_width: int = 400, line_color: str = "black", detail: int = 2) -> str:
    """
    Trace a real photo/painting file (jpg/png) onto the canvas as pencil-style line strokes.
    This uses classic edge-detection (not the AI's memory) to compute every stroke, so it works
    for complex images like portraits that would be impossible to hand-calculate coordinate by coordinate.

    image_path: path to a source image on disk (e.g. a Mona Lisa reference photo).
    max_width: the drawing is scaled to this width so stroke count stays reasonable.
    detail: 1 = very detailed/many strokes, 3-5 = simplified/fewer strokes. Raise this if drawing is too slow or too busy.
    """
    if not canvas:
        return "Error: Create a canvas first."

    img = cv2.imread(image_path)
    if img is None:
        return f"Error: could not read image at {image_path}. Check the path."

    # Downscale so we get a sensible number of strokes instead of tens of thousands
    h, w = img.shape[:2]
    scale = max_width / w
    img = cv2.resize(img, (max_width, int(h * scale)))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    stroke_count = 0
    for contour in contours:
        # approxPolyDP collapses each contour down to its essential corner points,
        # turning a jagged pixel outline into a handful of straight pencil strokes
        simplified = cv2.approxPolyDP(contour, epsilon=float(detail), closed=False)
        points = simplified.reshape(-1, 2)
        for i in range(len(points) - 1):
            x0, y0 = points[i]
            x1, y1 = points[i + 1]
            draw.line(
                [int(x0) + x_offset, int(y0) + y_offset, int(x1) + x_offset, int(y1) + y_offset],
                fill=line_color,
                width=1,
            )
            stroke_count += 1

    return f"Sketched '{image_path}' using {stroke_count} traced pencil strokes."

@mcp.tool()
def save_canvas(filepath: str) -> str:
    """
    Save the current canvas to a file (e.g. C:/Users/AHMED/image.png).
    """
    if not canvas: return "Error: Create a canvas first."
    canvas.save(filepath)
    return f"Saved canvas to {filepath}."

if __name__ == "__main__":
    # Run the MCP server using standard input/output
    mcp.run(transport='stdio')
