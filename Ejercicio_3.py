#Usando procesos, abre tres procesos,
#cada uno de los cuales debe….
#P1: debe abrir el bloc de notas/editor de texto del sistema que uses
#P2: debes esperar 5 segundos para cambiar la prioridad de P1
#P3: se lanza 2 segundos después de P2 haya arrancado y 
#mata a P1 al instante
#¿Qué es lo que ocurre durante la ejecución?
#¿Termina el programa correctamente?¿Cómo podrías solucionarlo?
#OPCIONAL +0,5: ¿Qué mecanismo de los estudiados te permitiría sincronizar
# la muerte de P1?Describe  todo lo que se te ocurra al respecto 

import os
import psutil
import time
import subprocess
import multiprocessing
import sys

def P1():
    print(f"Proceso1 con PID: {os.getpid()} creado.")
    subprocess.run(["cmd.exe"])

def P2():
    print(f"Proceso2 con PID: {os.getpid()} creado.")
    time.sleep(5)
    cambiar_prioridad_p1()

def cambiar_prioridad_p1():
    for process in psutil.process_iter(['pid','name']):
        if process.info['name'] == "cmd.exe" and int(process.info['pid']) != os.getpid():
            subprocess.check_output("wmic process where processid=\""+str(process.info['pid'])+"\" CALL   setpriority \"below normal\"")
            print("Prioridad cambiada")

def P3():
    print(f"Proceso3 con PID: {os.getpid()} creado.")
    time.sleep(2)
    for process in psutil.process_iter(['pid','name']):
        if process.info['name'] == "cmd.exe" and int(process.info['pid']) != os.getpid():
            subprocess.run(["taskkill","/pid",str(process.info['pid']),"/f"])
            print("Proceso 1 muerto")
    

if __name__ == "__main__":

    proceso1 = multiprocessing.Process(name="P1",target=P1)
    proceso2 = multiprocessing.Process(name="P2",target=P2)
    proceso3 = multiprocessing.Process(name="P3",target=P3)

    proceso1.start()
    proceso2.start()
    proceso3.start()

    proceso1.join()
    proceso2.join()
    proceso3.join()

#Qué es lo que ocurre durante la ejecución?

#cuando se inicia el programa, se crean 3 procesos, el primero abre el cmd,
#  el segundo que esta dormido 5 segundos, despues de que se inicie el primero,
#  cambia la prioridad del proceso 1, y el tercero que esta dormido 2 segundos y
#  se inicia cuando se activa el segundo pero con los 2 segundos de sleep,
#  mata al proceso1, y por ende cierra el cmd.


#¿Termina el programa correctamente?
#A mi me termina bien, ya que cierra el cmd y termina el programa, y
#  vuelve al terminal por defecto de python.
# ¿Cómo podrías solucionarlo?


