import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="It's Time to drink Water!",
            message="Paani pi le bhai.",
            app_name="Water Reminder",
    app_icon="C:/Users/HP/Desktop/Drink_Water/icon.ico",
            timeout=10
        )
        time.sleep(60*60)  