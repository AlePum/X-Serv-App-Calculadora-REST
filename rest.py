import webapp
import random


class calcuRest(webapp.webApp):

    def parse(self, request):
        metodo = request.split()[0]
        recurso = request.split()[1].split("/")[1]
        cuerpo = request.split("\r\n\r\n")[1]
        return (metodo, recurso, cuerpo)


    def process(self, parsedRequest):
        (metodo, recurso, cuerpo) = parsedRequest
        if metodo == "GET":
            try:
                if len(self.operacion.split("+")) == 2:
                    sumar = float(self.operacion.split("+")[0]) + float(self.operacion.split("+")[1])
                    httpCode = "200 OK"
                    htmlBody = ("El resultado de la suma es: " + str(sumar))
                if len(self.operacion.split("-")) == 2:
                    restar = float(self.operacion.split("-")[0]) - float(self.operacion.split("-")[1])
                    httpCode = "200 OK"
                    htmlBody = ("El resultado de la resta es: " + str(restar))
                if len(self.operacion.split("*")) == 2:
                    multiplicar = float(self.operacion.split("*")[0]) * float(self.operacion.split("*")[1])
                    httpCode = "200 OK"
                    htmlBody = ("El resultado de la multiplicacion es: " + str(multiplicar))
                if len(self.operacion.split("/")) == 2:
                    dividir = float(self.operacion.split("/")[0]) / float(self.operacion.split("/")[1])
                    httpCode = "200 OK"
                    htmlBody = ("El resultado de la division es: " + str(dividir))
            except AttributeError:
                return ("404 Not Found", "Utiliza PUT")
            except ValueError:
                return ("404 Not Found", "Operacion Incorrecta")
        elif metodo == "PUT":
            self.operacion = cuerpo
            print self.operacion
            httpCode = "200 OK"
            htmlBody = ("La operacion pasada es: " + cuerpo)
        return (httpCode, htmlBody)

if __name__ == "__main__":
    calculadora = calcuRest("localhost", 1234)
