from flask import Flask, jsonify, request, redirect
import uuid

app = Flask(__name__)

# --- الإعدادات ---
REAL_WEBSITE_URL = "https://gilded-axolotl-58b093.netlify.app" 
API_SECRET_KEY = "S3cretPass2025" 

# قاموس لتخزين التوكنات (المفاتيح المؤقتة) المرتبطة بمعرف المستخدم
# Format: { "user_id_A": "token_A", "user_id_B": "token_B", ... }
user_tokens = {}

@app.route('/get-link', methods=['GET'])
def get_link():
    # 1. التحقق من كلمة السر
    auth_header = request.headers.get('Authorization')
    if auth_header != API_SECRET_KEY:
        return jsonify({"status": "error", "message": "Forbidden"}), 403

    # 2. الحصول على معرف المستخدم من رأس الطلب (Header)
    # ملاحظة: يجب أن يرسل التطبيق هذا المعرف في كل طلب
    user_id = request.headers.get('X-User-ID')
    
    if not user_id:
        return jsonify({"status": "error", "message": "Missing X-User-ID header"}), 400

    # 3. التحقق: هل هذا المستخدم لديه توكن مخزَّن مسبقاً؟
    if user_id in user_tokens:
        unique_token = user_tokens[user_id]
    else:
        # إذا كان مستخدماً جديداً، نولِّد له توكن جديد ونخزِّنه
        unique_token = str(uuid.uuid4())
        user_tokens[user_id] = unique_token # التخزين للمستقبل

    # 4. إرسال الرابط المؤقت
    masked_link = f"{request.host_url}go/{unique_token}"
    
    return jsonify({
        "status": "success",
        "url": masked_link
    })

@app.route('/go/<token>', methods=['GET'])
def redirect_to_site(token):
    # نتحقق مما إذا كان التوكن المقدم (Token) هو قيمة لأي مفتاح (User ID) في قاموسنا
    if token in user_tokens.values():
        # التوكن موجود ويسمح بالوصول المتكرر
        return redirect(REAL_WEBSITE_URL)
    else:
        # التوكن غير معروف أو لم يتم توليده من قبل
        return "Invalid Link or Forbidden Access.", 404

if __name__ == '__main__':
    app.run(debug=True)
