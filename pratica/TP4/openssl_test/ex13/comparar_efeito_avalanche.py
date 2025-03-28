import os

def contar_bits_diferentes(bin1, bin2):
    dif = 0
    for b1, b2 in zip(bin1, bin2):
        xor = b1 ^ b2
        dif += bin(xor).count('1')
    return dif

print("Comparando os arquivos cifrados (efeito avalanche):\n")

for i in range(1, 11):
    nome1 = f"C{i}.bin"
    nome2 = f"C{i}_p.bin"
    if not os.path.exists(nome1) or not os.path.exists(nome2):
        print(f"[!] Arquivos {nome1} ou {nome2} não encontrados.")
        continue

    with open(nome1, "rb") as f1, open(nome2, "rb") as f2:
        c1 = f1.read()
        c2 = f2.read()
        bits_dif = contar_bits_diferentes(c1, c2)
        taxa = bits_dif / 128 * 100
        print(f"C{i} x C{i}_p → {bits_dif} bits diferentes ({taxa:.2f}%)")
