import sys
from app import create_app

# Obtém os parâmetros de inicializao
config = 'development'
if "--debug" in sys.argv:
    config = 'development'
elif "--production" in sys.argv:
    config = "production"


# Cria o App
app = create_app(config)

# Inicia o App
if __name__ == "__main__":
    if config == 'development':
        app.run(debug=True)

