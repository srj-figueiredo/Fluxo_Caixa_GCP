from flask import Flask, request, jsonify
import pyodbc
import google.cloud.pubsub_v1 as pubsub

app = Flask(__name__)

# Configuração de conexão com o banco de dados SQL Server
def get_db_connection():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=localhost;DATABASE=carrefour_db;UID=user;PWD=password')
    return conn

# Função para publicar evento no Google Pub/Sub
def publish_event(event_data):
    publisher = pubsub.PublisherClient()
    topic_path = publisher.topic_path('your-gcp-project-id', 'launch_topic')
    publisher.publish(topic_path, event_data.encode('utf-8'))

@app.route('/launch', methods=['POST'])
def launch_value():
    data = request.get_json()
    value = data['value']
    transaction_type = data['type']

    # Inserir dados no banco de dados SQL Server
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (value, type) VALUES (?, ?)", (value, transaction_type))
    conn.commit()
    conn.close()

    # Publicar evento para atualizar saldo
    publish_event(f"Transaction: {value}, Type: {transaction_type}")

    return jsonify({'status': 'success', 'message': 'Transaction recorded successfully'})

if __name__ == '__main__':
    app.run(debug=True)
