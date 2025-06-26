import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


try:
 cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?)",("Jonathan", "Jonathan@gmail.com"))
 cursor.execute("INSERT INTO clientes (id, nome, email) VALUES (?,?,?)",(1, "Teste", "teste@gmail.com"))
 conexao.commit()  
except Exception as exc:
    print(f"Ops!! um erro ocorreu! {exc}")
    conexao.rollback() 
finally:
    conexao.commit()    