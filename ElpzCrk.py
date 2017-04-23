# -*- Coding: UTF-8 -*-
# Python 3
#
#          ███████╗██╗     ██████╗ ███████╗ ██████╗██████╗ ██╗  ██╗
#          ██╔════╝██║     ██╔══██╗╚══███╔╝██╔════╝██╔══██╗██║ ██╔╝
#          █████╗  ██║     ██████╔╝  ███╔╝ ██║     ██████╔╝█████╔╝ 
#          ██╔══╝  ██║     ██╔═══╝  ███╔╝  ██║     ██╔══██╗██╔═██╗ 
#          ███████╗███████╗██║     ███████╗╚██████╗██║  ██║██║  ██╗
#          ╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
#                                                         By: LawlietJH
#																v1.2.1

import threading
import time
import sys
import os



Autor = "LawlietJH"
Version = "v1.2.1"

BEC = """
          ███████╗██╗     ██████╗ ███████╗ ██████╗██████╗ ██╗  ██╗
          ██╔════╝██║     ██╔══██╗╚══███╔╝██╔════╝██╔══██╗██║ ██╔╝
          █████╗  ██║     ██████╔╝  ███╔╝ ██║     ██████╔╝█████╔╝ 
          ██╔══╝  ██║     ██╔═══╝  ███╔╝  ██║     ██╔══██╗██╔═██╗ 
          ███████╗███████╗██║     ███████╗╚██████╗██║  ██║██║  ██╗
          ╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝
"""
#~ Fuente: 'ANSI Shadow' - Página: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=ElpzCrk

BA = r"""
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩
"""
#~ Fuente: 'Calvin S' - Página: http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH


#=======================================================================



def Dat():
		
	Nombre = BEC
	Autor = BA
	Ver = "\n\n{:^80}".format(Version)
	print(Nombre, "\n\n", Autor, Ver)



#=======================================================================



Alf = ""
Actual = 0
Total = 0
Cony = 0
List = []
Lisy = []



#=======================================================================



def Progreso(x, Total):	# Imprime Una Barra De Progreso.
	
	TamBar = 30
	Progreso = (x * 100) / Total
	Actual = x / Total
	
	TiempoTransc = int(time.clock()) + 1
	BarraAct = int(Actual * TamBar)
	
	bar = "\r [+] Progreso: {:.2f}%".format(Progreso)
	bar += " |" + "█".join(["" for _ in range(BarraAct)])  # Imprimir Progreso.
	bar += " ".join(["" for _ in range(int(TamBar - BarraAct))]) + "|"
	bar += " [" + Tiempo((Total - x) * (TiempoTransc / x))  + "] "	# Imprimir Tiempo Restante.
	
	sys.stdout.write(bar)



def Tiempo(sec):	# Imprime El Tiempo Restante.
	
	if sec >= 3600:  # Convierte a Horas
		return "{0:d} hora(s)".format(int(sec / 3600))
	elif sec >= 60:  # Convierte a Minutos
		return "{0:d} minuto(s)".format(int(sec / 60))
	else:            # Sin Conversión
		return "{0:d} segundo(s)".format(int(sec))



def Tot():	# Función Que Determina La Canctidad De Cadenas De Salida (Con Repetición).
	
	global Cony
	
	Len = len(Alf)
	Z = 0
	
	for x in range(1, Cony+1):
		
		Z += Len ** x
	
	return Z
	


def Save(X, Eny):
	
	global Actual
	
	Actual += 1
	Barra()
	Eny.write(X + "\n")



#=======================================================================



def Combin(A, Eny):
	
	global Cony
	
	if Cony == 2:
		
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
	
	elif Cony == 3:
		
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
			for _3 in Alf:
				_3 = _2 + _3
				Save(_3, Eny)
	
	elif Cony == 4:
			
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
			for _3 in Alf:
				_3 = _2 + _3
				Save(_3, Eny)
				for _4 in Alf:
					_4 = _3 + _4
					Save(_4, Eny)
	
	elif Cony == 5:
		
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
			for _3 in Alf:
				_3 = _2 + _3
				Save(_3, Eny)
				for _4 in Alf:
					_4 = _3 + _4
					Save(_4, Eny)
					for _5 in Alf:
						_5 = _4 + _5
						Save(_5, Eny)
	
	elif Cony == 6:
		
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
			for _3 in Alf:
				_3 = _2 + _3
				Save(_3, Eny)
				for _4 in Alf:
					_4 = _3 + _4
					Save(_4, Eny)
					for _5 in Alf:
						_5 = _4 + _5
						Save(_5, Eny)
						for _6 in Alf:
							_6 = _5 + _6
							Save(_6, Eny)
	
	elif Cony == 7:
		
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
			for _3 in Alf:
				_3 = _2 + _3
				Save(_3, Eny)
				for _4 in Alf:
					_4 = _3 + _4
					Save(_4, Eny)
					for _5 in Alf:
						_5 = _4 + _5
						Save(_5, Eny)
						for _6 in Alf:
							_6 = _5 + _6
							Save(_6, Eny)
							for _7 in Alf:
								_7 = _6 + _7
								Save(_7, Eny)



def Barra():
	
	global Total, Actual
	
	if Total > 1 and Total <= 1000 :
		if Actual % 50 == 0: Progreso(Actual, Total)
	elif Total > 1000 and Total <= 100000 :
		if Actual % 100 == 0: Progreso(Actual, Total)
	elif Total > 100000 and Total <= 1000000 :
		if Actual % 500 == 0: Progreso(Actual, Total)
	elif Total > 1000000 and Total <= 10000000:
		if Actual % 12000 == 0: Progreso(Actual, Total)
	elif Total > 10000000:
		if Actual % 10000 == 0: Progreso(Actual, Total)

	
	
def Imprimir(Eny):
	
	global Total, Actual
	
	Total = Tot()
	Actual = 1
	
	print("\n\n\t [*] Generando Lista De Cadenas y Guardandolas En El Archivo...")
	print("\n\n\t\t [~] Tamaño Aprox. De Salida: {:.3f} Mb.".format(Total/130000))
	print("\n\t\t [~] Total De Cadenas: {}\n\n".format(Total))
	
	for x in Alf:
		
		Save(x, Eny)
		
		if Cony >= 2: Combin(x, Eny)
	
	Progreso(Actual-1, Total)



def Main():
	
	global Cony, Total, Alf
	
	Keys = input("\n\n [*] Añade Palabras Para Crear El Diccionario."+
				 "\n\n [*] Separalas usando 'espacio' ',' ';'"+
				 "\n\n [*] Ejemplos: Hola Mundo | Hola,Mundo | Hola;Mundo | Hola, Mundo | etc."+
				 "\n\n     >>> ").replace(" ",";").replace(",",";").split(";")
	Alfa = ""
	Alf = ""
	
	for x in Keys:	# Obtenemos Una Sola Cadena con Todas Las Palabras Escritas.
		
		if x != "": Alfa += x
	
	for y in Alfa:	# Eliminamos Letras Repetidas.
		
		if not y in Alf: Alf += y
	
	while True:
	
		try:
			
			Cony = int(input("\n [+] Longitud Máx. [1-6]: "))
			
			if Cony > 6: print("\n\n [!] Error!")
			elif Cony < 1: return
			else: break
		
		except:
			
			print("\n\n [!] Error!")
	
	open("Eny.ZioN","w")
	Eny = open("Eny.ZioN","a")
	
	Imprimir(Eny)
	
	Eny.close()
	
	print("\n\n")
	
	os.system("Pause")



if __name__ == "__main__":
	
	
	Dat()
	
	Main()


