from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

activities = []

@app.route("/activity", methods=["POST"])
def activity():
    data = request.get_json(silent=True) or {}

    event = data.get("event", "unknown")

    activities.append({
        "event": event,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    return jsonify({"status": "recorded"})


@app.route("/dashboard")
def dashboard():
    rows = ""

    for item in activities:
        rows += f"""
        <tr>
            <td>{item["event"]}</td>
            <td>{item["time"]}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Security Test Dashboard</title>
        <style>
            body {{
                font-family: Arial;
                margin: 40px;
            }}

            table {{
                border-collapse: collapse;
                width: 700px;
            }}

            th, td {{
                border: 1px solid #ccc;
                padding: 12px;
                text-align: left;
            }}

            th {{
                background: #eee;
            }}

            .test {{
                margin-top: 30px;
                padding: 20px;
                border: 1px solid #ddd;
            }}
        </style>
    </head>

    <body>

        <h1>Security Test Dashboard</h1>

        <table>
            <tr>
                <th>Event</th>
                <th>Time</th>
            </tr>

            {rows}

        </table>

        <div class="test">
            <h2>Dummy Test Credentials</h2>

            <p>
                Username: <b>test-user</b>
            </p>

            <p>
                Password: <b>TEST-ONLY-123</b>
            </p>
        </div>

    </body>
    </html>
    """


@app.route("/")
def home():
    return "Security test backend is running."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
