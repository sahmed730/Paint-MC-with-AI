# Paint MCP with AI

A Model Context Protocol (MCP) server that provides AI assistants with tools to programmatically draw and save images using Python's Pillow library.

## Features
- Create a canvas with a specified size and background color
- Draw rectangles, circles, and lines
- Add text to the canvas
- Save the resulting canvas to a file

## Setup
1. Create a Python virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration for MCP Client
Add the following to your MCP client settings JSON file (e.g. Claude Desktop or Cursor):

```json
{
  "mcpServers": {
    "paint": {
      "command": "C:\\path\\to\\paint-mcp\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\path\\to\\paint-mcp\\server.py"
      ]
    }
  }
}
```

## Example
Check `draw_script.py` for an example of how the tools can be used programmatically to draw diagrams.
