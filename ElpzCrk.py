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
#																v1.3.6

import string
import time
import sys
import os



Autor = "LawlietJH"
Version = "v1.3.6"

BEC = """
          ███████╗██╗     ██████╗ ███████╗ ██████╗██████╗ ██╗  ██╗
          ██╔════╝██║     ██╔══██╗╚══███╔╝██╔════╝██╔══██╗██║ ██╔╝
          █████╗  ██║     ██████╔╝  ███╔╝ ██║     ██████╔╝█████╔╝ 
          ██╔══╝  ██║     ██╔═══╝  ███╔╝  ██║     ██╔══██╗██╔═██╗ 
          ███████╗███████╗██║     ███████╗╚██████╗██║  ██║██║  ██╗
          ╚══════╝╚══════╝╚═╝     ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝"""
#~ Fuente: 'ANSI Shadow' - Página: http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=ElpzCrk

BA = """
                            ╦  ┌─┐┬ ┬┬  ┬┌─┐┌┬┐╦╦ ╦
                            ║  ├─┤││││  │├┤  │ ║╠═╣
                            ╩═╝┴ ┴└┴┘┴─┘┴└─┘ ┴╚╝╩ ╩"""
#~ Fuente: 'Calvin S' - Página: http://patorjk.com/software/taag/#p=display&f=Calvin%20S&t=LawlietJH


#=======================================================================



def Dat():	# Imprime Los Banners.
		
	Nombre = BEC
	Autor = BA
	Ver = "\n\n{:^80}".format(Version)
	print(Nombre, "\n", Autor, Ver)



#=======================================================================



Alf = ""
Actual = 0
Total = 0
Cony = 0
List = []
Lisy = []
Comy = False



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
	
	if sec >= 31449600000:  # Convierte a Milenios
		return "{:d} Milenio(s)".format(int(sec / 31449600000))
	elif sec >= 3144960000:  # Convierte a Siglos
		return "{:d} Siglo(s)".format(int(sec / 3144960000))
	elif sec >= 314496000:  # Convierte a Decadas
		return "{:d} Decada(s)".format(int(sec / 314496000))
	elif sec >= 31449600:  # Convierte a Años
		return "{:d} año(s)".format(int(sec / 31449600))
	elif sec >= 604800:  # Convierte a Semanas
		return "{:d} Semana(s)".format(int(sec / 604800))
	elif sec >= 86400:  # Convierte a Dias
		return "{:d} Dia(s)".format(int(sec / 86400))
	elif sec >= 3600:  # Convierte a Horas
		return "{:d} hora(s)".format(int(sec / 3600))
	elif sec >= 60:  # Convierte a Minutos
		return "{:d} minuto(s)".format(int(sec / 60))
	else:            # Sin Conversión
		return "{:d} segundo(s)".format(int(sec))



def Tot():	# Función Que Determina La Canctidad De Cadenas De Salida.
	
	global Cony
	
	Len = len(Alf)
	Z = 0
	
	for x in range(1, Cony+1):
		
		Z += Len ** x
	
	return Z



def Save(X, Eny):	# Función Que Guarda Las Cadenas En EL Archivo.
	
	global Actual
	
	Actual += 1
	Barra()
	Eny.write(X + "\n")



#=======================================================================



def Combin(A, Eny):	# Función Que Crea Las Cadenas Desde 1 Hasta El Máximo de Longitud Elegida.
	
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
	elif Cony == 8:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
	elif Cony == 9:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
	elif Cony == 10:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
	elif Cony == 11:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
	elif Cony == 12:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
												for _12 in Alf:
													_12 = _11 + _12
													Save(_12, Eny)
	elif Cony == 13:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
												for _12 in Alf:
													_12 = _11 + _12
													Save(_12, Eny)
													for _13 in Alf:
														_13 = _12 + _13
														Save(_13, Eny)
	elif Cony == 14:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
												for _12 in Alf:
													_12 = _11 + _12
													Save(_12, Eny)
													for _13 in Alf:
														_13 = _12 + _13
														Save(_13, Eny)
														for _14 in Alf:
															_14 = _13 + _14
															Save(_14, Eny)
	elif Cony == 15:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
												for _12 in Alf:
													_12 = _11 + _12
													Save(_12, Eny)
													for _13 in Alf:
														_13 = _12 + _13
														Save(_13, Eny)
														for _14 in Alf:
															_14 = _13 + _14
															Save(_14, Eny)
															for _15 in Alf:
																_15 = _14 + _15
																Save(_15, Eny)
	elif Cony == 16:
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
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
												for _12 in Alf:
													_12 = _11 + _12
													Save(_12, Eny)
													for _13 in Alf:
														_13 = _12 + _13
														Save(_13, Eny)
														for _14 in Alf:
															_14 = _13 + _14
															Save(_14, Eny)
															for _15 in Alf:
																_15 = _14 + _15
																Save(_15, Eny)
																for _16 in Alf:
																	_16 = _15 + _16
																	Save(_16, Eny)



