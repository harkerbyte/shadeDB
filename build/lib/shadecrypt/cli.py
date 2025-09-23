import sys
from shadecrypt.model import shadecrypt
from shadecrypt.config import get_db,load_config,set_current_db

def main():
  if len(sys.argv) < 2:
    print('Usage: shadecrypt [args...]')
    sys.exit(1)
  
  command = sys.argv[1]
  if command == "status":
    print(load_config())
    
  args = sys.args[2:]
  
  loaded = load_config()
  shadeDB = shadecrypt(get_db(),write=loaded.get('export',True) ,backup=loaded.get('backup',False))
  
  if command == "init":
    if not args:
      print('Usage: shadecrypt init < db_path/db_name.scdb > < allow backup: True/False >')
      sys.exit(1)
    db_path = args[0]
    bkup = args[1] or False
    shadeDB = shadecrypt(db_path,backup=bkup)
    set_current_db(db_path)
    print(f'Initialised {db_path} and set as default')
    
    return
  
  if command == "use":
    db_path = args[0]
    bkup = args[1]  or False
    
    set_current_db(db_path,backup=bkup)
    print(f'shadecrypt: default db has been set to \x1b[1;32m{db_path}\x1b[1;0m\nAllow backup : {bkup}')
  
  if command == "ls":
    print(load_config().get("current_db",None))
    
  if command == "put":
    if not get_db:
      print(f'Error: couldn\'t access the db named {get_db}')
      sys.exit(1)
    
    pass