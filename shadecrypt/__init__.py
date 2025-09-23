import os
from shadecrypt.core import shadeDB

try:
  os.mkdir('~/.shadecrypt/',0o744)
except Exception as error:
  pass
CONFIG_PATH = '~/.shadecrypt/config.scdb'
if not os.path.exists(CONFIG_PATH):
  with open(CONFIG_PATH,"w"):
    pass
  os.chmod(CONFIG_PATH,0o644)
  instance = shadeDB(CONFIG_PATH,write=True)
instance = shadeDB(CONFIG_PATH,write=True)

  