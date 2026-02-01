from web import app



if __name__ == '__main__':
    app.run(debug=True)
    # Testar conexão ao iniciar
    # print("🚀 Iniciando API...")
    # success, message = db_config.test_connection()
    
    # if success:
    #     print(f"✅ {message}")
    #     app.run(
    #         host='0.0.0.0',
    #         port=5000,
    #         debug=os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    #     )
    # else:
    #     print(f"❌ {message}")
    #     print("🔧 Verifique suas configurações no arquivo .env")



# if __name__ == '__main__':
#     app.run(debug=True)