def Comby(A, Eny):	# Función Que Crea Las Cadenas Sólo de la Longitud Elegida.
	
	global Cony
	
	if Cony == 2:
		for _2 in Alf:
			_2 = A + _2
			Save(_2, Eny)
	elif Cony == 3:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				Save(_3, Eny)
	elif Cony == 4:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					Save(_4, Eny)
	elif Cony == 5:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						Save(_5, Eny)
	elif Cony == 6:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							Save(_6, Eny)
	elif Cony == 7:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								Save(_7, Eny)
	elif Cony == 8:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									Save(_8, Eny)
	elif Cony == 9:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										Save(_9, Eny)
	elif Cony == 10:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											Save(_10, Eny)
	elif Cony == 11:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											for _11 in Alf:
												_11 = _10 + _11
												Save(_11, Eny)
	elif Cony == 12:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											for _11 in Alf:
												_11 = _10 + _11
												for _12 in Alf:
													_12 = _11 + _12
													Save(_12, Eny)
	elif Cony == 13:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											for _11 in Alf:
												_11 = _10 + _11
												for _12 in Alf:
													_12 = _11 + _12
													for _13 in Alf:
														_13 = _12 + _13
														Save(_13, Eny)
	elif Cony == 14:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											for _11 in Alf:
												_11 = _10 + _11
												for _12 in Alf:
													_12 = _11 + _12
													for _13 in Alf:
														_13 = _12 + _13
														for _14 in Alf:
															_14 = _13 + _14
															Save(_14, Eny)
	elif Cony == 15:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											for _11 in Alf:
												_11 = _10 + _11
												for _12 in Alf:
													_12 = _11 + _12
													for _13 in Alf:
														_13 = _12 + _13
														for _14 in Alf:
															_14 = _13 + _14
															for _15 in Alf:
																_15 = _14 + _15
																Save(_15, Eny)
	elif Cony == 16:
		for _2 in Alf:
			_2 = A + _2
			for _3 in Alf:
				_3 = _2 + _3
				for _4 in Alf:
					_4 = _3 + _4
					for _5 in Alf:
						_5 = _4 + _5
						for _6 in Alf:
							_6 = _5 + _6
							for _7 in Alf:
								_7 = _6 + _7
								for _8 in Alf:
									_8 = _7 + _8
									for _9 in Alf:
										_9 = _8 + _9
										for _10 in Alf:
											_10 = _9 + _10
											for _11 in Alf:
												_11 = _10 + _11
												for _12 in Alf:
													_12 = _11 + _12
													for _13 in Alf:
														_13 = _12 + _13
														for _14 in Alf:
															_14 = _13 + _14
															for _15 in Alf:
																_15 = _14 + _15
																for _16 in Alf:
																	_16 = _15 + _16
																	Save(_16, Eny)
	


def Barra():	# Función Que Controla La Velocidad Al Imprimir En Pantalla La Barra De Progreso.
	
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



