# zeusconnect
Zeusconnect helps you connect your lnd lightning node to your Zeus wallet

## What is zeusconnect for?
Easier connection between your lnd lightning node and your mobile zeus wallet

## Installation
First, clone repository to your node. Run this in your terminal:

```sh
git clone https://github.com/proofofjogi/zeusconnect.git
```

And then move into the repository directory
```sh
cd zeusconnect
```

Make a virtual environment and activate it. This requires python3-venv to be installed. Run
```sh
sudo apt install python3-venv
```

to install python3-venv. Next we make a virtual environment named env and activate it:

```sh
python3 -m venv env
source env/bin/activate
```

Now we can install al python dependencies:
```sh
pip install -r requirements.txt
```
That's it for the installation. Now we need to configure zeusconnect.

## Configuration

Within the zeusconnect folder, there's a confiduration file. It is config.json looks like this initially:

```sh
{
  "lnd_macaroon": "<configure/path/to/macaroon/here/>",
  "port": "4204"
}
```

That file won't work like that. The lnd_macaroon path needs to point to your admin.macaroon file inside your lnd folder. See this example:
```sh
{
  "lnd_macaroon": "~/.lnd/data/chain/bitcoin/mainnet/admin.macaroon",
  "port": "4204"
}
```
Configure config.json accordingly using the path on your node, wherever your .lnd folder is.

Note, by default this application runs on port 4204. You can change the port in the config file if you find a conflict on your node.

## Run

You can now run zeusconnect.py on your node. Make sure that the environmet is active to run.

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

You can access zeusconnect on your node IP address, in this example it is served at http://192.168.1.33:4204. You will be able to connect Zeus to your node using the hex string output.
