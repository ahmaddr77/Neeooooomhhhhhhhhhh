
# إنشاء تطبيق Flask
app = Flask(__name__)

# الرابط الذي تريد تخزينه
# !!! قم بتغيير هذا الرابط إلى الرابط الذي تريده !!!
STORED_URL = "https://gilded-axolotl-58b093.netlify.app/"

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

# هذا السطر ضروري لمنصة النشر لتشغيل السيرفر
# لا تحتاج إلى تشغيله محلياً
if __name__ == '__main__':
    # سيتم تشغيل السيرفر على منفذ تحدده منصة النشر تلقائياً
    app.run(host='0.0.0.0', port=5000)