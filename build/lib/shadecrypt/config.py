from shadecrypt.__init__ import instance
from shadecrypt.model import shadecrypt


def load_config():
  if os.path.exists(CONFIG_PATH):
    return instance.export_dict()
  return {"current_db": None, "recent": None}


def set_current_db(path,backup=False):
    instance.update(('current_db',path))
    instance.update(('backup',backup))
    cur_history = instance.get('history')
    instance.update(('recent',cur_history))