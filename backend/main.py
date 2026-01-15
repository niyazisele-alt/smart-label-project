from flask import Flask, jsonify
from led import show_label as led_show
from lcd import show_label as lcd_show

app = Flask(__name__)

@app.route("/")
def home():
    # Ürün verisi
    product = {
        "name": "Süt 1L",
        "price": 29.90,
        "barcode": "869000000001"
    }

    # LED ekran simülasyonu
    led_show(product)

    # LCD ekran simülasyonu
    lcd_show(product)

    # Tarayıcıda JSON olarak göster
    return jsonify({
        "project": "Smart Label",
        "status": "running",
        "product": product,
        "display": ["LED", "LCD"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)