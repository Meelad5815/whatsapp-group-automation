"""Configuration file for WhatsApp Group Automation

Add your group IDs and customize messages here.
"""

# List of WhatsApp group IDs
# To find group ID:
# 1. Open WhatsApp Web (web.whatsapp.com)
# 2. Open the group
# 3. Look at the URL: https://web.whatsapp.com/send?phone=XXXXXXXXXXX
# 4. The number is your group ID

GROUPS = [
    # Add your group IDs here
    # Example: "1234567890-1234567890",
]

# Default message to send
DEFAULT_MESSAGE = """
🤖 Automated Message

This is an automated post from the WhatsApp automation script.

Customize this message in config.py!
"""

# Scheduling settings
SCHEDULE_ENABLED = False
SCHEDULE_HOUR = 9  # 24-hour format
SCHEDULE_MINUTE = 0

# Advanced settings
WAIT_TIME = 15  # Seconds to wait before sending
CLOSE_TAB = True  # Close browser tab after sending
