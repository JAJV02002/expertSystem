from tkinter import *
from PIL import Image, ImageTk


# Ruta y etiqueta de las imagenes para facil acceso
imagenes_paises = {
    'Quebec': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/quebec.png', 
    'Banff': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/banff.png',
    'Chicago': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/chicago.png',
    'Canadá': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/canada.png',
    'Montreal': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/montreal.png',
    'Whistler': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/whistler.png',
    'NuevaYork': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/nuevayork.png',
    'Toronto': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/toronto.png',
    'Denali': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/denali.png',
    'LasVegas': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/lasvegas.png',
    'LaHabana': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/lahabana.png',
    'Galapagos': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/galapagos.png',
    'Miami': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/miami.png',
    'Cartagena': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/cartagena.png',
    'MachuPicchu': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/machupicchu.png',
    'Cancún': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/cancun.png',
    'Cusco': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/cusco.png',
    'Amazonas': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/amazonas.png',
    'SaoPaulo': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/saopaulo.png',
    'BuenosAires': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/buenosaires.png',
    'Bariloche': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/bariloche.png',
    'PuntadelEste': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/puntadeleste.png',
    'Santiago': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/santiago.png',
    'Patagonia': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/patagonia.png',
    'Lima': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/lima.png',
    'Oaxaca': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/oaxaca.png',
    'TierradelFuego': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/tierradelfuego.png',
    'RiodeJaneiro': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/riodejaneiro.png',
    'Edimburgo': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/edimburgo.png',
    'Interlaken': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/interlaken.png',
    'Paris': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/paris.png',
    'Florencia': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/florencia.png',
    'Chamonix': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/chamonix.png',
    'Milán': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/milan.png',
    'Viena': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/viena.png',
    'Reykjavik': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/reykjavik.png',
    'Mónaco': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/monaco.png',
    'Atenas': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/atenas.png',
    'CostaBrava': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/costabrava.png',
    'CostaAzul': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/costaazul.png',
    'Praga': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/praga.png',
    'Cracovia': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/cracovia.png',
    'Zúrich': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/zurich.png',
    'Venecia': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/venecia.png',
    'Plitvice': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/plitvice.png',
    'Ibiza': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/ibiza.png',
    'Dublín': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/dublin.png',
    'Tirol': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/tirol.png',
    'Ginebra': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/ginebra.png',
    'Bruselas': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/bruselas.png',
    'Dolomitas': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/dolomitas.png',
    'Hamburgo': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/hamburgo.png',
    'SanPetersburgo': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/sanpetersburgo.png',
    'AlpesSuizos': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/alpessuizos.png',
    'MonteCarlo': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/montecarlo.png',
    'Kyoto': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/kyoto.png',
    'Himalaya': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/nepal.png',
    'HongKong': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/hongkong.png',
    'UlanBator': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/ulanbator.png',
    'Ladakh': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/ladakh.png',
    'Singapur': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/singapur.png',
    'Bhutan': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/bhutan.png',
    'MonteFuji': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/fujisan.png',
    'Tokio': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/tokio.png',
    'AngkorWat': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/angkor.png',
    'Phuket': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/phuket.png',
    'Dubai': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/dubai.png',
    'Jaipur': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/jaipur.png',
    'Bali': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/bali.png',
    'Seul': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/seul.png',
    'Samarcanda': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/samarcanda.png',
    'Cebu': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/cebu.png',
    'Shanghai': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/shanghai.png',
    'Ayutthaya': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/ayutthaya.png',
    'Jeju': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/jeju.png',
    'Osaka': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/osaka.png',
    'Beijing': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/beijing.png',
    'Sapa': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/sapa.png',
    'KualaLumpur': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/kl.png',
    'LuangPrabang': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/luangprabang.png',
    'Maldivas': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/maldivas.png',
    'Bangkok': '/Users/antoniojuarez/Python/Mecatronica/OctavoSem/SistemasExpertos/Proyecto_P1/bangkok.png',


    # Asegúrate de tener imágenes para todos los países y rutas correctas.
}

