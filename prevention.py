# ==========================================
# SIMULASI PENCEGAHAN DEADLOCK
# METODE RESOURCE ORDERING
# SERVER LAYANAN AKADEMIK
# ==========================================

# Urutan resource yang telah ditetapkan
resource_order = {
    "DB": 1,
    "PR": 2,
    "LK": 3
}

# Kebutuhan resource setiap proses
processes = {
    "P1": ["DB", "PR"],
    "P2": ["DB", "LK"],
    "P3": ["DB", "PR", "LK"]
}

print("====================================")
print(" SIMULASI PENCEGAHAN DEADLOCK")
print(" METODE RESOURCE ORDERING")
print("====================================")

print("\nUrutan resource:")
print("DB -> PR -> LK")

print("\nPemeriksaan urutan setiap proses:")

for process, resources in processes.items():

    ordered_resources = sorted(
        resources,
        key=lambda x: resource_order[x]
    )

    print("\nProses:", process)
    print("Permintaan awal:", resources)
    print("Urutan yang diwajibkan:", ordered_resources)

    if resources == ordered_resources:
        print("Status: SESUAI ATURAN")
    else:
        print("Status: URUTAN PERLU DIPERBAIKI")

print("\n====================================")
print(" KESIMPULAN")
print("====================================")

print("Semua proses harus mengikuti urutan")
print("DB -> PR -> LK.")

print("Urutan global ini mencegah circular wait")
print("dalam model resource ordering.")
