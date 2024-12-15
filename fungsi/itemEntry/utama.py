import os
import json
import sys
import itertools
class Node :
    id_obj = itertools.count()
    def __init__(self, type ,desc, by ,sa ,nc ,nd):
        self.id =next(Node.id_obj)
        self.description = desc
        self.type_off_license = type
        self.type_by = by
        self.type_sa = sa
        self.type_nc = nc
        self.type_nd = nd
        self.next = None
class Stack:
    def __init__(self,json_file='./fungsi/itemEntry/license.json'):
        self.head = None
        self.json_file = json_file
        self._total_data = 0
        self.load_json()
    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        return {
            "type": self.head.type_off_license,
            "desc": self.head.description,
            "by": self.head.type_by,
            "sa": self.head.type_sa,
            "nc": self.head.type_nc,
            "nd": self.head.type_nd
        }
    def size(self):
        return self._total_data
    # Parameter for saving data into JSON
    def isEmpty(self):
        return self.head is None
    def enstack(self,type ,desc, by ,sa ,nc ,nd):
        print("From utama.py",type ,desc, by ,sa ,nc ,nd)
        add_data = Node(type ,desc, by ,sa ,nc ,nd)
        add_data.next = self.head
        self.head = add_data
        self._total_data += 1
        self.save_to_json()
    def destack(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove_data = self.head
        self.head = self.head.next
        self._total_data -= 1
        self.save_to_json()
    def save_to_json(self):
        with open(self.json_file, 'r+') as file:
            data = json.load(file)
            
            current = self.head
            while current:
                if data['license_data']:
                    last_entry = data['license_data'][-1]
                    last_entry["license"] = {
                        'type': current.type_off_license,
                        'desc': current.description,
                        'by': current.type_by,
                        'sa': current.type_sa,
                        'nc': current.type_nc,
                        'nd': current.type_nd
                    }
                current = current.next
            
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()  
    print("Berhasil diupdate!")
    # Parameter to check if 'data.json' it's exist if not create 'data.json' with blanket {'license_data'}     
    def load_json(self):
        if not os.path.exists(self.json_file) or os.path.getsize(self.json_file) == 0:
            with open(self.json_file, 'w') as f:
                json.dump({"license_data": []}, f, indent=4)