# Funcion para abrir una ventana en la que se van a recomendar paises a visitar al usuario segun sus preferencias
def mostrar_recomendaciones(destino, clima, presupuesto, actividad):
    ventana_recomendaciones = Toplevel()
    ventana_recomendaciones.title("Recomendaciones de Viaje")
    ventana_recomendaciones.geometry('1300x600')
    ventana_recomendaciones.config(bg='#191970')  # Establecer el color de fondo (Azul medianoche) usando un código hexadecimal

    recomendaciones = ""
    ruta_imagen = ""
 
 ##### Viaje al continente Americano #####   
    if destino == "Continente Americano":
        if clima == "Frio":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Quebec, Canadá"
                    ruta_imagen = imagenes_paises['Quebec']
                elif actividad == "Aventura":
                    recomendaciones = "Parque Nacional Banff, Canadá"
                    ruta_imagen = imagenes_paises['Banff']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Chicago, Estados Unidos"
                    ruta_imagen = imagenes_paises['Chicago']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Montreal, Canadá"
                    ruta_imagen = imagenes_paises['Montreal']
                elif actividad == "Aventura":
                    recomendaciones = "Whistler, Canadá"
                    ruta_imagen = imagenes_paises['Whistler']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Nueva York, Estados Unidos"
                    ruta_imagen = imagenes_paises['NuevaYork']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Toronto, Canadá"
                    ruta_imagen = imagenes_paises['Toronto']
                elif actividad == "Aventura":
                    recomendaciones = "Denali, Alaska, Estados Unidos"
                    ruta_imagen = imagenes_paises['Denali']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Las Vegas, Estados Unidos"
                    ruta_imagen = imagenes_paises['LasVegas']
        elif clima == "Calor":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "La Habana, Cuba"
                    ruta_imagen = imagenes_paises['LaHabana']
                elif actividad == "Aventura":
                    recomendaciones = "Galápagos, Ecuador"
                    ruta_imagen = imagenes_paises['Galapagos']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Miami, Estados Unidos"
                    ruta_imagen = imagenes_paises['Miami']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Cartagena, Colombia"
                    ruta_imagen = imagenes_paises['Cartagena']
                elif actividad == "Aventura":
                    recomendaciones = "Machu Picchu, Perú"
                    ruta_imagen = imagenes_paises['MachuPicchu']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Cancún, México"
                    ruta_imagen = imagenes_paises['Cancún']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Cusco, Perú"
                    ruta_imagen = imagenes_paises['Cusco']
                elif actividad == "Aventura":
                    recomendaciones = "Amazonas, Brasil"
                    ruta_imagen = imagenes_paises['Amazonas']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Sao Paulo, Brasil"
                    ruta_imagen = imagenes_paises['SaoPaulo']
        elif clima == "Templado":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Buenos Aires, Argentina"
                    ruta_imagen = imagenes_paises['BuenosAires']
                elif actividad == "Aventura":
                    recomendaciones = "San Carlos de Bariloche, Argentina"
                    ruta_imagen = imagenes_paises['Bariloche']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Punta del Este, Uruguay"
                    ruta_imagen = imagenes_paises['PuntadelEste']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Santiago, Chile"
                    ruta_imagen = imagenes_paises['Santiago']
                elif actividad == "Aventura":
                    recomendaciones = "Patagonia, Chile"
                    ruta_imagen = imagenes_paises['Patagonia']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Lima, Perú"
                    ruta_imagen = imagenes_paises['Lima']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Oaxaca, México"
                    ruta_imagen = imagenes_paises['Oaxaca']
                elif actividad == "Aventura":
                    recomendaciones = "Tierra del Fuego, Argentina"
                    ruta_imagen = imagenes_paises['TierradelFuego']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Rio de Janeiro, Brasil"
                    ruta_imagen = imagenes_paises['RiodeJaneiro']   
                    
