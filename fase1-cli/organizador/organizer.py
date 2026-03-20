# organizador de arquivos, vai receber um caminho e vai organizar os arquivos dentro dele 
# organizar em pastas
# imagens/   → .jpg .jpeg .png .gif .svg
# Documents/ → .pdf .txt .docx .odt
# videos/    → .mp4 .mkv .avi .mov
# audio/     → .mp3 .wav .flac
# outros/    → qualquer coisa que não se encaixar

# ou seja, o programa vai receber esse caminho, criar os diretorios das subfolders e jogar ( move ) todos os arquivos 
# do folder ( caminho dado ) para cada um desses novos diretorios

from pathlib import Path
import os
import shutil

print("----File Organizer----")
print(f"You are in {Path.cwd()} folder")
p = input("Write the Path of the folder that you wanna organize: ")
print(f"organizando {p}...")
(Path(p) / 'Imagens').mkdir(exist_ok=True)
(Path(p) / 'Documents').mkdir(exist_ok=True)
(Path(p) / 'Vídeos').mkdir(exist_ok=True)
(Path(p) / 'Áudios').mkdir(exist_ok=True)
(Path(p) / 'Others').mkdir(exist_ok=True)

categorias = {
    '.jpg': 'Imagens',
    '.jpeg': 'Imagens',
    '.png': 'Imagens',
    '.gif': 'Imagens',
    '.svg': 'Imagens',
    '.pdf': 'Documents',
    '.txt': 'Documents',
    '.docx': 'Documents',
    '.odt': 'Documents',
    '.mp4': 'Vídeos',
    '.mkv': 'Vídeos',
    '.mov': 'Vídeos',
    '.avi': 'Vídeos',
    '.mp3': 'Áudio', 
    '.wav': 'Áudio',
    '.flac': 'Áudio',
}

contador_arquivo = 0

for arquivo in Path(p).iterdir():

    if arquivo.is_file():
        extensao = arquivo.suffix
        pasta_destino = categorias.get(extensao, 'Others') 
        
        shutil.move(arquivo, Path(p) / pasta_destino)
        print(f"{arquivo} -> {pasta_destino}")
        contador_arquivo += 1

print(f"{contador_arquivo} files organized!")