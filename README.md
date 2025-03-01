# ROSTER NUKER BOT

**A Powerful Discord Nuker Bot!**  
**Features:**  
+ Delete all channels  
+Delete all roles  
+ Change server name  
+ Create and spam channels  
+ Mass ban members  

---

## Installation (Termux & Terminal)

### ** Install Requirements**
#### **For Termux (Android)**
```bash
pkg update && pkg upgrade
pkg install python git
pip install -r requirements.txt
```

#### **For Terminal (Windows/Linux)**
```bash
git clone https://github.com/your-repo/roster-nuker.git
cd roster-nuker
pip install -r requirements.txt
```

---

## **Configuration**
Edit the `config.json` file and add your bot token:

```json
{
    "TOKEN": "YOUR_BOT_TOKEN",
    "GUILD_ID": "YOUR_SERVER_ID",
    "CHANNEL_NAME": "nuked-channel",
    "WEBHOOK_MESSAGE": "Server Nuked!",
    "SPAM_SPEED": 1,
    "CHANNEL_BATCH": 5
}
```

---

##  **How to Run**
### **For Termux**
```bash
python roster.py
```
### **For Terminal (Windows/Linux)**
```bash
python3 roster.py
```

---