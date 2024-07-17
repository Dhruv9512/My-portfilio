# app/routes.py

from flask import Blueprint, jsonify
import psycopg2
import os

main = Blueprint('main', __name__)

def connect_to_database():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        dbname=os.getenv('DB_NAME')
    )
    return conn

@main.route('/api', methods=["GET"])
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
