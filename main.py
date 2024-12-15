from flask import Flask , render_template , request , redirect ,url_for
import sys
import uuid
import jsonify , json

# Import File From folder Fungsi
sys.path.insert(0, "..")
from fungsi.itemEntry.innerMultipleClass import license_main
sys.path.insert(0, "..")
from fungsi.itemEntry.utama import Stack
sys.path.insert(0, "..")
from fungsi.itemSearch.search2 import option1
sys.path.insert(0, "..")
from fungsi.itemSorting.sorting2 import bubbleSort , selectionSort
sys.path.insert(0, "..")
from new import main

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/admin")
def admin():
    return render_template('admin/index.html')
# Sorting
@app.route("/admin/customer",methods=["GET", "POST"])
def customer():
    with open('./fungsi/itemEntry/license.json','r' ) as f:
        data = json.load(f)
    if 'license_data' in data:
        items = data['license_data']
    # Display customer here
    option = request.form.get("sort_key", "id")  

    sorting=bubbleSort(data, option)
    return render_template(
        'admin/jobs/customer.html',
        option = option,
        sorting = sorting['license_data'] ,
        items = items
    )
@app.route("/admin/product")
def product():
    return render_template('admin/jobs/product.html')

# Add Product
@app.route("/admin/product/add_product", methods=['GET', 'POST'])
def add_product():
    with open('./fungsi/license-data.json') as f:
        data = json.load(f)
    if 'license' in data:
        items = data['license']
    option_data = [
                {'selected_option': "Trial"},
                {'selected_option':"Subscribe"},
                {'selected_option':"Forever"}
            ]  
    return render_template('admin/jobs/add_product.html',items=items ,option_data=option_data)
@app.route("/admin/product/add_product/process", methods=['POST', 'GET'])
def add_product_process():
    if request.method == 'POST':
        name = request.form['fullname']
        subs = request.form.get('subscribe_select')
        token =  str(uuid.uuid4())
        license = request.form['license_type']
        license_type = int(license)   
        main(name, subs, token, license_type)
    else :
        return redirect(url_for("index"))
    return render_template("admin/jobs/success.html")
# Searching Product
@app.route('/admin/search/result', methods=['GET','POST'])
def search():
    with open('./fungsi/itemEntry/license.json','r') as f:
        data =json.load(f)
        
    if 'license_data' in data:
        wow = data['license_data']
    if request.method == 'POST':
        searchs= request.form['search']
        result = option1(wow, 'name' ,searchs)
    else :
        return redirect(url_for("header"))
    return render_template('admin/jobs/search.html',item=result,searchs=searchs)

@app.route("/admin/license")
def license():
    with open('./fungsi/license-data.json') as f:
        data = json.load(f)
    if 'license' in data:
        items = data['license']
    return render_template('admin/jobs/license.html',items=items)
@app.route("/admin/log")
def log():
    return render_template('admin/jobs/activity-logs.html')
@app.route("/admin/user")
def user():
    return render_template('admin/jobs/users.html')
@app.route("/admin/setting")
def setting():
    return render_template('admin/jobs/settings.html')
# Fungsi 
@app.route("/admin/add")
def create():
    # Masukkan fungsi berlangganan disini
    return render_template('admin/crud/create.html')
@app.route("/admin/display")
def display():
    # Import JSON
    # Process to get data from column in JSON Data
    # Display JSON into Table
    return render_template('admin/crud/display.html')
@app.route("/admin/edit")
def edit():
    # Input token or Name
    # Get data
    # Input new data
    # Rewire data
    return render_template('admin/crud/edit.html')
@app.route("/admin/delete")
def delete():
    # Input token
    # truncate data
    return render_template('admin/crud/delete.html')
if __name__ == "__main__":
    app.run(debug=True)