##### Viaje de America a Europa #####             
    if destino == "Continente Europeo":
        if clima == "Frio":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Edimburgo, Escocia"
                    ruta_imagen = imagenes_paises['Edimburgo']
                elif actividad == "Aventura":
                    recomendaciones = "Interlaken, Suiza"
                    ruta_imagen = imagenes_paises['Interlaken']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "París, Francia"
                    ruta_imagen = imagenes_paises['Paris']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Florencia, Italia"
                    ruta_imagen = imagenes_paises['Florencia']
                elif actividad == "Aventura":
                    recomendaciones = "Chamonix, Francia"
                    ruta_imagen = imagenes_paises['Chamonix']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Milán, Italia"
                    ruta_imagen = imagenes_paises['Milán']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Viena, Austria"
                    ruta_imagen = imagenes_paises['Viena']
                elif actividad == "Aventura":
                    recomendaciones = "Reykjavik, Islandia"
                    ruta_imagen = imagenes_paises['Reykjavik']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Mónaco, Mónaco"
                    ruta_imagen = imagenes_paises['Mónaco']
        elif clima == "Calor":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Atenas, Grecia"
                    ruta_imagen = imagenes_paises['Atenas']
                elif actividad == "Aventura":
                    recomendaciones = "Costa Brava, España"
                    ruta_imagen = imagenes_paises['CostaBrava']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Costa Azul, Francia"
                    ruta_imagen = imagenes_paises['CostaAzul']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Praga, República Checa"
                    ruta_imagen = imagenes_paises['Praga']
                elif actividad == "Aventura":
                    recomendaciones = "Cracovia, Polonia"
                    ruta_imagen = imagenes_paises['Cracovia']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Zúrich, Suiza"
                    ruta_imagen = imagenes_paises['Zúrich']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Venecia, Italia"
                    ruta_imagen = imagenes_paises['Venecia']
                elif actividad == "Aventura":
                    recomendaciones = "Lagos de Plitvice, Croacia"
                    ruta_imagen = imagenes_paises['Plitvice']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Ibiza, España"
                    ruta_imagen = imagenes_paises['Ibiza']
        elif clima == "Templado":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Dublín, Irlanda"
                    ruta_imagen = imagenes_paises['Dublín']
                elif actividad == "Aventura":
                    recomendaciones = "Tirol, Austria"
                    ruta_imagen = imagenes_paises['Tirol']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Ginebra, Suiza"
                    ruta_imagen = imagenes_paises['Ginebra']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Bruselas, Bélgica"
                    ruta_imagen = imagenes_paises['Bruselas']
                elif actividad == "Aventura":
                    recomendaciones = "Escalada en Dolomitas, Italia"
                    ruta_imagen = imagenes_paises['Dolomitas']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Hamburgo, Alemania"
                    ruta_imagen = imagenes_paises['Hamburgo']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "San Petersburgo, Rusia"
                    ruta_imagen = imagenes_paises['SanPetersburgo']
                elif actividad == "Aventura":
                    recomendaciones = "Alpes Suizos, Suiza"
                    ruta_imagen = imagenes_paises['AlpesSuizos']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Monte Carlo, Mónaco"
                    ruta_imagen = imagenes_paises['MonteCarlo']
 
