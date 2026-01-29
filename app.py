from flask import Flask, jsonify, request
from flask_cors import CORS
from config.database import db_config

import os

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

#__isso permite a conexão dos apps
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "message": "API FUNCIONANDO",
        "status": "online"
    })

@app.route("/test-db")
def test_datanase():
    """Endpoint para testar conexão"""
    sucess, message = db_config.test_connection()

    if sucess:
        return jsonify({
            "status": "sucess",
            "message": message,
            "database": os.getenv('DB_NAME')
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": message
        }), 500


@app.route('/db-info')
def database_info():
    """Endpoint para obter informações do banco"""
    try:
        connection = db_config.get_connection()
        if connection:
            cursor = connection.cursor()
            
            # Obter informações básicas
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            
            cursor.execute("SELECT DATABASE()")
            current_db = cursor.fetchone()[0]
            
            cursor.execute("SHOW TABLES")
            tables = [table[0] for table in cursor.fetchall()]
            
            cursor.close()
            connection.close()
            
            return jsonify({
                "mysql_version": version,
                "database": current_db,
                "tables": tables,
                "total_tables": len(tables)
            })
    except Exception as e:
        return jsonify({
            "error": f"Erro ao obter informações: {str(e)}"
        }), 500

if __name__ == '__main__':
    # Testar conexão ao iniciar
    print("🚀 Iniciando API...")
    success, message = db_config.test_connection()
    
    if success:
        print(f"✅ {message}")
        app.run(
            host='0.0.0.0',
            port=5000,
            debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
        )
    else:
        print(f"❌ {message}")
        print("🔧 Verifique suas configurações no arquivo .env")



# if __name__ == '__main__':
#     app.run(debug=True)

