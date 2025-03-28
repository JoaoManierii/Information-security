from pathlib import Path

for i in range(1, 11):
    Path(f"M{i}.txt").unlink(missing_ok=True)
    Path(f"M{i}_p.txt").unlink(missing_ok=True)

original = [
    "abcdefghijklmno1",
    "abcdefghijklmno2",
    "abcdefghijklmno3",
    "abcdefghijklmno4",
    "abcdefghijklmno5",
    "abcdefghijklmno6",
    "abcdefghijklmno7",
    "abcdefghijklmno8",
    "abcdefghijklmno9",
    "abcdefghijklmnoA"
]

modificado = [
    "abcdefghijklmnoX",
    "abcdefghijklmnoY",
    "abcdefghijklmnoZ",
    "abcdefghijklmnoW",
    "abcdefghijklmnoQ",
    "abcdefghijklmnoE",
    "abcdefghijklmnoR",
    "abcdefghijklmnoT",
    "abcdefghijklmnoU",
    "abcdefghijklmnoI"
]

for i in range(10):
    with open(f"M{i+1}.txt", "wb") as f:
        f.write(original[i].encode("utf-8"))
    with open(f"M{i+1}_p.txt", "wb") as f:
        f.write(modificado[i].encode("utf-8"))

print("✅ Arquivos criados com exatamente 16 bytes.")
