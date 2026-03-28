#!/usr/bin/env python3
"""
Monitor UDP traffic to check if ACC/SPARE commands are being sent
"""
import socket
import json

def main():
    # Monitor UDP traffic to ESP32
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 9000))  # Listen on port 9000
    sock.settimeout(1.0)

    print('Monitoring UDP traffic on port 9000...')
    print('Press Ctrl+C to stop')

    try:
        while True:
            try:
                data, addr = sock.recvfrom(2048)
                print(f'\nReceived {len(data)} bytes from {addr}:')
                try:
                    msg = json.loads(data.decode())
                    print(f'  JSON: {msg}')
                    if 'p' in msg and isinstance(msg['p'], dict):
                        payload = msg['p']
                        print(f'  Payload: acc={payload.get("acc", "?")}, spare={payload.get("spare", "?")}, led={payload.get("led", "?")}, laser={payload.get("laser", "?")}')
                except Exception as e:
                    print(f'  Raw: {data[:100]}... (not JSON: {e})')
            except socket.timeout:
                print('.', end='', flush=True)
            except KeyboardInterrupt:
                break
    except Exception as e:
        print(f'Error: {e}')
    finally:
        sock.close()

if __name__ == '__main__':
    main()