# -----------------------------
# 1. Import Required Libraries
# -----------------------------
import requests
from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler

# -----------------------------
# 2. Song Link
# -----------------------------
SONG_LINK = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Change to your favorite

# -----------------------------
# 3. Pushbullet Config
# -----------------------------
PUSHBULLET_API_KEY = "o.hdyfu6O6blui986xs5e3qKHANCwVmRgq"

def send_pushbullet_notification():
    data = {
        "type": "note",
        "title": "🎵 It's 5 PM - Music Time!",
        "body": f"Tap to listen: {SONG_LINK}"
    }
    response = requests.post(
        'https://api.pushbullet.com/v2/pushes',
        json=data,
        headers={'Access-Token': PUSHBULLET_API_KEY}
    )
    if response.status_code == 200:
        print("✅ Pushbullet notification sent.")
    else:
        print(f"❌ Pushbullet error: {response.status_code} - {response.text}")

# -----------------------------
# 4. Twilio Config
# -----------------------------
TWILIO_ACCOUNT_SID = "AC5756035a25c5b685ad48c7ca4ee78342"
TWILIO_AUTH_TOKEN = "[AuthToken]"
TWILIO_WHATSAPP_NUMBER = "+14155238886"  # Twilio sandbox number
YOUR_WHATSAPP_NUMBER = "+918586858027"   # Your verified WhatsApp number

def send_whatsapp_message():
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f"🎵 It's 5 PM - Time to play your song! Click here: {SONG_LINK}",
        from_=TWILIO_WHATSAPP_NUMBER,
        to=YOUR_WHATSAPP_NUMBER
    )
    print(f"✅ WhatsApp message sent. SID: {message.sid}")

# -----------------------------
# 5. Scheduler Setup
# -----------------------------
def daily_5pm_job():
    send_pushbullet_notification()
    send_whatsapp_message()

scheduler = BlockingScheduler()
scheduler.add_job(daily_5pm_job, 'cron', hour=23, minute=10)
print("📅 Scheduler started. Waiting for 5:00 PM...")
scheduler.start()
