from api import app, sucess


# print(sucess)
if __name__ == '__main__':
    # Testar conexão ao iniciar
    # print("🚀 Iniciando API...")
    # success, message = db_config.test_connection()
    
    if sucess:
        app.run(
            host='0.0.0.0',
            port= sucess['port'],
            debug=sucess['debug']
        )
    else:
        
        print("🔧 Verifique suas configurações no arquivo .env")



# if __name__ == '__main__':
#     app.run(debug=True)

