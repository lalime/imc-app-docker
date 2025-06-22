from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)

# Connexion à MySQL
db = mysql.connector.connect(
    host="mysql",
    user="root",
    password="password",
    database="imc_db"
)

cursor = db.cursor()


def calculate_bmi(weight, height):
    """Calculate the Body Mass Index (BMI) and return the category."""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


@app.route('/api/bmi', methods=['POST'])
def bmi():
    """Endpoint to calculate BMI and store the result in the database."""
    data = request.json
    weight = float(data['weight'])
    height = float(data['height'])
    
    bmi, category = calculate_bmi(weight, height)
    
    # Enregistrer dans la base de données
    query = "INSERT INTO bmi_records (weight, height, bmi, category) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (weight, height, bmi, category))
    db.commit()
    
    return jsonify({"bmi": bmi, "category": category})


@app.route('/api/bmi/history', methods=['GET'])
def history():
    """Endpoint to retrieve the BMI history from the database."""
    cursor.execute("SELECT weight, height, bmi, category FROM bmi_records")
    records = cursor.fetchall()
    return jsonify([{"weight": r[0], "height": r[1], "bmi": r[2], "category": r[3]} for r in records])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
