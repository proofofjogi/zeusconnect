from flask import Flask, render_template, url_for
import os
import subprocess
import PIL
import qrcode
import json

app = Flask(__name__)


def load_cofig():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


@app.route("/")
def connect():
    # Open configuration file:
    config = load_cofig()
    path = config.get("lnd_macaroon")
    if path.startswith("<"):
        return render_template('configure.html')
    #~/.lnd/data/chain/bitcoin/mainnet/admin.macaroon

    macaroon = subprocess.check_output(f'xxd -p -c2000 {path}', shell=True).decode()

    img = qrcode.make(macaroon)
    qr = 'connection_qr.png'
    img.save(os.getcwd() + '/static/' + qr, 'PNG')

    return render_template('connect.html', macaroon=macaroon, qr=qr)


if __name__ == '__main__':
    config = load_cofig()
    port = config.get("port")
    app.run(host='0.0.0.0', port=port, debug=True)
