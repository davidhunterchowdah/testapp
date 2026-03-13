from flask import Flask, jsonify, send_from_directory
import os
from datetime import datetime

app = Flask(__name__, static_folder='public', static_url_path='')

# Serve static HTML page
@app.route('/')
def index():
    return send_from_directory('public', 'index.html')

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "environment": os.getenv("FLASK_ENV", "development")
    })

# Placeholder endpoint
@app.route('/api/placeholder', methods=['GET'])
def placeholder():
    return jsonify({"message": "This is a placeholder endpoint"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
