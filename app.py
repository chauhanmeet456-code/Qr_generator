from flask import Flask, render_template, request, send_file
import qrcode
import os
from PIL import ImageColor

app = Flask(__name__)

QR_FOLDER = "static/generated"

if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)


@app.route("/", methods=["GET", "POST"])
def home():

    qr_path = None

    if request.method == "POST":

        data = request.form.get("data")

        size = int(request.form.get("size", 10))

        fill = request.form.get("fill", "#000000")

        back = request.form.get("back", "#ffffff")

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill, back_color=back)

        filename = "qr.png"

        qr_path = os.path.join(QR_FOLDER, filename)

        img.save(qr_path)

        qr_path = "/" + qr_path.replace("\\", "/")

    return render_template("index.html", qr=qr_path)


@app.route("/download")
def download():

    file = os.path.join(QR_FOLDER, "qr.png")

    if os.path.exists(file):
        return send_file(file, as_attachment=True)

    return "No QR Generated"


if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=5000)
