import json
from flask import Flask, request, render_template
app = Flask("3d Asset")

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        "name": request.form["name"],
        "polycount": request.form["polycount"],
        "id": request.form["id"],
        "user": request.form["user"]
            }
    with open("asset_data.json","w") as json_file:
        json.dump(data, json_file)

    return "Data saved correctly"

@app.route('/')
def index():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)


