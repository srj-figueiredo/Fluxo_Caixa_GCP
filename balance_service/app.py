import google.cloud.pubsub_v1 as pubsub
import pyodbc

# Função para consumir eventos do Google Pub/Sub
def consume_event(event_data):
    # Aqui seria a lógica para atualizar o saldo no banco de dados
    print(f"Processing event: {event_data}")
    # Atualização do saldo no banco de dados
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=localhost;DATABASE=carrefour_db;UID=user;PWD=password')
    cursor = conn.cursor()
    cursor.execute("UPDATE saldo SET value = value + ? WHERE date = CURRENT_DATE", (event_data['value'],))
    conn.commit()
    conn.close()

def listen_to_pubsub():
    subscriber = pubsub.SubscriberClient()
    subscription_path = subscriber.subscription_path('your-gcp-project-id', 'launch_subscription')

    def callback(message):
        print(f"Received message: {message.data}")
        consume_event(message.data)
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

if __name__ == "__main__":
    listen_to_pubsub()
