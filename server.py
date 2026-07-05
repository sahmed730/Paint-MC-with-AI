import io
import base64
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
