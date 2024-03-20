from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/cpu/")
def cpu():
    return render_template("cpu.html")

@app.route('/memory/')
def memory():
    return render_template('memory.html')

@app.route('/motherboard/')
def motherboard():
    return render_template('motherboard.html')

if __name__ == '__main__':
    app.run(debug=True)
