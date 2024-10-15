import flet as ft
import random

def verifica_adivinar(e,page):
    adivinar_usuario=int(entrada_numero.value)
    
    if adivinar_usuario==numero_Secreto:
        texto_resultado.value="¡felicidadea! adivinaste el numero secreto"
        boton_adivinar.disabled=True
        page.add(ft.Audio(src="victor.mp3,autoplay=True"))
    elif adivinar_usuario < numero_secreto:
        texto_resultado.value="¡Fallase! El numero sereto es mayor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
    else:
        texto_resultado.value="¡Fallaste El numero secreto es menor"
        page.add(ft.Audio(src="Boing.mp3",autoplay=True))
    entrada_numero.value=""
    page.update()
    
    #funciones principal
    def main(page: ft.page):
        #variables globales
        
