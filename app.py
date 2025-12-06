from flask import Flask, jsonify

# إنشاء تطبيق Flask
app = Flask(__name__)

# الرابط الذي تريد تخزينه
STORED_URL = "https://gilded-axolotl-58b093.netlify.app"

@app.route('/get-link', methods=['GET'])
def get_link():
    """
    هذه هي نقطة النهاية (Endpoint) التي ستعيد الرابط.
    """
    response = {
        "status": "success",
        "url": STORED_URL
    }
    return jsonify(response)