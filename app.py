import flask
import mysql.connector
from flask import request

mydb = mysql.connector.connect(
  host="b8tcabkum5dy8adidox0-mysql.services.clever-cloud.com",
  user="uwzqzz3dglhmhuxi",
  password="SXVjEEmuQxL2TWNOiOfN",
  database="b8tcabkum5dy8adidox0"
)
app = flask.Flask(__name__)

def insertar(pilar):
    pass

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True,force=True)
    fulfillmentText = ''
    query_result = req.get('queryResult')
    if query_result.get('action') == 'register.data':
        try:
            idUser = int(query_result.get('parameters').get('id'))
            nameUser = str(query_result.get('parameters').get('name'))
            lastUser = str(query_result.get('parameters').get('last'))
            charge = str(query_result.get('parameters').get('cargo'))
            password = str(query_result.get('parameters').get('password'))
            mycursor = mydb.cursor()
            sql = "INSERT INTO `Stakeholder` (`idStakeholder`, `nombreStakeholder`, `apellidoStakeholder`, `cargoStakeholder`, `passwordStakeholder`) VALUES (%s,%s,%s,%s,%s)"
            val = (idUser, nameUser, lastUser, charge, password)
            mycursor.execute(sql, val)
            mydb.commit()
            fulfillmentText = f'¡Gracias!, Sr(a). {nameUser} su registro se ha completado exitosamente. Para continuar escriba: "Comenzar llenado de datos" '
        except:
            fulfillmentText = 'No fue posible completar el registro'

    elif query_result.get('action') =='inicio.sesion':
        idUser = int(query_result.get('parameters').get('id'))
        try:
            mycursor = mydb.cursor()
            sql = "SELECT `nombreStakeholder`, `apellidoStakeholder` FROM `Stakeholder` WHERE `idStakeholder` =%s" % (idUser)
            mycursor.execute(sql)
            resultado = mycursor.fetchall()
            fulfillmentText = 'Bienvenido ' + resultado[0][0] + ' ' + resultado[0][1]

        except:
            fulfillmentText = 'Intente de nuevo'

    elif query_result.get('action') =='get.pregunta':
        idUser = int(query_result.get('parameters').get('id'))
        try:
            mycursor = mydb.cursor()
            sql = "SELECT `nombrePersona`, `apellidoPersona` FROM `Persona` WHERE `idPersona` =%s" % (idUser)
            mycursor.execute(sql)
            resultado = mycursor.fetchall()
            fulfillmentText = 'Bienvenido ' + resultado[0][0] + ' ' + resultado[0][1]

        except:
            fulfillmentText = 'Intente de nuevo'

    elif query_result.get('action') =='Institucionalidad':
        p1_institucionalidad = str(query_result.get('parameters').get('p1_1_institucionalidad'))
        p1_institucionalidad = p1_institucionalidad[1:]
        p2_institucionalidad = str(query_result.get('parameters').get('p2_institucionalidad'))
        p2_institucionalidad = p2_institucionalidad[1:]
        p3_institucionalidad = str(query_result.get('parameters').get('p3_institucionalidad'))
        p3_institucionalidad = p3_institucionalidad[1:]
        p4_institucionalidad = str(query_result.get('parameters').get('p4_institucionalidad'))
        p4_institucionalidad = p4_institucionalidad[1:]
        p5_institucionalidad = str(query_result.get('parameters').get('p5_institucionalidad'))
        p5_institucionalidad = p5_institucionalidad[1:]
        p6_institucionalidad = str(query_result.get('parameters').get('p6_institucionalidad'))
        p6_institucionalidad = p6_institucionalidad[1:]
        p7_institucionalidad = str(query_result.get('parameters').get('p7_institucionalidad'))
        p7_institucionalidad = p7_institucionalidad[1:]
        p8_institucionalidad = str(query_result.get('parameters').get('p8_institucionalidad'))
        p8_institucionalidad = p8_institucionalidad[1:]
        p9_institucionalidad = str(query_result.get('parameters').get('p9_institucionalidad'))
        p9_institucionalidad = p9_institucionalidad[1:]
        p10_institucionalidad = str(query_result.get('parameters').get('p10_institucionalidad'))
        p10_institucionalidad = p10_institucionalidad[1:]
        try:
            mycursor = mydb.cursor()

            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('1', '72209978', '1', '1', %s)" % (p1_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('2', '72209978', '1', '2', %s)" % (p2_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('3', '72209978', '1', '3', %s)" % (p3_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('4', '72209978', '1', '4', %s)" % (p4_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('5', '72209978', '1', '5', %s)" % (p5_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('6', '72209978', '1', '6', %s)" % (p6_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('7', '72209978', '1', '7', %s)" % (p7_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('8', '72209978', '1', '8', %s)" % (p8_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('9', '72209978', '1', '9', %s)" % (p9_institucionalidad)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('10', '72209978', '1', '10', %s)" % (p10_institucionalidad)
            mycursor.execute(sql)
            mydb.commit()
            fulfillmentText = f'''Se completaron los datos del pilar {query_result.get('action')}. Para continuar puede:
        - Continuar la entrada de datos
            '''

        except:
            fulfillmentText = 'Intente de nuevo'

    elif query_result.get('action') =='Infraestructura':
        p1_infraestructura = str(query_result.get('parameters').get('p1_1_infraestructura'))
        p1_infraestructura = p1_infraestructura[1:]
        p2_infraestructura = str(query_result.get('parameters').get('p2_infraestructura'))
        p2_infraestructura = p2_infraestructura[1:]
        p3_infraestructura = str(query_result.get('parameters').get('p3_infraestructura'))
        p3_infraestructura = p3_infraestructura[1:]
        p4_infraestructura = str(query_result.get('parameters').get('p4_infraestructura'))
        p4_infraestructura = p4_infraestructura[1:]
        p5_infraestructura = str(query_result.get('parameters').get('p5_infraestructura'))
        p5_infraestructura = p5_infraestructura[1:]
        p6_infraestructura = str(query_result.get('parameters').get('p6_infraestructura'))
        p6_infraestructura = p6_infraestructura[1:]
        p7_infraestructura = str(query_result.get('parameters').get('p7_infraestructura'))
        p7_infraestructura = p7_infraestructura[1:]
        p8_infraestructura = str(query_result.get('parameters').get('p8_infraestructura'))
        p8_infraestructura = p8_infraestructura[1:]
        p9_infraestructura = str(query_result.get('parameters').get('p9_infraestructura'))
        p9_infraestructura = p9_infraestructura[1:]
        p10_infraestructura = str(query_result.get('parameters').get('p10_infraestructura'))
        p10_infraestructura = p10_infraestructura[1:]
        try:
            mycursor = mydb.cursor()
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('11', '72209978', '1', '11', %s)" % (p1_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('12', '72209978', '1', '12', %s)" % (p2_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('13', '72209978', '1', '13', %s)" % (p3_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('14', '72209978', '1', '14', %s)" % (p4_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('15', '72209978', '1', '15', %s)" % (p5_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('16', '72209978', '1', '16', %s)" % (p6_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('17', '72209978', '1', '17', %s)" % (p7_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('18', '72209978', '1', '18', %s)" % (p8_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('19', '72209978', '1', '19', %s)" % (p9_infraestructura)
            mycursor.execute(sql)
            sql = "INSERT INTO `Valor_completado` (`idIndicador`, `idStakeholder`, `idSesion`, `idItemEvaluacion`, `valor`) VALUES ('20', '72209978', '1', '20', %s)" % (p10_infraestructura)
            mycursor.execute(sql)
            mydb.commit()
            fulfillmentText = f'''Se completaron los datos del pilar {query_result.get('action')}. Para continuar puede:
        - Continuar la entrada de datos
            '''

        except:
            fulfillmentText = 'Intente de nuevo'

    return {
        'fulfillmentText': fulfillmentText
    }


if __name__ == "__main__":
    app.secret_key = 'ItIsASecret'
    app.debug = True
    app.run()