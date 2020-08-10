# MCOC2020-P0
# Mi computador
- Marca/modelo: HP 14 Notebook PC

- Tipo: Notebook

- Año adquisición: 2014

- Procesador:
  - Marca/Modelo: Intel(R) Core(TM) i3-4005U
  - Velocidad Base: 1,70 GHz
  - Velocidad Máxima: 1.70 GHz
  - Numero de núcleos: 4
  - Numero de hilos: 2
  - Arquitectura: x64
  - Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
  
- Tamaño de las cachés del procesador
  - L1: 128KB
  - L2: 512KB
  - L3: 3000KB
  
- Memoria
  - Total: 4 GB
  - Tipo memoria: DDR3
  - Velocidad 1600 MHz
  - Numero de (SO)DIMM: 4
  
- Tarjeta Gráfica
  - Marca / Modelo: Nvidia GeForce 820M
  - Memoria dedicada: 1,00 GB
  - Resolución: 1600 x 1080 x 59 hercios
  
- Disco 1:
  - Marca: WDC WDS500G2B0A-00SM50
  - Tipo: SSD
  - Tamaño: 465,76 GB
  - Particiones: 4
  - Sistema de archivos: NTFS


- Dirección MAC de la tarjeta wifi: C4:8E:8F:17:99:97‬

- Dirección IP (Interna, del router): 192.168.0.9

- Dirección IP (Externa, del ISP): 200.86.137.110

- Proveedor internet: VTR Banda Ancha S.A.

# Desempeño MATMUL
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/graficos.jpg)

- ¿Como difiere del gráfico del profesor/ayudante? <br>
 Mi grafico difere del profesor/ayudante en el grafico de arriba en donde se puede apreciar perfectamente que las "lineas de color" no son iguales. Otra diferencia es que todas las lineas del grafico del profesor empiezan en 0,1(ms) y termian en 10(s) aproximadamente, muy distinto de mi gráfico donde las lineas empiezan en el 0,1(s) y terminan en el 10(min).
- ¿A qué se pueden deber las diferencias? <br>
 Las diferencias de "forma" de las lineas se debe plenamente en que estas fueron generadas aleatoriamente por lo que no deberia haber una exactamente igual a la otra. La diferencia de tiempo probablemente se debe a que el procesador del profesor o ayudante es mas rapido y eficiente que el mio por lo que puede realizar la misma tarea en  mucho menos tiempo.
- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? <br>
 Esto se debe a que la variacion de 1 en N, genera la misma variacion exponencial en la memoria al ser (N^2). Esto hace que sea vea lineal al hacer su grafico logaritmico. Por el contrario, para el grafico del tiempo al ser las matrices N*N la dificultad aumentaba considerablemente al aumentar N por que lo que refleja en las ligeras diferencias que tiene la curva con una linea recta.
- ¿Qué versión de python está usando? <br>
 Python 3.7
- ¿Qué versión de numpy está usando?<br>
 1.16.4
- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. <br>
Solamente se utiliza un procesador. <br>
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/procesador%20ejecutando%20el%20codigo.jpg)

# Desempeño MIMATMUL
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/graficos%20de%20mimatmul.png)

- ¿Como difiere del gráfico del profesor/ayudante? <br>
 
- ¿A qué se pueden deber las diferencias? <br>
 
- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? <br>
 
- ¿Qué versión de python está usando? <br>
 Python 3.7
- ¿Qué versión de numpy está usando?<br>
 1.16.4
- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. <br>
Solamente se utiliza un procesador. <br>
![alt text]()


