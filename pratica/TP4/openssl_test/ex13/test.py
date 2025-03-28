from pathlib import Path

for i in range(1, 11):
    size1 = Path(f"M{i}.txt").stat().st_size
    size2 = Path(f"M{i}_p.txt").stat().st_size
    print(f"M{i}.txt: {size1} bytes | M{i}_p.txt: {size2} bytes")
