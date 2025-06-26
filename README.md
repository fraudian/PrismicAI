# Prismic CLI Chatbot

🧠 **Prismic CLI Chatbot** is a command-line interface AI chatbot powered by [Groq's LLaMA 3 API](https://groq.com/).

This project is a **terminal-based port of** [`mishl-dev/Discord-AI-Chatbot`](https://github.com/mishl-dev/Discord-AI-Chatbot), reimagined to run entirely in your terminal with no Discord dependencies.

---

### ✨ Features

- 💬 **Natural Conversations** using LLaMA3-70B via the Groq API.
- ⌨️ **Terminal-only interface** — no GUI or web interface required.
- 🧠 **Persistent verification logic** using local JSON storage.
- 🔁 **Polling loop** to process and respond to messages as they come in.

---

### 📦 About This Project

Originally built for Discord, this version brings the same AI personality into a lightweight, no-frills CLI chatbot for personal or experimental use.

---

### 🛠 Requirements

- Python 3.10+
- Groq API key
- `.env` file for your Groq credentials

---

### 🔧 Setup

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt

2. Login to **https://console.groq.com/home** preferably using Github.

3. Create a Key from **https://console.groq.com/keys**

4. Then Edit `.env` and replace `GROQ_API_KEY` with your GroqAPI Key

# 📝 License
MIT License – free to use and modify with attribution.

#
Made with ❤️ by fraudian
