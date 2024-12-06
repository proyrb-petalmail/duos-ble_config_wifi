import socket
import os

def configure_wifi(ssid, password):
    config = f"""
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={{
    ssid="{ssid}"
    psk="{password}"
}}
"""
    with open("/etc/wpa_supplicant.conf", "w") as f:
        f.write(config)
    os.system("wpa_cli -i wlan0 reconfigure")
    print("Wi-Fi configuration updated.")

def main():
    # 创建 BLE 监听套接字
    sock = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_RAW, socket.BTPROTO_HCI)
    sock.bind((0,))

    print("Listening for BLE data...")
    while True:
        data = sock.recv(1024)
        if b"SSID" in data and b"PWD" in data:
            ssid = data.decode().split("SSID:")[1].split("PWD:")[0].strip()
            password = data.decode().split("PWD:")[1].strip()
            print(f"Received SSID: {ssid}, Password: {password}")
            configure_wifi(ssid, password)
            break

if __name__ == "__main__":
    main()