##### Viaje de America a Asia ##### 
    if destino == "Continente Asiático":
        if clima == "Frio":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Kyoto, Japón"
                    ruta_imagen = imagenes_paises['Kyoto']
                elif actividad == "Aventura":
                    recomendaciones = "Himalaya, Nepal"
                    ruta_imagen = imagenes_paises['Himalaya']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Hong Kong, China"
                    ruta_imagen = imagenes_paises['HongKong']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Ulan Bator, Mongolia"
                    ruta_imagen = imagenes_paises['UlanBator']
                elif actividad == "Aventura":
                    recomendaciones = "Ladakh, India"
                    ruta_imagen = imagenes_paises['Ladakh']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Singapur"
                    ruta_imagen = imagenes_paises['Singapur']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Bhután"
                    ruta_imagen = imagenes_paises['Bhutan']
                elif actividad == "Aventura":
                    recomendaciones = "Monte Fuji, Japón"
                    ruta_imagen = imagenes_paises['MonteFuji']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Tokio, Japón"
                    ruta_imagen = imagenes_paises['Tokio']
        elif clima == "Calor":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Angkor Wat, Camboya"
                    ruta_imagen = imagenes_paises['AngkorWat']
                elif actividad == "Aventura":
                    recomendaciones = "Phuket, Tailandia"
                    ruta_imagen = imagenes_paises['Phuket']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Dubái, Emiratos Árabes Unidos"
                    ruta_imagen = imagenes_paises['Dubai']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Jaipur, India"
                    ruta_imagen = imagenes_paises['Jaipur']
                elif actividad == "Aventura":
                    recomendaciones = "Bali, Indonesia"
                    ruta_imagen = imagenes_paises['Bali']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Seúl, Corea del Sur"
                    ruta_imagen = imagenes_paises['Seul']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Samarcanda, Uzbekistán"
                    ruta_imagen = imagenes_paises['Samarcanda']
                elif actividad == "Aventura":
                    recomendaciones = "Cebú, Filipinas"
                    ruta_imagen = imagenes_paises['Cebu']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Shanghái, China"
                    ruta_imagen = imagenes_paises['Shanghai']
        elif clima == "Templado":
            if presupuesto == "500 - 1,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Ayutthaya, Tailandia"
                    ruta_imagen = imagenes_paises['Ayutthaya']
                elif actividad == "Aventura":
                    recomendaciones = "Jeju, Corea del Sur"
                    ruta_imagen = imagenes_paises['Jeju']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Osaka, Japón"
                    ruta_imagen = imagenes_paises['Osaka']
            elif presupuesto == "1,500 - 2,500 USD":
                if actividad == "Cultura":
                    recomendaciones = "Beijing, China"
                    ruta_imagen = imagenes_paises['Beijing']
                elif actividad == "Aventura":
                    recomendaciones = "Sapa, Vietnam"
                    ruta_imagen = imagenes_paises['Sapa']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Kuala Lumpur, Malasia"
                    ruta_imagen = imagenes_paises['KualaLumpur']
            else:  # (2,500 - 5,000 USD)
                if actividad == "Cultura":
                    recomendaciones = "Luang Prabang, Laos"
                    ruta_imagen = imagenes_paises['LuangPrabang']
                elif actividad == "Aventura":
                    recomendaciones = "Maldivas"
                    ruta_imagen = imagenes_paises['Maldivas']
                else:  # (Actividad = Lujo y compras)
                    recomendaciones = "Bangkok, Tailandia"
                    ruta_imagen = imagenes_paises['Bangkok']              
                                                
