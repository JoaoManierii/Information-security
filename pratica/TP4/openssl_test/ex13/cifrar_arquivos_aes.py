import subprocess
from pathlib import Path



chave = "a3f536b587c72ad2bb2f18619d768ec9"

for i in range(1, 11):
    arquivo_normal = f"M{i}.txt"
    arquivo_modificado = f"M{i}_p.txt"
    if not Path(arquivo_normal).exists():
        print(f"[ERRO] {arquivo_normal} não encontrado.")
        continue
    if not Path(arquivo_modificado).exists():
        print(f"[ERRO] {arquivo_modificado} não encontrado.")
        continue

    saida_normal = f"C{i}.bin"
    saida_modificado = f"C{i}_p.bin"

    subprocess.run([
        "openssl", "enc", "-aes-128-ecb", "-nosalt", "-nopad",
        "-in", arquivo_normal,
        "-out", saida_normal,
        "-K", chave
    ])

    subprocess.run([
        "openssl", "enc", "-aes-128-ecb", "-nosalt", "-nopad",
        "-in", arquivo_modificado,
        "-out", saida_modificado,
        "-K", chave
    ])

    print(f"[OK] M{i}.txt e M{i}_p.txt cifrados.")
