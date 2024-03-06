import sqlite3
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()


# with open("stats.json", "w") as outfile:
# json.dump(stats, outfile)
connection = sqlite3.connect(os.getenv("DB_URL"), check_same_thread=False)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS statisticsRPSSL (player INTEGER, computer INTEGER, draw INTEGER, "
                   "rock INTEGER, paper INTEGER, scissors INTEGER, spock INTEGER, lizard INTEGER)")

@app.route('/saveStats', methods=['POST'])
def saveStats():
    stats = request.get_json()
    cursor.execute("SELECT * FROM statisticsRPSSL")

    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO statisticsRPSSL VALUES (:player, :computer, :draw, :rock, :paper, :scissors, :spock, :lizard)", stats)
    else:
        cursor.execute("UPDATE statisticsRPSSL SET player = :player, computer = :computer, draw = :draw, rock = :rock, "
                       "paper = :paper,  scissors = :scissors, spock = :spock, lizard = :lizard", stats)
    connection.commit()
    return jsonify({"message": "Success"})

@app.route('/getStats', methods=['GET'])
def getStats():
    cursor.execute("SELECT * FROM statisticsRPSSL LIMIT 1")
    stats = cursor.fetchone()
    print(stats)
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True)

