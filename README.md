# zeusconnect
Zeus Connect helps you connect your lnd lightning node to your Zeus wallet

## What is zeusconnect for?
Easier connection between your lndlightning node and your mobile zeus wallet

## Installation
Clone repository on your node:

```sh
git clone https://github.com/proofofjogi/zeusconnect.git
```

cd into the repository
```sh
cd zeusconnect
```

Make virtual environment and activate

(Requires python3-venv)
```sh
sudo apt install python3-venv
```

```sh
python3 -m venv env
source env/bin/activate
```

Install flask dependencies
```sh
pip install -r requirements.txt
```

## Configuration

config.json looks like this initially:

```sh
{
  "lnd_macaroon": "<configure/path/to/macaroon/here/>",
  "port": "4204"
}
```

That won't work like that. The lnd_macaroon path needs to point to your admin.macaroon file inside your lnd folder. See this example:
```sh
{
  "lnd_macaroon": "~/.lnd/data/chain/bitcoin/mainnet/admin.macaroon",
  "port": "4204"
}
```
Configure config.json accordingly using the path on your node, wherever your .lnd folder is.

Note, by default this application runs on port 4204. You can change the port in the config file if you find a conflict on your node.

## Run

You can now run Zeus Connect on your node. 

```sh
python zeusconnect.py
```

Will generate this output:

```sh
(env) user@host:~/zeusconnect$ python zeusconnect.py
 * Serving Flask app 'zeusconnect' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:4204
 * Running on http://192.168.1.33:4204 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 116-705-899
```

You can access it on your IP address, in this example it is 192.168.1.33:4204. You will be able to connect Zeus to your node using the Hex String or the QR code.
