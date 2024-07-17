from flask import Flask, jsonify,make_response
from flask_mysqldb import MySQL
from flask_cors import CORS
import traceback
import os

app = Flask(__name__)
CORS(app)
app.config['MYSQL_HOST'] = os.getenv('localhost')
app.config['MYSQL_USER'] = os.getenv('root')
app.config['MYSQL_PASSWORD'] = os.getenv('')
app.config['MYSQL_DB'] = os.getenv('ml_projects')

mysql = MySQL(app)

@app.route('/api', methods=["POST"])
def api():
    try:
        cur = mysql.connection.cursor()
        cur.execute("use ml_projects")
        cur.execute('SELECT * FROM projects')
        data = cur.fetchall()
        cur.close()

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
        traceback.print_exc()  
        return make_response(jsonify({"error": str(e)}), 500)

if __name__ == "__main__":
    DEBUG_MODE =os.getenv('DEBUG_MODE')=='True'
    app.run(debug=DEBUG_MODE)
