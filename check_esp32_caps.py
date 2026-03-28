import socket
import json
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

try:
    # Send hello message first
    hello = {'v': 1, 't': 'hello', 'seq': 1, 'ts': int(time.time() * 1000)}
    msg = json.dumps(hello)
    sock.sendto(msg.encode(), ('192.168.4.1', 9000))
    print('Sent hello message')

    # Wait for ACK and capabilities
    responses = []
    start_time = time.time()
    while time.time() - start_time < 3:
        try:
            data, addr = sock.recvfrom(2048)
            response = data.decode()
            responses.append(response)
            print(f'Response {len(responses)}:')
            print(response)
            print()

            # Check if we got capabilities
            try:
                resp_json = json.loads(response)
                if resp_json.get('t') == 'cap':
                    print('Found capabilities!')
                    if 'p' in resp_json and 'pins' in resp_json['p']:
                        pins = resp_json['p']['pins']
                        print('Configured pins:')
                        for pin_name, pin_num in pins.items():
                            print(f'  {pin_name}: GPIO{pin_num}')

                        has_acc = 'acc' in pins
                        has_spare = 'spare' in pins
                        print(f'\nACC relay: {"YES" if has_acc else "NO"}')
                        print(f'SPARE relay: {"YES" if has_spare else "NO"}')
                    break
            except:
                pass

        except socket.timeout:
            break

    if not responses:
        print('No responses received')

except Exception as e:
    print(f'Error: {e}')
finally:
    sock.close()