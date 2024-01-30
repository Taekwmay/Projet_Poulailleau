from bluepy.btle import Scanner


scanner = Scanner()
print("Begin device scan")
while True:
    devices = scanner.scan(timeout=3.0)

    for device in devices:
        if (device.addr=="s6:c6:c7:39:a2:e8" or device.addr=="d6:1c:bf:b7:76:62" or device.addr=="d7:ef:13:27:15:29"):
        print(
            f"Device found {device.addr} ({device.addrType}), "
            f"RSSI={device.rssi} dB"
        )
        for adtype, description, value in device.getScanData():
            print(f"  ({adtype}) {description} = {value}")

