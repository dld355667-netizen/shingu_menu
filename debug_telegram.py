import urllib.request
import json
import ssl

TOKEN = '8743054120:AAH838bI6-ZfoN_zTND-uWnK9Y5kuDHGNrE'
CHAT_ID = '5690339677'

def debug_telegram():
    context = ssl._create_unverified_context()
    
    # 1. Test getMe
    print("--- Testing getMe ---")
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/getMe"
        with urllib.request.urlopen(url, context=context) as response:
            print(f"getMe success: {response.read().decode()}")
    except Exception as e:
        print(f"getMe failed: {e}")

    # 2. Test sendMessage
    print("\n--- Testing sendMessage ---")
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": "Final debugging attempt"
    }
    data_json = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=data_json, headers={'Content-Type': 'application/json'})
    
    try:
        with urllib.request.urlopen(req, context=context) as response:
            print(f"sendMessage success: {response.read().decode()}")
    except Exception as e:
        print(f"sendMessage failed: {e}")
        if hasattr(e, 'read'):
            print(f"Error details: {e.read().decode()}")

if __name__ == "__main__":
    debug_telegram()
