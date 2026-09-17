# simulate_ble.py


import random, requests, time


URL = 'http://localhost:8000/api/ingest'


print("Starting BLE Mesh Simulator...")
print("Targeting Zone 3 for Critical Compression Cascade...\n")

density = 50

while True:
    # Baseline traffic for normal zones
    requests.post(URL, json = {'zone': "Zone 1", 'density': random.randint(40, 60)})
    requests.post(URL, json = {'zone': "Zone 2", 'density': random.randint(55, 75)})

    density += random.randint(15, 40) # Simulated bottleneck spike in Zone 3

    print(f"[EDGE NODE] Broadcasting Zone 3 Density: {density}")

    requests.post(URL, json = {'zone': "Zone 3", 'density': density})

    time.sleep(1) # Send every sec