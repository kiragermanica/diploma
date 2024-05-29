from flask import render_template, request
import qrcode
from io import BytesIO
import base64
from . import routes_bp

@routes_bp.route('/qrcode', methods=['GET', 'POST'])
def qrcode_generator():
    if request.method == 'POST':
        data = request.form['data']
        img = qrcode.make(data)
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return render_template('qrcode.html', qrcode_image=img_base64)
    return render_template('qrcode.html')
