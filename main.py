from conexao import criar_conexao, fechar_conexao

def insere_usuario(con,usuario,email,senha):
    cursor = con.cursor()
    sql = "INSERT INTO usuarios (usuario,email,senha) values (%s, %s, %s)"
    valores = (usuario,email,senha)
    cursor.execute(sql, valores)
    cursor.close()
    con.commit()

def usuarios_cadastrados(con):
    cursor = con.cursor()
    sql = "SELECT id, usuario, email FROM usuarios"
    cursor.execute(sql)
    
    for (id, usuario, email) in cursor:
        print(id, usuario, email)
    
    cursor.close()
def main():
    con = criar_conexao("localhost", "root", "", "banco")
    insere_usuario(con, "Maria", "maria@maria.com.br", "maria123")

    usuarios_cadastrados(con)
    fechar_conexao(con)

if __name__ == '__main__':
    main()