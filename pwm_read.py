# pwm_read.py
# 2021-04-01
# Public Domain

# http://abyz.me.uk/picod/py_picod.html

# Este script utiliza la biblioteca `picod` para manejar señales PWM
# en un microcontrolador Raspberry Pi Pico. Supone una conexión entre
# GPIO 16 (salida) y GPIO 17 (entrada).

import time  # Biblioteca estándar para manejar retardos en Python
import picod  # Biblioteca específica para controlar Raspberry Pi Pico

# Configuración de los pines GPIO
OUT_GPIO = 14  # Pin GPIO configurado como salida PWM
IN_GPIO = 13   # Pin GPIO configurado como entrada para lectura PWM

# Parámetros de la señal PWM
FREQ = 1250000  # Frecuencia en Hz (1.25 MHz)
DUTY = 25.0     # Ciclo de trabajo (duty cycle) en porcentaje

# Crear instancia de conexión con el Raspberry Pi Pico
pico = picod.pico()
if not pico.connected:  # Verificar si hay conexión con el microcontrolador
   exit()  # Si no hay conexión, salir del programa

# Resetear la configuración del Pico para liberar los GPIO y hardware
pico.reset()

# Configurar el pin de salida (OUT_GPIO) para generar una señal PWM
pico.tx_pwm(OUT_GPIO, FREQ, DUTY)
print("Setting frequency={}, dutycycle={}".format(FREQ, DUTY))

# Leer la frecuencia de la señal PWM desde el pin de entrada (IN_GPIO)
for i in range(10):  # Repetir 10 veces
   status, frequency = pico.pwm_read_frequency(IN_GPIO)  # Leer frecuencia
   print("frequency={}".format(frequency))  # Imprimir el valor leído
   time.sleep(0.3)  # Esperar 0.3 segundos entre lecturas

# Leer el ciclo de trabajo (duty cycle) de la señal PWM desde el pin de entrada
for i in range(10):  # Repetir 10 veces
   status, dutycycle = pico.pwm_read_dutycycle(IN_GPIO)  # Leer duty cycle
   print("dutycycle={:.2f}".format(dutycycle))  # Imprimir con dos decimales
   time.sleep(0.3)  # Esperar 0.3 segundos entre lecturas

# Contar los bordes ascendentes (high edges) de la señal PWM
for i in range(10):  # Repetir 10 veces
   status, count, seconds = pico.pwm_read_high_edges(IN_GPIO)  # Leer bordes ascendentes
   print("count={} seconds={:.2f}".format(count, seconds))  # Imprimir resultado
   time.sleep(0.3)  # Esperar 0.3 segundos entre lecturas

# Cerrar la transmisión PWM en el pin de salida
pico.tx_close(OUT_GPIO)

