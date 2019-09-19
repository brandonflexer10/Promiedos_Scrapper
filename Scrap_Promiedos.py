import requests
from bs4 import BeautifulSoup

def obtener_fechas_boca_1718():
	links = []
	fechas = []
	for i in list(range(27)):
		links.append('http://www.promiedos.com.ar/fechatotal.php?fecha=' + str(i + 1) + '_1&liga=Primera&temporada=20172&grupo=1')
	for link in links:
		page = requests.get(link)
		fechas.append(BeautifulSoup(page.text, 'html.parser'))
	return fechas

def obtener_fechas_boca_1617():
	links = []
	fechas = []
	for i in list(range(30)):
		links.append('http://www.promiedos.com.ar/fechatotal.php?fecha=' + str(i + 1) + '_1&liga=Primera&temporada=20162&grupo=1')
	for link in links:
		page = requests.get(link)
		fechas.append(BeautifulSoup(page.text, 'html.parser'))
	return fechas

def obtener_fechas_boca_15():
	links = []
	fechas = []
	for i in list(range(30)):
		links.append('http://www.promiedos.com.ar/fechatotal.php?fecha=' + str(i + 1) + '_1&liga=Primera&temporada=20151&grupo=1')
	for link in links:
		page = requests.get(link)
		fechas.append(BeautifulSoup(page.text, 'html.parser'))
	return fechas

def obtener_fechas_superliga1819():
	links = []
	fechas = []
	for i in list(range(25)):
		links.append('http://www.promiedos.com.ar/fecha.php?fecha=' + str(i + 1) + '_1&_=1560202011604')
	for link in links:
		page = requests.get(link)
		fechas.append(BeautifulSoup(page.text, 'html.parser'))
	return fechas



#def obtener_data_enfrentamiento(fechas):
	#enfrentamientos = []
	#for fecha in fechas:
		#data = fecha.find_all(style="background: #e5e5e5")
	#	data = fecha.findAll('tr',{"style" : "background: #e5e5e5"})
	#	data2 = data.findAll('td')
	#	enfrentamientos.append(data2)
	#print(enfrentamientos)

def obtener_data(fechas):
	enfrentamientos_x_fecha = []
	#fechas = fechas_boca_1718()
	for fecha in fechas:
		#page = requests.get(fecha)
		#page_soup = BeautifulSoup(page.text,'html.parser')
		equipos = fecha.find_all(class_="datoequipo")
		enfrentamientos_x_fecha.append(equipos)
	#print(type(enfrentamientos_x_fecha[0]))
	#print(type(str(enfrentamientos_x_fecha[0][0])))
	#print((enfrentamientos_x_fecha[0][0]))
	#tigres = str(enfrentamientos_x_fecha[0][0])
	#tigre = tigres[51:len(tigres)-7]
	#print(tigre)
	print(len(enfrentamientos_x_fecha))
	print(len(enfrentamientos_x_fecha[0]))
	print(enfrentamientos_x_fecha[1])
	return enfrentamientos_x_fecha

def extraer_equipos(enfrentamientos_x_fecha):
	equipos_x_fecha = []
	equipos_en_orden = []
	
	for fecha in enfrentamientos_x_fecha:
		i = 0
		while i < len(fecha):
			raw_name = str(fecha[i])
			name = raw_name[51:len(raw_name)-7]
			equipos_x_fecha.append(name)
			i = i + 1
		equipos_en_orden.append(equipos_x_fecha)
		equipos_x_fecha = []

		#for equipo in fecha:
		#	raw_name = str(equipo)
		#	name = raw_name[51:len(raw_name)-7]
		#	equipos_x_fecha.append(name)
		#equipos_en_orden.append(equipos_x_fecha)
	print(equipos_en_orden)
	print(len(equipos_en_orden[0]))
	return equipos_en_orden



def obtener_goles(fechas):
	goles_x_enfrentamiento = []
	#fechas = fechas_boca_1718()
	for fecha in fechas:
		#page = requests.get(fecha)
		#page_soup = BeautifulSoup(page.text, 'html.parser')
		goles = fecha.find_all(style="font-size:14px")
		goles_x_enfrentamiento.append(goles)
	#print(goles_x_enfrentamiento)
	#print(len(goles_x_enfrentamiento))
	#print(len(goles_x_enfrentamiento[0]))
	#print(goles_x_enfrentamiento[2])
	#print(goles_x_enfrentamiento)
	return goles_x_enfrentamiento     #Goles_x_enfrentamiento es una lista con 27 posiciones, donde la i-ésima posicion es una lista con los goles de la fecha i. 
									  #Goles_x_enfrentamiento[i][j] me devuelve los goles que hizo el equipo que aparece en la posición j del fixture de la fecha en la fecha i


def extraer_goles(goles_sucios):
	goles_x_fecha = []
	goles_fecha_total = []
	for fecha in goles_sucios:
		print(fecha)
		i = 0
		while i < len(fecha):
			gol = str(fecha[i])
			gol_limpio = gol[29]
			goles_x_fecha.append(gol_limpio)
			print(goles_x_fecha)
			i = i + 1
		goles_fecha_total.append(goles_x_fecha)
		goles_x_fecha = []
	print(goles_fecha_total)
	return goles_fecha_total

def pasar_datos(lista_goles , lista_equipos):
	archivo = open('torneo_superliga_racing.txt','w')
	matriz = []
	for i in range(len(lista_goles)):
		fila_goles = lista_goles[i]
		fila_equipos = lista_equipos[i]
		for j in range(len(fila_equipos)//2):
			s = '' + str([i+1]) + ','
			eq1 = fila_equipos[2*j]
			eq2 = fila_equipos[(2*j)+1]
			gol1 = fila_goles[(2*j)]
			gol2 = fila_goles[(2*j)+1]
			s = s + eq1 + ',' + eq2 + ',' + gol1 + ',' + gol2 #+ '\n'
			archivo.write(s)
			matriz.append(s)
	print(matriz)
	return matriz







#IDEA--> armar una lista para cada fecha que contenga el orden en el que aparecen los equipos en el fixture de la fecha (0 local del primer partido, 1 visitante primer parti)




#page = requests.get(promiedo)


#fecha_soup = BeautifulSoup(page.text, 'html.parser' )

#tabla = fecha_soup.find_all(class_ = "datoequipo")

#equipos = tabla.find(class_="finaliza")

#print(fecha_soup)

#print(tabla)
def main():
	fechas = obtener_fechas_boca_1617()
	#print(fechas)
	#obtener_data(fechas)
	#obtener_goles(fechas)
	#extraer_goles(obtener_goles(fechas))
	#obtener_data_enfrentamiento(fechas)
	#extraer_equipos(obtener_data(fechas))
	pasar_datos(extraer_goles(obtener_goles(fechas)),extraer_equipos(obtener_data(fechas)))
if __name__ == '__main__':
	main()
#print(type(tabla))

#print(equipos)

