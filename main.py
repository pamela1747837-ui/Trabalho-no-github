import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.183",
    port=3309,
    user="root",
    password="root123",
    detabase="anny_e_pamela"
)
def inserir_usuario(nome, email, senha, idade):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO usuarios (nome, email, senha, idade) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (nome, email, senha, idade))
    conn.commit()
    print("Usuário inserido com sucesso!")
    cursor.close()
    conn.close()
    def listar_usuarios():
        conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, email, idade FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)
    cursor.close()
    conn.close()
def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, email, idade FROM usuarios")
    usuarios = cursor.fetchall()
    for u in usuarios:
        print(u)
    cursor.close()
    conn.close()
