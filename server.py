from io import BytesIO
from flask import Flask, send_file, request

from composer import ImageComposer

app = Flask(__name__)

@app.route("/")
def index():
    # Get API Key
    api_key = request.args.get("api_key")
    if not api_key:
        return '{"error": "no_api_key"}'
    # Render
    composer = ImageComposer(
        api_key,
        lat=request.args.get("latitude", "43.0639"),
        long=request.args.get("longitude", "-70.9677"),
        timezone=request.args.get("timezone", "America/New_York"),
    )
    output = composer.render()
    # Send to client
    output.seek(0)
    return send_file(output, mimetype="image/png")
