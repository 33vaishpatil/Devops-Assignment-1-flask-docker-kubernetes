from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body {
                background-color: #f4f6f8;
                font-family: Arial;
                text-align: center;
                padding-top: 100px;
            }
            .card {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                display: inline-block;
            }
            h1 {
                color: #2c3e50;
            }
            p {
                color: #555;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Flask App Running</h1>
            <p>Welcome Vaishnavi 👋</p>
            <p>Status: <b style="color:green;">UP</b></p>
            <p>Version: v2</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