##### Para mostrar el mensaje de recomendación #####    
    if recomendaciones:
        mensaje = f"Considerando que viaja hacia {destino}, prefiere un clima {clima},un presupuesto de {presupuesto}, e interés en {actividad}. Le recomendamos visitar: {recomendaciones}"
        label_mensaje = Label(ventana_recomendaciones, text=mensaje, bg='#191970', fg='white')
        label_mensaje.pack()
        
        if ruta_imagen:
            imagen_original = Image.open(ruta_imagen)
            
            # Para reducir la imagen a la mitad de su tamaño original:
            nuevo_tamaño = (imagen_original.width // 2, imagen_original.height // 2)
            
            # Si se requiere un tamaño específico, puedes especificar las dimensiones directamente:
            # nuevo_tamaño = (300, 200)
            
            imagen_redimensionada = imagen_original.resize(nuevo_tamaño)
            foto = ImageTk.PhotoImage(imagen_redimensionada)
            
            label_imagen = Label(ventana_recomendaciones, image=foto)
            label_imagen.image = foto  # Mantener una referencia
            label_imagen.place(x = 400 , y = 25)

    else:
        mensaje = "Lo sentimos, no hay recomendaciones que coincidan con sus preferencias."
        Label(ventana_recomendaciones, text=mensaje, bg='#191970', fg='white').pack()

    botonCerrar = Button(ventana_recomendaciones, text="Cerrar", command=ventana_recomendaciones.destroy)
    botonCerrar.config(bg='white', fg='blue', highlightbackground='#191970', highlightthickness=0, font=('Arial', 12), relief='raised', bd=2)
    botonCerrar.place(x=550, y=550)

# Funcion para abrir una ventana en la que el usuario pueda dar más caracteristicas del viaje que quiere hacer
def abrir_ventana_continente():
    destino = destino_seleccionado.get()
    ventana_continente = Toplevel()
    ventana_continente.title(f"Recomendaciones para {destino}") # Establecer el título de la ventana
    ventana_continente.geometry('755x300') # Establecer el tamaño de la ventana
    ventana_continente.config(bg='#191970')  # Establecer el color de fondo (Azul medianoche) usando un código hexadecimal
    
    
    Label(ventana_continente, text="Seleccione las opciones que se ajusten a sus preferencias:", bg='#191970', fg='white').place(x = 125 , y = 25)
    
    marco_clima = LabelFrame(ventana_continente, text="Preferencia Climática", padx=5, pady=5, bg='#add8e6', fg='#191970')
    marco_clima.place(x=50, y=75)
    clima_seleccionado = StringVar(value=" ")
    for opcion in ["Frio" , "Calor" , "Templado"]:
        Radiobutton(marco_clima, text=opcion, variable=clima_seleccionado, value=opcion, bg='#add8e6', fg='#191970', selectcolor='blue').pack(anchor='w')
    
    marco_presupuesto = LabelFrame(ventana_continente, text="Presupuesto", padx=5, pady=5, bg='#add8e6', fg='#191970')
    marco_presupuesto.place(x=295, y=75)
    presupuesto_seleccionado = StringVar(value=" ")
    for opcion in ["500 - 1,500 USD", "1,500 - 2,500 USD", "2,500 - 5,000 USD"]:
        Radiobutton(marco_presupuesto, text=opcion, variable=presupuesto_seleccionado, value=opcion, bg='#add8e6', fg='#191970', selectcolor='blue').pack(anchor='w')

    marco_actividades = LabelFrame(ventana_continente, text="Actividades de Interés", padx=5, pady=5, bg='#add8e6', fg='#191970')
    marco_actividades.place(x=550, y=75)
    actividad_seleccionada = StringVar(value=" ")
    for opcion in ["Cultura", "Aventura", "Compras y Lujo"]:
        Radiobutton(marco_actividades, text=opcion, variable=actividad_seleccionada, value=opcion, bg='#add8e6', fg='#191970', selectcolor='blue').pack(anchor='w')
    
    botonRecomendaciones = Button(ventana_continente, text="Mostrar Recomendaciones", 
           command=lambda: mostrar_recomendaciones(destino, clima_seleccionado.get(), 
                                                   presupuesto_seleccionado.get(), actividad_seleccionada.get()))
    botonRecomendaciones.config(bg='white', fg='blue', highlightbackground='#191970', highlightthickness=0, font=('Arial', 12), relief='raised', bd=2)
    botonRecomendaciones.place(x=200, y=250)
    
    botonRegresar = Button(ventana_continente, text="Regresar", command=ventana_continente.destroy)
    botonRegresar.config(bg='white', fg='blue', highlightbackground='#191970', highlightthickness=0, font=('Arial', 12), relief='raised', bd=2)
    botonRegresar.place(x=400, y=250)

# Configuración de la ventana principal
root = Tk()
root.title("Recomendaciones de viaje")
root.geometry('520x300')
root.config(bg='#191970')  # Establecer el color de fondo (Azul medianoche) usando un código hexadecimal

Label(root, text="Seleccione el continente que más le gustaría visitar:", bg='#191970', fg='white').place(x = 125 , y = 25)

marco_destino = LabelFrame(root, text="¿Qué continente le gustaría visitar?", padx=5, pady=5 , bg='#add8e6', fg='#191970')
marco_destino.place(x=150, y=75)
destino_seleccionado = StringVar(value=" ")
for opcion in ["Continente Americano", "Continente Europeo", "Continente Asiático"]:
    Radiobutton(marco_destino, text=opcion, variable=destino_seleccionado, value=opcion, bg='#add8e6', fg='#191970', selectcolor='blue').pack(anchor='w')

botonPreferencias = Button(root, text="Continuar", command=abrir_ventana_continente)
botonPreferencias.config(bg='white', fg='blue', highlightbackground='#191970', highlightthickness=0, font=('Arial', 12), relief='raised', bd=2)
botonPreferencias.place(x=225, y=250)

root.mainloop()