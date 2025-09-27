# ShadeDB

![PyPI - Version](https://img.shields.io/pypi/v/shadeDB?color=blue&label=PyPI)  
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows%20%7C%20android-lightgrey)
![License](https://img.shields.io/pypi/l/shadeDB?color=yellow)
<a href = "https://facebook.com/harkerbyte">![Facebook](https://img.shields.io/badge/Facebook-%231877F2.svg?style=flat&logo=Facebook&logoColor=white)</a>
<a href ="https://youtube.com/@harkerbyte?si=aPSIREosLJlFOmyX" >![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=flat&logo=YouTube&logoColor=white)</a>
<a href="https://whatsapp.com/channel/0029Vb5f98Z90x2p6S1rhT0S">![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white)</a>
<a href="https://instagram.com/harkerbyte" >
![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=flat&amp;logo=instagram&amp;logoColor=white) </a>

[♟️ Mission](https://harkerbyte.github.io/portfolio/)

![1000094092](https://github.com/user-attachments/assets/da83cb25-8fad-4ad1-a326-bc6168b62009)


🚀 **shadeDB**, also know as **shadecrypt**, is a lightweight, multipurpose **CLI + Python database server** — small enough to run anywhere, yet powerful enough to manage structured data with speed and simplicity.  

Unlike traditional file-based CLIs, shadeDB works more like Redis:  

- You **initialize once** → a background server process holds the live database in memory.  
- All future CLI commands (`put`, `get`, `update`, etc.) talk to that server via a local socket.  
- The server **automatically persists** data to a `.scdb` file, with optional write and backup controls.  

---

## ✨ Features

- **Class-oriented design** — core database logic is in the `shadeDB` class.  
- **Persistent workflow** — one live server handles all operations.  
- **Background persistence** — in-memory with disk persistence.  
- **Portable** — runs on Linux, macOS, Windows, Android (via Termux).  
- **Multipurpose CLI** — simple commands: `init`, `start`, `use`, `pull`, `get`, `update`, `remove`, `ls`, `stop`.  
- **Config-aware** — automatically tracks the “current” DB in `~/.shadeDB/config.scdb`.  

---

## 🔧 Installation

```bash
pip install shadeDB
```

After install, the `shadeDB` command is available globally. A shorter keyword for shadeDB  - **scdb**

---

## ⚡ Quickstart (CLI)

### 1. Initialize a database  
Creates `./mydb.scdb`, starts the server, and sets it as default:  
```bash
shadeDB init ./mydb.scdb backup
```
⚠️ Only provide the "backup" argument if you intend for the server to register newer backups as you make new changes. 
---
### 2. Start database server
This is necessary, as the cli wrapper only communicates with the database server to retrieve,update,remove and store data.
```bash
shadeDB start
```
---

### 3. Insert data  
```bash
shadeDB update alice.age 17 && scdb update alice.gender female
```
---

### 4. Fetch data  
```bash
shadeDB get alice
# {"nickname": "Shade", "status": "active"}
```
---

### 5. Nested access  
```bash
shadeDB pull alice.nickname
# "Shade"
```

---
Making single value updates, it is compulsory to surround with double quotes.
### 6. Update  
```bash
shadeDB update alice "my name is alice"
```

---

### 7. Remove  
```bash
shadeDB remove alice 
# deletes {"nickname":"shade","status":"active"}
```
### 8. Remove nested 
```bash
shadeDB remove alice.nickname
# deletes {"nickname":"shade"} 
````
---

### 9. Check for the current database
```bash
shadeDB ls
# ./mysql.scsb
```

---

### 10. Switch database
```bash
shadeDB use ./backup.scdb backup
# Only provide the backup argument, if it need arises.
```

---

### 11. Stop server  
```bash
shadeDB stop
```

---

## 📚 Python API  

shadeDB can also be embedded directly into Python apps using the `ShadeDB` class.  

### 🔧 Initialize  
```python
from shadeDB.core import ShadeDB

db = ShadeDB(
    file="./data.scdb",
    write=True,
    id=True,
    backup=False
)
```

**Parameters**  
- `file (str)` → Path to `.scdb` file  
- `write (bool)` → Persist changes to disk (default: `True`)  
- `id (bool)` → Assign unique ID per entry (default: `True`)  
- `backup (bool)` → Keep backup copy (default: `False`)  

---

### 🛠️ Key Methods  

```python
db.update(("alice", {"nickname": "Shade", "status": "active"}))   # Insert/update
db.get("alice", multiple=True/False)      # Fetch record
db.get("alice.nickname")  # Fetch nested value
db.get_context("alice")   # Get full dict
db.get_by_id(1) # Fetch by ID
db.get_id("alice",multiple=True/False) # Get ID of key
db.items()                # List all entries
db.import_dict({...},overwrite=True/False)     # Import dictionary, can also overwrite existing records
db.export_dict()          # Export to dictionary
db.remove("alice")        # Delete entry
db.clear()                # Clear all
db.status()               # DB status
db.__performance__()      # Performance stats
```

---

## ⚡ Example Workflow  

```python
from shadeDB.core import ShadeDB

db = ShadeDB("./appdata.scdb", write=True)

# Insert
db.update(("alice", {"nickname": "Shade", "status": "active"}))

# Nested access
print(db.get("alice.nickname"))   # Shade

# Full context
print(db.get_context("alice"))    # {'nickname': 'Shade', 'status': 'active'}

# Export
print(db.export_dict())
```

---

## 📑 Command & Method Reference  

| Command / Method         | Description |
|---------------------------|-------------|
| `init <file>  <backup>` | Initialize DB + server |
| `use <file> <backup>`             | Switch database |
| `pull <key>.<value>`      | Fetch nested record |
| `get <key>`  <multiple>          | Fetch data  |
| `update <key>.<value>`   | Update existing record |
| `remove <key>`           | Delete entry ( Supports dot notation)|
| `ls`                     | Current database |
| `stop`                   | Stop server |
| `update(item)`           | Insert/update via Python |
| `get(key,multiple=True/False)`               | Fetch record |
| `get_context(key)`       | Full dictionary view |
| `get_by_id(id)`          | Fetch by unique ID |
| `get_id(key,multiple=True/False)`            | Return ID of key |
| `items()`                | List all entries |
| `import_dict(dict,overwrite=True/False)`      | Import bulk dict |
| `export_dict()`          | Export full dict |
| `remove(key)`            | Delete by key/ID |
| `clear()`                | Wipe database |
| `status()`               | DB status info |
| `__performance__()`      | Compile time & stats |



### 🔮 Few hints on what's to come in future updates
- **Remote mode** → optional TCP listener so shadeDB can be queried from another device (like Redis-lite networking).
- **Replication/Sync** → lightweight push/pull sync between devices.
- **Faster query returns** → implement a new algorithm to speed up query processing.
- **Custom encryption algorithm** → device based encryption algorithm.
- **Plugin system** → user-defined operations via Python modules.