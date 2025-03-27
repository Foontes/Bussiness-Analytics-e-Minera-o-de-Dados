import os
from PIL import Image

pasta_origem = "../../../../img/garfield"
pasta_destino = "../../../../img/garfield_black_white"


os.makedirs(pasta_destino, exist_ok=True)

for arquivo in os.listdir(pasta_origem):
    caminho_completo = os.path.join(pasta_origem, arquivo)

    if arquivo.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        imagem = Image.open(caminho_completo).convert("L")

        caminho_destino = os.path.join(pasta_destino, arquivo)
        imagem.save(caminho_destino)

        print(f"Convertido: {arquivo} → {caminho_destino}")

print("Todas as imagens foram convertidas com sucesso!")
