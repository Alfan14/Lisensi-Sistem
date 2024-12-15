import itertools
import os
import json
import datetime
import uuid

class Node:
    id_obj = itertools.count()
    def __init__(self ,name,subs,license_type,activated , expired ,token, active ,license):
        self.id =next(Node.id_obj)
        self.user_name = name
        self.type_subscribe = subs 
        self.type_off_license = license_type
        self.activated_license = activated 
        self.expired_license = expired
        self.token_license = token
        self.active_or_not = active 
        self.license = license
class Queue:
    def __init__(self,json_file='./fungsi/itemEntry/license.json'):
        self._total_aktivasi = 0 
        self.json_file =json_file 
        self.load_dari_json()

    def isEmpty(self):
            return self.json_file is None
    
    def enqueue(self,name,subs,license_type,activated , expired ,token, active , license):
        print("From enque.py",name, subs, license_type, token , activated, expired, active , license)
        
        aktivasi_baru = Node(name,subs,license_type,activated , expired ,token, active , license)
        self.aktivasi_baru = aktivasi_baru
        sekarang = self.aktivasi_baru
        
        aktivasi= {
            'id':sekarang.id,
            'name':sekarang.user_name,
            'type_of_subscribe':sekarang.type_subscribe,
            'type_off_license':sekarang.type_off_license,
            'aktivasi_token':sekarang.token_license,
            'activated_at':sekarang.activated_license,
            'expires_at':sekarang.expired_license,
            'active' :sekarang.active_or_not,
            'license':sekarang.license
        }
        
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        
        
        if 'license_data' not in data:
            data['license_data'] = []
        
        data['license_data'].append(aktivasi)

        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=4)
        print("Hore data berhasil masuk!!")
    def load_dari_json(self):
        if not os.path.exists(self.json_file) or os.path.getsize(self.json_file) == 0:
            with open(self.json_file, 'w') as f:
                json.dump({"license_data": []}, f, indent=4)
        else:
            try:
                with open(self.json_file, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error reading JSON file: {e}")
                # Optionally reset the file content if error occurs
                with open(self.json_file, 'w') as f:
                    json.dump({"license_data": []}, f, indent=4)

                
if __name__ =='__main__':
    # trial_v = 0
    # token = str(uuid.uuid4())
    # name = 'Alan'
    # subs = 'Trial'
    # license_type = 1
    # current_trial = datetime.datetime.now()
    # expired = current_trial + datetime.timedelta(days=trial_v)
    # activated = current_trial
    # active = True
    
    import sys
    sys.path.insert(0, "..")
    from itemEntry.berlangganan import name, subs, license_type, activated, expired, token
    active = True
    
    q = Queue()
    q.enqueue(name,subs,license_type,activated , expired ,token, active)
