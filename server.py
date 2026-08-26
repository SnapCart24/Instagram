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
    html = """
    <html>
    <head>
        <title>Security Test Dashboard</title>
        <style>
            body {
                font-family: Arial;
                margin: 40px;
            }

            table {
                border-collapse: collapse;
                width: 700px;
            }

            th, td {
                border: 1px solid #ccc;
                padding: 10px;
            }

            th {
                background: #eee;
            }
        </style>
    </head>

    <body>

        <h1>Security Test Activity</h1>

        <table>
            <tr>
                <th>Event</th>
                <th>Time</th>
            </tr>
    """

    for item in activities:
        html += f"""
            <tr>
                <td>{item['event']}</td>
                <td>{item['time']}</td>
            </tr>
        """

    html += """
        </table>

    </body>
    </html>
    """

    return html


@app.route("/")
def home():
    return "Activity server is running."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
