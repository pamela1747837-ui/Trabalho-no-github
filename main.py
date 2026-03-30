import mysql.connector

banco = mysql.connector.connect(
    host="10.30.29.183",
    port=3309,
    user="root",
    password="root123",
    detabase="anny_e_pamela"
)
  sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    senha VARCHAR(255),
    idade INT
); 
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
def apagar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    sql = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(sql, (id_usuario,))
    conn.commit()
    print(f"Registro {id_usuario} removido.")
    cursor.close()
    conn.close()
def fazer_login(email, senha_digitada):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    sql = "SELECT senha FROM usuarios WHERE email = %s"
    cursor.execute(sql, (email,))
    usuario = cursor.fetchone()
    
    if usuario and usuario['senha'] == senha_digitada:
        print("Login autorizado!")
    else:
        print("E-mail ou senha incorretos.")
    
    cursor.close()
    conn.close()
