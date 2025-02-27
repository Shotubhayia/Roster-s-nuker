# Rostu Nuker Bot - Termux Setup

## 馃搶 Prerequisites
Before running the bot, ensure you have **Termux** installed.

## 馃敡 Installation Steps

### 1锔忊儯 Update and Install Required Packages
```bash
pkg update && pkg upgrade -y
pkg install python git unzip -y
pip install --upgrade pip
```

### 2锔忊儯 Clone the GitHub Repository
Replace `YOUR_GITHUB_REPO_URL` with your actual GitHub repository link:
```bash
git clone YOUR_GITHUB_REPO_URL rostu_nuker
cd rostu_nuker
```

### 3锔忊儯 Install Required Python Libraries
```bash
pip install -r requirements.txt
```

### 4锔忊儯 Configure Your Bot Token
Edit the `config.py` file and add your **Discord Bot Token**:
```bash
nano config.py
```
Save the file by pressing `CTRL + X`, then `Y`, and `ENTER`.

### 5锔忊儯 Run the Bot
```bash
python bot.py
```

## 鉂� Need Help?
If you encounter any issues, feel free to ask for support!