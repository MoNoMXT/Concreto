from machine import Pin
import time

# Pin para el tren de pulsos
pulse_pin = Pin(15, Pin.OUT)  # Usá el pin que conectes a tu etapa de potencia

# LED onboard (solo para Pico W)
led = Pin("LED", Pin.OUT)

# Duración de medio ciclo (~16.6 µs → redondeamos a 17 µs)
half_period_us = 17

while True:
    led.on()  # Indicar que se está enviando el tren
    
    # Enviar 5 ciclos (5 pulsos → 10 transiciones)
    for _ in range(5):
        pulse_pin.on()
        time.sleep_us(half_period_us)
        pulse_pin.off()
        time.sleep_us(half_period_us)
    
    led.off()  # Fin del tren

    time.sleep(1)  # Esperar 1 segundo
