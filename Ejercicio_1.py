#Implementa en python un código de Productor Consumidor mediante
#cola sincronizada tal que:
#-El productor produce números enteros mayor que 100 y
#menor que 500(Aleatorios),
#el tiempo de espera entre la generación de un número y
#otro es de PT segundos (1 punto)
#-El consumidor lee X números de la cola de golpe,
#calcula la multiplicación de esos X números .(1 punto).
#el tiempo de espera entre la lectura de X elementos cola y 
#la siguiente lectura de los siguientes X elementos es de  CT segundos
# (1 punto)
#Prueba el algoritmo con los distintos casos usando una
# relación de productor:consumidor de     
#1:1   con PT=1  CT=4 y X=3 (0,5 puntos)
#4:2 con PT=2  CT=2 y X=2 (0,5 puntos)
#2:6 con PT=1  CT=10 y X=4 (0,5 puntos)

import threading
import queue
import random
import time


class Productor(threading.Thread):
    def __init__(self, queue,PT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.PT = PT
        

    def run(self):
        while True:
            numero = random.randint(100, 500)
            self.queue.put(numero)
            time.sleep(self.PT)


class Consumer(threading.Thread):
    def __init__(self, queue,X,CT):
        threading.Thread.__init__(self)
        self.queue = queue
        self.X = X
        self.CT = CT

    def run(self):
        while True:
            list = []
            res = 1
            for i in range(self.X):
                list.append(self.queue.get())
                res *= list[i]
            print(f"Multiplicación de {list}: {res}")
            time.sleep(self.CT)
            

def main():
    #1:1   con PT=1  CT=4 y X=3 
    q_1_1 = queue.Queue()
    p_1_1= Productor(q_1_1,PT=1)
    c_1_1 = Consumer(q_1_1,X=3,CT=4)
    #4:2 con PT=2  CT=2 y X=2 (0,5 puntos)
    q_4_2 = queue.Queue()
    p_4_2= Productor(q_4_2,PT=2)
    c_4_2 = Consumer(q_4_2,X=2,CT=2)
    #2:6 con PT=1  CT=10 y X=4 (0,5 puntos)
    q_2_6 = queue.Queue()
    p_2_6= Productor(q_2_6,PT=1)
    c_2_6 = Consumer(q_2_6,X=4,CT=10)


    p_1_1.start()
    c_1_1.start()

    p_4_2.start()
    c_4_2.start()

    p_2_6.start()
    c_2_6.start()

    p_1_1.join()
    c_1_1.join()

    p_4_2.join()
    c_4_2.join()

    p_2_6.join()
    c_2_6.join()

if __name__ == "__main__":
    main()