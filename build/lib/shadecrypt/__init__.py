import os

CONFIG_PATH = os.getenv("SHADECRYPT_CONFIG") or os.path.expanduser("~/.shadecrypt/config.scdb")

if not os.path.exists(CONFIG_PATH):
  instance = shadecrypt(CONFIG_PATH,write=True)
instance = shadecrypt(CONFIG_PATH,write=True)