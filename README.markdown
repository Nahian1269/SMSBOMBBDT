

> **⚠️ Legal and Ethical Warning**: RedBomberBD is for **authorized testing only**. Sending unsolicited SMS or spamming without explicit consent from the phone number owner and API providers is **illegal** and **unethical**, potentially violating Bangladesh laws and API terms of service. Misuse may lead to legal consequences, account bans, or service disruptions. The developer is not responsible for any misuse.

## Key Features
- Sends multiple OTP requests to Bangladesh-specific APIs for SMS bombing tests.
- Simple command-line interface optimized for Termux on Android.
- Configurable request limits to simulate SMS spam responsibly.
- Open-source and lightweight, requiring minimal dependencies.



```bash
pkg update -y && pkg upgrade -y
pkg install python -y
pkg install git -y
git clone https://github.com/Nahian1269/SMSBOMBBDT.git
cd RedBomberBD
pip install requests colorama
python redbombbd.py
```

### Prerequisites
- **Termux**: Install from [F-Droid](https://f-droid.org/en/packages/com.termux/) for the latest version.
- **Internet Connection**: Needed to clone the repository and install dependencies.
- **Storage Permission** (optional): Run `termux-setup-storage` for file access.