def getTotal(Total):	# Función Que Divide Con Coma "," La Cadena Del Total De Cadenas En El Archivo.
	
	Len = len(str(Total))
	Cadena = ""
	
	if Len >= 4 and Len <=6:
		Cadena = str(Total)
		Cadena = Cadena[:-3] + "," + Cadena[-3:]
		return Cadena
	elif Len >= 7 and Len <=9:
		Cadena = str(Total)
		Cadena = Cadena[:-6] + "," + Cadena[-6:-3] + "," + Cadena[-3:]
		return Cadena
	elif Len >= 10 and Len <=12:
		Cadena = str(Total)
		Cadena = Cadena[:-9] + "," + Cadena[-9:-6] + "," + Cadena[-6:-3] + "," + Cadena[-3:]
		return Cadena
	elif Len >= 13 and Len <=15:
		Cadena = str(Total)
		Cadena = Cadena[:-12] + "," + Cadena[-12:-9] + "," + Cadena[-9:-6] + "," + Cadena[-6:-3] + "," + Cadena[-3:]
		return Cadena
	elif Len >= 16 and Len <=18:
		Cadena = str(Total)
		Cadena = Cadena[:-15] + "," + Cadena[-15:-12] + "," + Cadena[-12:-9] + "," + Cadena[-9:-6] + "," + Cadena[-6:-3] + "," + Cadena[-3:]
		return Cadena	
	elif Len >= 19 and Len <=21:
		Cadena = str(Total)
		Cadena = Cadena[:-18] + "," + Cadena[-18:-15] + "," + Cadena[-15:-12] + "," + Cadena[-12:-9] + "," + Cadena[-9:-6] + "," + Cadena[-6:-3] + "," + Cadena[-3:]
		return Cadena
	elif Len >= 22 and Len <=24:
		Cadena = str(Total)
		Cadena = Cadena[:-21] + "," + Cadena[-21:-18] + "," + Cadena[-18:-15] + "," + Cadena[-15:-12] + "," + Cadena[-12:-9] + "," + Cadena[-9:-6] + "," + Cadena[-6:-3] + "," + Cadena[-3:]
		return Cadena
	else: return str(Total)

	
def Imprimir(Eny):	# Función Que Imprime En Pantalla La Información de Salida.
	
	global Total, Actual
	
	if Comy == False:
		
		Total = Tot()
		Actual = 1
		Tam = Total/130000
		Cadenas = ""
	
		print("\n\t [*] Generando Lista De Cadenas y Guardandolas En El Archivo...")
		if Tam < 1000:   print("\n\t\t [~] Tamaño Aprox. De Salida:\t{:.3f} Mb.".format(Tam))
		elif Tam > 1000: print("\n\t\t [~] Tamaño Aprox. De Salida:\t{:.2f} Gb.".format(Tam/1000))
		
		if len(str(Total)) <= 3: Cadenas = Total
		else: Cadenas = getTotal(Total)
		
		print("\t\t [~] Total De Cadenas:\t\t{}".format(Cadenas))
		print("\t\t [~] Nombre De Archivo:\t\tEny.ZioN\n\n")
		
		try:
			for x in Alf:
				
				Save(x, Eny)
				
				if Cony >= 2: Combin(x, Eny)
			
			Progreso(Actual-1, Total)
		
		except KeyboardInterrupt:
				
				print("\n\n\t Cancelando..!")
				try: time.sleep(1.5)
				except KeyboardInterrupt: pass
				exit(1)
				
	elif Comy == True:
		
		Total = len(Alf) ** Cony
		Actual = 1
		Tam = 0
		
		if Cony == 7: Tam = Total/116510
		elif Cony == 6: Tam = Total/131240
		elif Cony == 5: Tam = Total/146500
		else: Tam = Total / 100000
		
		Cadenas = ""
		
		print("\n\t [*] Generando Lista De Cadenas y Guardandolas En El Archivo...")
		if Tam < 1000:
			print("\n\t\t [~] Tamaño Aprox. De Salida:\t{:.3f} Mb.".format(Tam))
		elif Tam >= 1000 and Tam < 10000:
			print("\n\t\t [~] Tamaño Aprox. De Salida:\t{:.2f} Gb.".format(Tam/1000))
		elif Tam >= 10000:
			print("\n\t\t [~] Tamaño Aprox. De Salida:\t{:.2f} Tb.".format(Tam/10000))
		
		if len(str(Total)) <= 3: Cadenas = Total
		else: Cadenas = getTotal(Total)
		
		print("\t\t [~] Total De Cadenas:\t\t{}".format(Cadenas))
		print("\t\t [~] Nombre De Archivo:\t\tEny.ZioN\n\n")
		
		try:
			
			for x in Alf:
				
				if Cony == 1: Save(x, Eny)
				elif Cony >= 2: Comby(x, Eny)
			
			Progreso(Actual-1, Total)
		
		except KeyboardInterrupt:
				
				print("\n\n\t Cancelando..!")
				try: time.sleep(1.5)
				except KeyboardInterrupt: pass
				exit(1)



#=======================================================================



