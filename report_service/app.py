from flask import Flask, request, jsonify
import pyodbc
import csv
import os

app = Flask(__name__)

# Função para conectar ao banco de dados SQL Server
def get_db_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=localhost;DATABASE=carrefour_db;UID=user;PWD=password')
    return conn

@app.route('/generate_report', methods=['GET'])
def generate_report():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Consultar transações no banco de dados
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE date BETWEEN ? AND ?", (start_date, end_date))
    transactions = cursor.fetchall()

    # Gerar relatório CSV
    report_file = f"report_{start_date}_to_{end_date}.csv"
    with open(report_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Value', 'Type', 'Date'])
        for transaction in transactions:
            writer.writerow(transaction)

    conn.close()

    return jsonify({'status': 'success', 'message': 'Report generated', 'report_file': report_file})

if __name__ == '__main__':
    app.run(debug=True)
