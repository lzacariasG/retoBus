import psycopg2 
import openpyxl
import subprocess
import json

class estadisticas:
    def estadisticasArch(self):
        sqlC = "select id, nombre, fchcarga, registroscargados, registroserror, montototal  from archivoscargados a "
        self.conection = psycopg2.connect("dbname=bdBous user=jonathan password=admin")
        self.cursor = self.conection.cursor()
        self.cursor.execute (sqlC)
        results = self.cursor.fetchall()
        return results
   
    def estadisticasCd(self):
        sqlC = "select c.ciudad, count(*), sum(valoradeudo ) from adeudocliente a left join ciudades c on c.id = a.idciudad where a.idarchivo = 23 group by c.ciudad"
        self.conection = psycopg2.connect("dbname=bdBous user=jonathan password=admin")
        self.cursor = self.conection.cursor()
        self.cursor.execute (sqlC)
        results = self.cursor.fetchall()
        return results
    
    def estadisticasCd(self):
        sqlC = "select a.empresa, count(*), sum(valoradeudo )from adeudocliente a where a.idarchivo = 23 group by empresa"
        self.conection = psycopg2.connect("dbname=bdBous user=jonathan password=admin")
        self.cursor = self.conection.cursor()
        self.cursor.execute (sqlC)
        results = self.cursor.fetchall()
        return results
    

instCls = estadisticas()
salida = instCls.leeCargas()
json_output = json.dumps(salida)





 
 