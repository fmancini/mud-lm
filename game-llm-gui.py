import requests
import json
import tkinter as tk
from tkinter import simpledialog, messagebox

def get_game_dialogue(prompt):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": "llama3.2:latest",  # o cualquier otro modelo que tengas en Ollama
        "system": "Eres un narrador de juegos de rol fantásticos",
        "prompt": prompt
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        # Ollama devuelve respuestas línea por línea, necesitamos concatenarlas
        full_response = ""
        for line in response.text.splitlines():
            if line:
                data = json.loads(line)
                if 'response' in data:
                    full_response += data['response']
                
        return full_response.strip()
    except Exception as e:
        print(f"Error al comunicarse con Ollama: {e}")
        return "Error en la generación del diálogo"

def start_game_gui():
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Genera el saludo inicial
    welcome = get_game_dialogue("Genera un saludo para dar la bienvenida a un nuevo jugador")
    player_name = simpledialog.askstring("Nombre del jugador", f"{welcome}\nIngresa tu nombre:")
    points = 0
    
    # Define las situaciones base
    scenarios = [
        "una cueva oscura",
        "un troll en el camino", 
        "un libro mágico misterioso"
    ]
    
    for scenario in scenarios:
        # Genera la descripción y opciones
        prompt = f"Describe una situación de aventura con {scenario} y da 2 opciones numeradas para resolver"
        question = get_game_dialogue(prompt)
        
        respuesta = simpledialog.askstring("Situación", f"{question}\nElige (1/2): ")
        
        # Genera el resultado
        result_prompt = f"El jugador eligió la opción {respuesta}. Genera un resultado para esta elección"
        resultado = get_game_dialogue(result_prompt)
        
        if respuesta == "1":
            points += 10
            messagebox.showinfo("Resultado", f"{resultado}\nHas ganado 10 puntos. Puntos totales: {points}")
        else:
            messagebox.showinfo("Resultado", f"{resultado}\nPuntos actuales: {points}")

    # Final del juego
    ending = get_game_dialogue(f"Genera un mensaje de despedida para {player_name} que obtuvo {points} puntos")
    messagebox.showinfo("Fin del juego", ending)

    root.destroy()  # Cierra la ventana principal

if __name__ == "__main__":
    start_game_gui()