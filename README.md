# WhatsApp Group Automation 🤖

Automate WhatsApp group messaging with Python. Send messages, schedule posts, and manage multiple groups effortlessly.

## Features ✨

- ✅ Send messages to WhatsApp groups automatically
- ✅ Schedule messages for specific times
- ✅ Send to multiple groups at once
- ✅ Send images with captions
- ✅ Logging and error handling
- ✅ Easy configuration

## Prerequisites 📋

- Python 3.7 or higher
- WhatsApp account
- Internet connection
- Chrome or Firefox browser

## Installation 🚀

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Meelad5815/whatsapp-group-automation.git
   cd whatsapp-group-automation
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your groups:**
   - Open `config.py`
   - Add your WhatsApp group IDs
   - Customize your messages

## How to Get Group ID 🔍

1. Open [WhatsApp Web](https://web.whatsapp.com)
2. Open the group you want to automate
3. Look at the browser URL
4. Extract the group ID from the URL format: `https://web.whatsapp.com/send?phone=XXXXXXXXXXX`
5. Copy the numbers after `phone=` - this is your group ID

## Usage 💻

### Basic Usage

```python
from whatsapp_automation import WhatsAppGroupAutomation

# Initialize
automation = WhatsAppGroupAutomation()

# Send message now
automation.send_message_now("GROUP_ID", "Hello World!")
```

### Schedule Message

```python
# Schedule for 2:30 PM
automation.schedule_message(
    group_id="GROUP_ID",
    message="Scheduled message",
    hour=14,
    minute=30
)
```

### Send to Multiple Groups

```python
groups = ["GROUP_ID_1", "GROUP_ID_2", "GROUP_ID_3"]
automation.send_to_multiple_groups(groups, "Message for all")
```

### Send Image

```python
automation.send_image_to_group(
    group_id="GROUP_ID",
    image_path="/path/to/image.jpg",
    caption="Check this out!"
)
```

## Configuration ⚙️

Edit `config.py` to customize:

- **GROUPS**: List of group IDs to target
- **DEFAULT_MESSAGE**: Default message template
- **SCHEDULE_ENABLED**: Enable/disable scheduling
- **WAIT_TIME**: Browser wait time (seconds)
- **CLOSE_TAB**: Auto-close browser tab after sending

## Running the Script 🎯

```bash
python whatsapp_automation.py
```

First run will:
1. Open WhatsApp Web
2. Prompt you to scan QR code (if not logged in)
3. Send messages according to your configuration

## Important Notes ⚠️

- **First Use**: You'll need to scan the WhatsApp Web QR code on first run
- **Stay Logged In**: Keep WhatsApp Web logged in for automation to work
- **Rate Limiting**: Script waits 60 seconds between messages to avoid blocks
- **Browser Focus**: Don't use your computer while messages are being sent
- **Compliance**: Use responsibly and comply with WhatsApp's Terms of Service

## Automation with Cron (Linux/Mac) ⏰

To run automatically at scheduled times:

```bash
# Edit crontab
crontab -e

# Add this line to run daily at 9 AM:
0 9 * * * /usr/bin/python3 /path/to/whatsapp_automation.py
```

## Automation with Task Scheduler (Windows) 🪟

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily, weekly, etc.)
4. Action: Start a program
5. Program: `python.exe`
6. Arguments: `C:\path\to\whatsapp_automation.py`

## Troubleshooting 🔧

### "PyAutoGUI cannot locate the enter key"
- Make sure WhatsApp Web is in focus
- Increase `wait_time` in config

### "Failed to send message"
- Check your internet connection
- Verify group ID is correct
- Ensure you're logged into WhatsApp Web
- Check if you're a member of the group

### "Browser doesn't open"
- Install/update Chrome or Firefox
- Check if WhatsApp Web works manually

## Logging 📝

All activities are logged to `whatsapp_automation.log`:
- Successful sends
- Failed attempts
- Error messages
- Timestamps

## Security & Privacy 🔒

- Never share your `config.py` with configured group IDs
- Don't commit sensitive data to public repositories
- Keep your API credentials secure
- Use `.gitignore` to exclude config files

## Limitations ⚡

- Requires WhatsApp Web to be accessible
- Cannot send to groups you're not a member of
- Subject to WhatsApp's rate limits
- Requires active internet connection
- Browser must be in focus during sending

## WhatsApp Business API Alternative 🏢

For enterprise solutions, consider:
- [WhatsApp Business Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api) (Official, supports groups since Oct 2025)
- [Whapi.cloud](https://whapi.cloud) - Third-party API provider
- [WABA Connect](https://wabaconnect.com) - Business API platform

## Contributing 🤝

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License 📄

MIT License - feel free to use this project for personal or commercial purposes.

## Disclaimer ⚖️

This tool is for educational purposes. Use responsibly and in compliance with:
- WhatsApp Terms of Service
- Local regulations
- Privacy laws
- Anti-spam policies

**Note**: Excessive automation may result in your WhatsApp account being banned. Use at your own risk.

## Support 💬

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Read the troubleshooting section

## Roadmap 🗺️

- [ ] GUI interface
- [ ] Message templates library
- [ ] Bulk image sending
- [ ] Contact management
- [ ] Analytics dashboard
- [ ] Cloud deployment guides

---

**Made with ❤️ for automation enthusiasts**

Star ⭐ this repo if you find it helpful!
