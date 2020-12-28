# SpotiMy
![License](https://img.shields.io/github/license/lmadduri/spotimy)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lmadduri/spotimy/CI)
[![codecov](https://codecov.io/gh/lmadduri/spotimy/branch/master/graph/badge.svg)](https://codecov.io/gh/lmadduri/spotimy)
[![Docs](https://img.shields.io/readthedocs/spotimy.svg)](https://spotimy.readthedocs.io/en/latest/)

An app that fills in the missing blanks with Spotify actions. Log into your account, accept the requested permissions, and view your top 10 favorite playlists. Additionally, use the terminal to enter one of the aesthetics to replace your most recent playlist covers based on the theme. Basic actions such as duplicating your playlists, creating a copy of someone else's playlist in your Spotify, arranging playlists in certain orders, and more features are currently in the process of being supported in a quick and easy way within the Spotify app, even the more powerful desktop app. 

## Tools Used
Python
SpotiPy
Flask

## Usage and Examples

Clone the repository
```bash
git clone https://github.com/lmadduri/SpotiMy.git
```

Use [pip](https://pip.pypa.io/en/stable/) to install dependencies
```bash
pip3 install -r requirements.txt
```

Ensure that you have a config.py file in the src folder that has credentials containing the following:
``` bash
username = "77wayghwgawa808wqf2ozfqpx"
client = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
redir = "http://127.0.0.1:9090"
```

Run the main file
```bash
python3 src/server.py
```

```bash
Welcome to SpotiMy!
Customize your playlist covers using this quick and easy tool
The aesthetics you can choose from are:
 ~~~ 
 neon, pearls, abstract, clouds, and art 
 ~~~
Which aesthetic would you like?
```
## Collaborators

Iliana Cantu and Lalitha Madduri (lm3302)