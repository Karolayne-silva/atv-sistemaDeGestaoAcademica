import mysql.connector

class ConexaoDB:
    def __init__(self, host="localhost", user="root", password="teste", database = "sga"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
    
        self.conexao = mysql.connector.connect(host = self.host,
                                           user = self.user,
                                           password = self.password,
                                           database = self.database)
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()

    def executarDQL(self, comando): 
        self.conectar()
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall() 
        self.desconectar()
        return print(resultado)

    def executarDML(self, comando):
        self.conectar()
        self.cursor.execute(comando)
        self.conexao.commit() 
        self.desconectar()
    
