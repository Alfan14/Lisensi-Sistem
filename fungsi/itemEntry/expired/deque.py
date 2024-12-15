import json

def hapus_aktivasi() :
    search = input("Masukkan tokenmu:")
    data  = json.load(open("license.json", 'r' ))
    new1 = data['license_data']
    for item in new1:
        if item.get('aktivasi_token')== search: # delete object with token=search
            new1.remove(item)
            break
    # Save the updated list back to the file 
    with open('license.json', 'w') as f:
        json.dump(data, f)
            
if __name__ == '__main__':     
    hapus_aktivasi()
            
