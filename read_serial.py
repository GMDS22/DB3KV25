import serial, time
port='COM30'
try:
    s=serial.Serial(port,115200,timeout=1)
    print('opened',port)
    t0=time.time()
    while time.time()-t0<5:
        line=s.readline()
        if line:
            print(line.decode(errors='replace').rstrip())
    s.close()
except Exception as e:
    print('err',e)
