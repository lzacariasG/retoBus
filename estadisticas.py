import psycopg2 
import openpyxl
import subprocess
import json

class estadisticas:
    def leeCargas(self):
        sqlC = "SELECT id, nombre, fchCarga::varchar, registroscargados, registroserror, montototal FROM archivoscargados ORDER BY id desc"
        self.conection = psycopg2.connect("dbname=bdBous user=jonathan password=admin")
        self.cursor = self.conection.cursor()
        self.cursor.execute (sqlC)
        results = self.cursor.fetchall()
        return results
   
        

instCls = estadisticas()
salida = instCls.leeCargas()
json_output = json.dumps(salida)
