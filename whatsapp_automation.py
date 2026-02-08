"""WhatsApp Group Automation Script

This script provides automated posting functionality for WhatsApp groups.
Supports both immediate and scheduled messaging.
"""

import pywhatkit as kit
import pyautogui
import time
from datetime import datetime, timedelta
import logging
from config import GROUPS, DEFAULT_MESSAGE

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('whatsapp_automation.log'),
        logging.StreamHandler()
    ]
)

class WhatsAppGroupAutomation:
    """Class to handle WhatsApp group automation tasks"""
    
    def __init__(self, wait_time=15, tab_close=True):
        """
        Initialize WhatsApp automation
        
        Args:
            wait_time (int): Wait time before sending message (seconds)
            tab_close (bool): Close tab after sending message
        """
        self.wait_time = wait_time
        self.tab_close = tab_close
        logging.info("WhatsApp Group Automation initialized")
    
    def send_message_now(self, group_id, message):
        """
        Send message to WhatsApp group immediately
        
        Args:
            group_id (str): WhatsApp group ID with country code (e.g., '+1234567890-1234567890')
            message (str): Message content to send
        """
        try:
            logging.info(f"Sending message to group: {group_id}")
            
            # Calculate time 1 minute from now
            now = datetime.now()
            send_time = now + timedelta(minutes=1)
            hour = send_time.hour
            minute = send_time.minute
            
            # Send message using pywhatkit
            kit.sendwhatmsg_to_group(
                group_id=group_id,
                message=message,
                time_hour=hour,
                time_min=minute,
                wait_time=self.wait_time,
                tab_close=self.tab_close
            )
            
            # Wait for browser to open and message to be typed
            time.sleep(self.wait_time + 5)
            
            # Press Enter to send
            pyautogui.press('enter')
            
            logging.info(f"Message sent successfully to group: {group_id}")
            return True
            
        except Exception as e:
            logging.error(f"Failed to send message to group {group_id}: {str(e)}")
            return False
    
    def schedule_message(self, group_id, message, hour, minute):
        """
        Schedule message to WhatsApp group for specific time
        
        Args:
            group_id (str): WhatsApp group ID
            message (str): Message content
            hour (int): Hour in 24-hour format (0-23)
            minute (int): Minute (0-59)
        """
        try:
            logging.info(f"Scheduling message to group: {group_id} at {hour}:{minute}")
            
            kit.sendwhatmsg_to_group(
                group_id=group_id,
                message=message,
                time_hour=hour,
                time_min=minute,
                wait_time=self.wait_time,
                tab_close=self.tab_close
            )
            
            # Wait and press enter
            time.sleep(self.wait_time + 5)
            pyautogui.press('enter')
            
            logging.info(f"Scheduled message sent successfully")
            return True
            
        except Exception as e:
            logging.error(f"Failed to schedule message: {str(e)}")
            return False
    
    def send_to_multiple_groups(self, group_ids, message):
        """
        Send same message to multiple WhatsApp groups
        
        Args:
            group_ids (list): List of WhatsApp group IDs
            message (str): Message content
        """
        results = []
        
        for group_id in group_ids:
            result = self.send_message_now(group_id, message)
            results.append({'group_id': group_id, 'success': result})
            
            # Wait between messages to avoid rate limiting
            if len(group_ids) > 1:
                time.sleep(60)  # Wait 1 minute between groups
        
        return results
    
    def send_image_to_group(self, group_id, image_path, caption=""):
        """
        Send image to WhatsApp group
        
        Args:
            group_id (str): WhatsApp group ID
            image_path (str): Path to image file
            caption (str): Optional image caption
        """
        try:
            logging.info(f"Sending image to group: {group_id}")
            
            # Calculate time
            now = datetime.now()
            send_time = now + timedelta(minutes=1)
            
            kit.sendwhats_image(
                receiver=group_id,
                img_path=image_path,
                caption=caption,
                wait_time=self.wait_time,
                tab_close=self.tab_close,
                time_hour=send_time.hour,
                time_min=send_time.minute
            )
            
            logging.info(f"Image sent successfully")
            return True
            
        except Exception as e:
            logging.error(f"Failed to send image: {str(e)}")
            return False


def main():
    """Main function to demonstrate usage"""
    
    # Initialize automation
    automation = WhatsAppGroupAutomation(wait_time=15, tab_close=True)
    
    # Example 1: Send message to single group immediately
    # Replace with your actual group ID (found in group invite link)
    # group_id = "YOUR_GROUP_ID"  # Format: XXXXXXXXXXX-XXXXXXXXXX
    # automation.send_message_now(group_id, "Hello from automated script!")
    
    # Example 2: Schedule message for specific time
    # automation.schedule_message(group_id, "Scheduled message", hour=14, minute=30)
    
    # Example 3: Send to multiple groups
    # groups = ["GROUP_ID_1", "GROUP_ID_2"]
    # automation.send_to_multiple_groups(groups, "Message to all groups")
    
    # Example 4: Using config file
    if GROUPS:
        automation.send_to_multiple_groups(GROUPS, DEFAULT_MESSAGE)
    else:
        logging.warning("No groups configured in config.py")
        print("\nPlease configure your groups in config.py before running!")
        print("\nTo get Group ID:")
        print("1. Open WhatsApp Web")
        print("2. Open the group")
        print("3. Check the URL: https://web.whatsapp.com/send?phone=XXXXXXXXXXX")
        print("4. The numbers after 'phone=' is your group ID")


if __name__ == "__main__":
    main()
