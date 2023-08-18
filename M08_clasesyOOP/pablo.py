class modulo_7:
    def primo(numero):
        cte = 0
        for i in range(2, (numero - 1)):
            if numero % i == 0:
                cte += 1
        if cte == 0:
            return True
        else:
            return False


    def ContadorNumeros(numeros):
        n = 0
        rep = 0
        valorComun = 0

        for i in numeros:
            for j in numeros:
                if i == j:
                    n += 1

                if n > rep:
                    rep = n
                    valorComun = i

            n = 0
        print("el valor que mas se repite es: ", valorComun)
        print("se repite ", rep, " veces")
        return rep, valorComun


    def convertidor(temperatura, origen, destino):
        if origen == "C" and destino == "F":
            tempeaturaF = (temperatura * (9 / 5)) + 32
            print(temperatura, "°C equibalen a ", tempeaturaF, "°F")
        elif origen == "C" and destino == "K":
            tempeaturaF = (temperatura + 273.15)
            print(temperatura, "°C equibalen a ", tempeaturaF, "°K")


    def Factorial(numero):
        base = 1
        for i in range(1, numero):
            base = base + (base * i)
        return (base)

print(modulo_7.Factorial(5))