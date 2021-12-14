import mysql.connector

class Connection():

    def __init__(self, userId):
      self._userId = userId

    @property
    def userId(self):
      return self._userId

    @userId.setter
    def userId(self, userId):
      self._userId = userId


    def getData(self, mydb, *args):
      mydb = mysql.connector.connect(
        host="b8tcabkum5dy8adidox0-mysql.services.clever-cloud.com",
        user="uwzqzz3dglhmhuxi",
        password="SXVjEEmuQxL2TWNOiOfN",
        database="b8tcabkum5dy8adidox0"
      )
      mycursor = mydb.cursor()
      sql = "INSERT INTO `Persona` (`idPersona`, `nombrePersona`, `apellidoPersona`, `phone`) VALUES (%s,%s,%s,%s)"
      val = args
      mycursor.execute(sql, val)
      mydb.commit()
      mydb.close()
