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
