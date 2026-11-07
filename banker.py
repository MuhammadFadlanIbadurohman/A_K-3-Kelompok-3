
# ==========================================
# SIMULASI ALGORITMA BANKER
# Kasus: Server Layanan Akademik Kampus
# Resource: DB, PR, LK
# ==========================================

processes = ["P1", "P2", "P3"]

# Matriks Allocation
allocation = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Matriks Max
max_need = [
    [1, 1, 0],
    [1, 1, 1],
    [1, 1, 1]
]

# Matriks Available
available = [0, 0, 0]

# Menghitung matriks Need
need = []

for i in range(len(processes)):
    row = []
    for j in range(3):
        row.append(max_need[i][j] - allocation[i][j])
    need.append(row)

# Menampilkan matriks
print("================================")
print(" SIMULASI ALGORITMA BANKER")
print(" SERVER LAYANAN AKADEMIK")
print("================================")

print("\nMatriks Allocation:")
for i in range(3):
    print(processes[i], allocation[i])

print("\nMatriks Max:")
for i in range(3):
    print(processes[i], max_need[i])

print("\nMatriks Need:")
for i in range(3):
    print(processes[i], need[i])

print("\nMatriks Available:")
print(available)

# Algoritma pemeriksaan safe state
work = available.copy()
finish = [False] * len(processes)
safe_sequence = []

while True:
    found = False

    for i in range(len(processes)):
        if not finish[i]:
            if all(need[i][j] <= work[j] for j in range(3)):

                for j in range(3):
                    work[j] += allocation[i][j]

                finish[i] = True
                safe_sequence.append(processes[i])
                found = True
                break

    if not found:
        break

# Menampilkan hasil
print("\n================================")
print(" HASIL PEMERIKSAAN")
print("================================")

if all(finish):
    print("STATUS: SAFE STATE")
    print("Urutan aman:", " -> ".join(safe_sequence))
else:
    print("STATUS: UNSAFE STATE")
    print("Tidak ditemukan safe sequence.")
