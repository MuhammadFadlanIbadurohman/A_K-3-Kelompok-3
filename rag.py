# ==========================================
# SIMULASI RESOURCE ALLOCATION GRAPH (RAG)
# SERVER LAYANAN AKADEMIK KAMPUS
# ==========================================

# Hubungan resource yang dialokasikan
allocation = {
    "DB": "P1",
    "PR": "P2",
    "LK": "P3"
}

# Hubungan proses yang meminta resource
request = {
    "P1": "PR",
    "P2": "LK",
    "P3": "DB"
}

print("====================================")
print(" RESOURCE ALLOCATION GRAPH (RAG)")
print(" SERVER LAYANAN AKADEMIK")
print("====================================")

print("\n1. RESOURCE YANG DIALOKASIKAN")
for resource, process in allocation.items():
    print(resource, "->", process)

print("\n2. RESOURCE YANG DIMINTA")
for process, resource in request.items():
    print(process, "->", resource)

print("\n3. GRAF HUBUNGAN")

for resource, process in allocation.items():
    print(resource, "->", process)

for process, resource in request.items():
    print(process, "->", resource)

print("\n4. SIKLUS DEADLOCK")

print("DB -> P1 -> PR -> P2 -> LK -> P3 -> DB")

print("\n5. ANALISIS")

print("P1 memegang DB dan menunggu PR.")
print("P2 memegang PR dan menunggu LK.")
print("P3 memegang LK dan menunggu DB.")

print("\nTerbentuk siklus melingkar.")
print("Dengan satu instance setiap resource,")
print("siklus ini menunjukkan kondisi deadlock.")
