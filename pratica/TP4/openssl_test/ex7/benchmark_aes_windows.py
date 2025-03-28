import subprocess
import time
from pathlib import Path

# Configurações
chaves = {
    "aes-128-cbc": "343ca768ab0328d8bd8c161f1630f9ed",
    "aes-192-cbc": "00112233445566778899aabbccddeeff0011223344556677",
    "aes-256-cbc": "f79d41142f2eccb65555250c82bef9ff64270d25a7b9d6e99b222ee99fbf61b8"
}
iv = "aeec6679352fa7f48f7f3568141e0754"

# Arquivos de entrada
arquivos = {
    "1MB": "arquivo_1MB.bin",
    "100MB": "arquivo_100MB.bin",
    "1GB": "arquivo_1GB.bin"
}

# Certifique-se de que os arquivos existem
for nome, caminho in arquivos.items():
    if not Path(caminho).exists():
        print(f"[ERRO] Arquivo '{caminho}' não encontrado!")
        exit(1)

# Executar testes
for tamanho_nome, arquivo_entrada in arquivos.items():
    for algoritmo, chave in chaves.items():
        tempos = []
        print(f"🔒 Iniciando {algoritmo} com arquivo {tamanho_nome}...")
        for i in range(1, 11):
            saida = f"saida_{algoritmo}_{tamanho_nome}_{i}.enc"
            inicio = time.perf_counter()
            subprocess.run([
                "openssl", "enc", f"-{algoritmo}",
                "-nosalt",
                "-in", arquivo_entrada,
                "-out", saida,
                "-K", chave,
                "-iv", iv
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            fim = time.perf_counter()
            duracao = fim - inicio
            tempos.append(duracao)
            print(f"  Execução {i}: {duracao:.2f} segundos")

        # Salvar tempos no arquivo
        with open(f"tempos_{algoritmo}_{tamanho_nome}.txt", "w") as f:
            for tempo in tempos:
                f.write(f"{tempo:.4f}\n")

print("✅ Testes concluídos. Tempos salvos em arquivos .txt.")
