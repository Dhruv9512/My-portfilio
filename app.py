from flask import Flask, jsonify,render_template
from flask_cors import CORS
import psycopg2
import os




app = Flask(__name__)
CORS(app)
app.config['POSTGRES_HOST'] = os.getenv('DB_HOST')
app.config['POSTGRES_USER'] = os.getenv('DB_USER')
app.config['POSTGRES_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['POSTGRES_DB'] = os.getenv('DB_NAME')

def connect_to_database():
    conn = psycopg2.connect(
        host=app.config['POSTGRES_HOST'],
        user=app.config['POSTGRES_USER'],
        password=app.config['POSTGRES_PASSWORD'],
        dbname=app.config['POSTGRES_DB']
    )
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api', methods=["GET"])
def api():
    try:
        conn = connect_to_database()
        cur = conn.cursor()
        cur.execute('SELECT * FROM projects')
        data = cur.fetchall()
        cur.close()
        conn.close()

        # Structure data into JSON format
        json_data = []
        for item in data:
            json_data.append({
                'Id': item[0],
                'Title': item[1],
                'Description': item[2],
                'GithubLink': item[3],
                'WebsiteLink': item[4]
            })

        return jsonify(json_data)

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    DEBUG_MODE =os.getenv('DEBUG_MODE')=='True'
    app.run(debug=DEBUG_MODE)
