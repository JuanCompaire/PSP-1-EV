#dado el siguiente código hazlo multihilo(0,5 puntos),
# consigue que la información pueda aparecer ordenada por pantalla y
# en el fichero se escriba de manera ordenada(2 puntos)
import os
import psutil
import time
import subprocess
import multiprocessing
import sys
import threading
import tempfile

file_name = os.path.join(tempfile.gettempdir(), os.urandom(24).hex())


def code(name,lock):
        time.sleep(10)
        with lock:
            print("codigo limpio fue escrito por "+str(name))
            subprocess.run(["ping", "google.com"])
            with open(file_name, 'w') as f:
                print("guardando en "+file_name)
                f.write("codigo limpio fue escrito por "+str(name)) 

lock = threading.Lock()

h = threading.Thread(target=code, args=("juan",lock))
h.start()

h1 = threading.Thread(target=code, args=("juan",lock))
h1.start()

h2 = threading.Thread(target=code, args=("juan",lock))
h2.start()


h.join()
h2.join()

