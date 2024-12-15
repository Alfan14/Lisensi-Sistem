import datetime
import json
import uuid
import sys
import textwrap

sys.path.insert(0, "..")
from fungsi.itemEntry.expired.enque import Queue
sys.path.insert(0, "..")
from fungsi.itemEntry.innerMultipleClass import license_main
sys.path.insert(0, "..")
from fungsi.itemEntry.utama import Stack

p = Stack()
q = Queue()

def wrap_text(text, width=50):
    return "\n".join(textwrap.wrap(text, width=width))
def main(name, subs, token, license_type):
    try:
        if int(license_type) <= 6:
            
            current_time = datetime.datetime.now()
            activated, expired = None, None
            active = False
        
        if subs.lower() == 'trial':
            trial_duration = 7
            activated = current_time
            expired = current_time + datetime.timedelta(days=trial_duration)
            active = True
        elif subs.lower() == 'subscribe':
            subscribe_duration = 30
            activated = current_time
            expired = current_time + datetime.timedelta(days=subscribe_duration)
            active = True
        elif subs.lower() == 'forever':
            forever_duration = 36500  
            activated = current_time
            expired = current_time + datetime.timedelta(days=forever_duration)
            active = True
        else:
            print("Invalid subscription type.")
            return

        license_data = license_main(license_type)

        unified_data = {
            "name": name,
            "type_of_subscribe": subs,
            "type_of_license": license_type,
            "activation_token": token,
            "activated_at": activated.strftime("%Y-%m-%d %H:%M:%S"),
            "expires_at": expired.strftime("%Y-%m-%d %H:%M:%S"),
            "active": active,
            "license": None,
        }

        q.enqueue(
            name=unified_data["name"],
            subs=unified_data["type_of_subscribe"],
            license_type=unified_data["type_of_license"],
            activated=unified_data["activated_at"],
            expired=unified_data["expires_at"],
            token=unified_data["activation_token"],
            active=unified_data["active"],
            license=unified_data["license"],
        )

        p.enstack(*license_data)

        license_details = p.peek()

        if license_details:
            unified_data["license"] = {
                "type": license_details.get("type"),
                "desc": license_details.get("desc"),
                "by": license_details.get("by"),
                "sa": license_details.get("sa"),
                "nc": license_details.get("nc"),
                "nd": license_details.get("nd"),
            }

        print(json.dumps(unified_data, indent=4))
        print("SELESAI")
    except Exception as e:
        print(f"An error occurred: {e}")
