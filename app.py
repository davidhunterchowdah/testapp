from flask import Flask, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='')

# Serve static HTML page
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# Health check endpoint (no-cache so proxies like Cloudflare don't serve stale timestamps)
@app.route('/api/health', methods=['GET'])
def health():
    response = jsonify({
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "environment": os.getenv("FLASK_ENV", "development")
    })
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    return response

# Placeholder endpoint
@app.route('/api/placeholder', methods=['GET'])
def placeholder():
    return jsonify({"message": "This is a placeholder endpoint"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
