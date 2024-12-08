# mud-lm
Emulador de juego estilo MUD utilizando ollama + LLM
## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- ollama
- LLM

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/fmancini/mud-lm/mud-lm.git
    cd mud-lm
    ```

2. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura ollama y LLM según las instrucciones de sus respectivas documentaciones.

5. Ejecuta el emulador:
    ```bash
    game_llm.py
    ```