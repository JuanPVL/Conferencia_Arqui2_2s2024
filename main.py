import redis
import os
import random
import time

#getting the password from the environment variable
password_R = os.getenv('REDIS_PASSWORD')

#connecting to the redis server

r = redis.Redis(host='localhost', port=6379, password=password_R)

if r is not None:
    print("Connected to Redis")
    print("Sending ingresos to Redis")
else:
    print("Error connecting to Redis")


ingresos = ["maestro","alumno","visitante"]

while True:
    ingreso = random.choice(ingresos)
    r.hincrby("ingresos", ingreso, random.randint(1, 5))

    egreso = random.choice(ingresos)
    r.hincrby("ingresos", egreso, -1)


    #crear key para almacenar el total de votos
    r.incr("total")

    print("Ingresa: ", ingreso)
    print("Egresa: ", egreso)


    time.sleep(2)