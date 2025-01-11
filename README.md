# Description
Ini adalah projek akhir semester 3 matakuliah struktur data menggunakan Flask dengan sistem kontrak lisensi.

# Penggunaan :
windows-> powershell

git clone https://github.com/Alfan14/Lisensi-Sistem.git <Nama_Projekmu>

cd <Nama_Projekmu>

pip install venv
python -m venv <nama_folder_venv>
./nama_folder_venv/Scripts/activate.ps1   
$env:FLASK_APP = "main.py"    
$env:FLASK_ENV = "development"
$env:FLASK_DEBUG=1
flask run