def KeyGen(Keys):	#~ Comprueba si hay alguna petición especial de caracteres.
	
	Keys = Keys.replace("a-z", string.ascii_lowercase)	#~ Alfabeto Minúsculas.
	Keys = Keys.replace("A-Z", string.ascii_uppercase)	#~ Alfabeto Mayúsculas.
	Keys = Keys.replace("a-Z", string.ascii_lowercase + string.ascii_uppercase)	#~ Alfabeto Minúsculas + Alfabeto Mayúsculas.
	Keys = Keys.replace("0-9", string.digits)	#~ Digitos de 0 al 9.
	Keys = Keys.replace("0-z", string.digits + string.ascii_lowercase)	#~ Digitos + Alfabeto Minúsculas.
	Keys = Keys.replace("0-Z", string.digits + string.ascii_uppercase)	#~ Digitos + Alfabeto Mayúsculas.
	Keys = Keys.replace("0-z-Z", string.digits + string.ascii_lowercase + string.ascii_uppercase)	#~ Digitos + Alfabeto Minúsculas + Alfabeto Mayúsculas.
	Keys = Keys.replace("0-f", string.hexdigits.lower())	#~ Hexadecimal Minúsculas.
	Keys = Keys.replace("0-F", string.hexdigits.upper())	#~ Hexadecimal Mayúsculas.
	Keys = Keys.replace("0-f-F", string.hexdigits)	#~ Hexadecimal Minúsculas + Hexadecimal Mayúsculas.
	
	return Keys



#=======================================================================



def Main():	# Función Principal Que Llama A Las Otras Funciones.
	
	global Cony, Total, Alf, Comy
	
	while True:
		
		os.system("cls")
		
		print("\n\t [1] Crear Diccionarios Con Caracteres Desde 1. ")
		print("\n\t [2] Crear Diccionarios Con Caracteres De La Longitud Indicada. ")
		print("\n\t >>> ", end="")
		
		try:
			Resp = int(input())
			
			if Resp == 2:
				Comy = True
				break
			elif Resp == 1:
				Comy = False
				break
			else: pass
			
		except: pass
		
	Keys = ""
	
	while True:
		
		os.system("cls")
		Dat()
		
		try:
			print("\n [*] Añade Palabras Para Crear El Diccionario."+
				"\n [*] Separalas usando 'espacio' ',' ';'"+
				"\n [*] Ejemplos: Hola Mundo | Hola,Mundo | Hola;Mundo | Hola, Mundo | etc."+
				"\n\n")
			Keys = input("     >>> ")
			
			Keys = KeyGen(Keys).replace(" ",";").replace(",",";").split(";")
			
			if Keys != [""]: break
			
		except KeyboardInterrupt:
			
			print("\n\n\t Cancelando..!")
			try: time.sleep(1.5)
			except KeyboardInterrupt: pass
			exit(1)
	
	Alfa = ""
	Alf = ""
	
	for x in Keys:	# Obtenemos Una Sola Cadena con Todas Las Palabras Escritas.
		
		if x != "": Alfa += x
	
	for y in Alfa:	# Eliminamos Letras Repetidas. Asi Evitamos Las Cadenas Repetidas.
		
		if not y in Alf: Alf += y
	
	if len(Alf) > 70:
		print("\n\n [!] Es Una Locura Viejo!!! Hay Más de 1 Cuatrillon De Posibilidades!!!")
		print("\n\n\t Algo así como: 1'000,000'000,000'000,000'000,000")
		print("\t\t\t  Trillon  Billon  Millon  Miles")
		time.sleep(5)
		return
	
	while True:
	
		try:
			
			if Comy == False: Cony = int(input("\n [+] Longitud Máx. [1-16]: "))
			elif Comy == True: Cony = int(input("\n [+] Longitud [1-16]: "))
			
			if Cony > 16: print("\n\n\t [!] Elige Un Número Entre [1-16]\n")
			elif Cony < 1: pass
			else: break
		
		except KeyboardInterrupt:
			
			print("\n\n\t Cancelando..!")
			try: time.sleep(1.5)
			except KeyboardInterrupt: pass
			exit(1)
		
		except ValueError: pass
	
	open("Eny.ZioN","w")
	Eny = open("Eny.ZioN","a")
	
	Imprimir(Eny)
	
	Eny.close()
	
	print("\n\n")
	
	os.system("Pause")



if __name__ == "__main__":
	
	Main()


