from flask import Flask, render_template,request, redirect

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

def store_data(values_list):
    row=values_list[0]
    for i in range(1,len(values_list)):
        row=row+","+values_list[i]
    with open("/Users/brunolopezgarcia/Documents/Python/Flask/main_server/database.txt", mode="a") as my_file:
        my_file.write('\n'+row)

@app.route("/thank.html", methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data=request.form.to_dict()
        store_data(list(data.values()))
        return render_template('thank.html')

    return 'Something went wrong'

#@app.route("/<string:page_name>")
#def html_page(page_name):
#    return render_template(page_name)


#def store_data(values_list):
#    row=values_list[0]
#    for i in range(1,len(values_list)):
#        row=row+","+values_list[i]
#    with open("/Users/brunolopezgarcia/Documents/Python/Flask/web_server/database.txt", mode="a") as my_file:
#        my_file.write('\n'+row)

#@app.route('/#thank', methods=['POST', 'GET'])
#def submit_form():
#    if request.method == 'POST':
#        data=request.form.to_dict()
#        store_data(list(data.values()))
#        return redirect('#thank')

#    return 'Something went wrong'
