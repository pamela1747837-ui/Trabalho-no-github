import mysql.connector

bamco = mysql.connector.connect(
    host="10.30.29.162",
    port=3309,
    user="root",
    password="root123",
    detabase="anny"
)
import sqlite3

cursor = banco.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS Pamela")
a = 10
while True:
    nome = input("digite seu nome: ")
    if nome == "sair":
        break
cursor.execute (f"INSERT INT usuario VALUES ({id_usuario}, '{nome}', '{senha}', {idade})")
