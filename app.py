from flask import Flask, request, Response, render_template, redirect

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/search")
def search():
    args = request.args.get("search")
    return redirect(f"https://programmingdoor.com/?s={args}")

if __name__ == "__main__":
    app.run()