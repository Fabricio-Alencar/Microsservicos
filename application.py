
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from rendenizar_projetos.app import router as rendenizar_router
from criar_projetos.app import router as criar_router
from gerenciar_projetos.app import router as gerenciar_router
from gerenciar_colaboradores.app import router as colaboradores_router


app = FastAPI(title="API Principal")

# Configuração global de CORS
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # <-- libera todas as origens
    #allow_origins=origins,         # libera só os sites listados acima
    allow_credentials=True,         # permite envio de cookies/autenticação
    allow_methods=["*"],            # permite todos os métodos (GET, POST, PUT, DELETE etc)
    allow_headers=["*"]             # permite todos os cabeçalhos HTTP
)


# Registrar os módulos/microserviços
app.include_router(rendenizar_router)
app.include_router(criar_router)
app.include_router(gerenciar_router)
app.include_router(colaboradores_router)


# 🩺 Endpoint de verificação
@app.get("/")
def status():
    return {"status": "API está no ar 🚀"}
