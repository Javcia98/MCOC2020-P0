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
 Se utilizan 4 procesadores. <br>
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/procesador%20ejecutando%20el%20codigo.jpg)

# Desempeño MIMATMUL
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/graficos%20de%20mimatmul.png)

- ¿Como difiere del gráfico del profesor/ayudante? <br>
 A grandes rasgos los graficos se ven muy parecidos con una clara tendencia lineal ascendente pero difieren en que en mi grafico hay casos en que la curva no es lineal y presenta unas pequeñas "desviaciones" las cuales se pueden apreciar claramente en el grafico ((como la curva de color rojo). También, en general, los calculos en el grafico del ayudante para cualquier N se demoraban menos tiempo que en mi grafico.
- ¿A qué se pueden deber las diferencias? <br>
 Estas diferencias seguramente se deben a que el codigo que use para el calculo de la multiplicacion de matrices fueron fragmentos de muchos codigos que encontre y los ordene para que me hicieran mas sentido para mi... seguramente esto hizo que el calculo no fuera el mas eficiente si se le compara con el que uso el ayudante. Tambien entra en juego los diferentes tipos de procesadores usados en cada computador. En relacion a los "saltos" que ocurren en algunas de las curvas estos pueden deberse a que al principio solo se usa un solo procesador logico para hacer los calculos, pero al pasar a un N mas grande se ve en la necesidad de usar los demas... aqui se explica las diferencias de tiempo con respecto a N.
- El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser? <br>
 Como se dijo anteriormente, el grafico del tiempo transcurrido no es lineal ya que presenta estos "saltos" de tiempo, ese comportamiento se debe a que al principio se usa solo un procesador y a medida que va aumentando N se van incorporando mas procesadores provocando estos saltos de tiempo y por consiguente este comportamiento no lineal.
- ¿Qué versión de python está usando? <br>
 Python 3.7
- ¿Qué versión de numpy está usando?<br>
 1.16.4
- Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. <br>
 Se utilizan 4 procesadores. <br>
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/imagen%20procesadores%20mimatmul.png)

 # Entrega4 - Desempeño de INV
 ![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/graficos%20TYPES.png)
 ![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/grafico%20memoria%20TYPES.png) <br>
 Al mirar el grafico podemos percatarnos que en mi sistema utilizar la opcion "overwrite_a=True" resulta en una ligera ganancia de desempeño (tiempo) al ser comparada con los otros casos. Además se debe agregar que hay 2 graficos en los que no se pudo considerar el primer caso ya que  linalg de numpy no soportaba el uso de float16 ni tampoco de float 128 por lo que en este tipos de datos no se pudo analizar si el caso 1 era el menor o no. Otro punto interesante de analizar es ver como se comporta cada tipo de dato al momento de analizar la memoria que ocupa. donde se muestra una clara tendencia referente a los tipos de datos con mayor uso de bits sean los que mas memoria ocupan (obersrvar grafico) <br>
 
- ¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? <br>
Segun mi parecer el algoritmo que utiliza el caso 1 (al ser el mas  relativamente rapido cuando fue comparado) es el de la solucion unica ya que es el algoritmo que utiliza la menor cantidad de variables al calcular las inversas, solo usa  ixj + 1 donde ese 1 es el determinante. Ahora para el caso 2 el cual es el que peor desempeño tiene seguramente puede usar el metodo de Cayley-Hamilton ya que este algoritmo usa una serie de operaciones matematicas ( sumatorias, pitatorias,potencias,factorial etc) por lo que seguramente el realizar estas operaciones y creas variables que guarden cada parte de estas es la razon de la diferencia de tiempo. Por ultimo el caso 3 al no ser el mas rapido ni el mas lento es probable que el metodo usado sea  la Inversion de Blockwise, esto debido a que igual usa un metodo parecido para el caso 1 pero con algunas operaciones extra.
- ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? (Ver clase 10 Agosto)<br>
 Con respeto a la estructura de caché, estos son una forma de acceder muy rapidamente a la información, entonces al partir con operaciones de matrices pequeñas se parte llenando una caché. Este caché seguira guardando informacion (la cual se puede acceder de manera muy rapida) hasta llenarse, en ese momento otra caché empieza a almacenar la informacion de las operaciones (fenomeno conocido como paralelismo) y asi sucesivamente. Una vez que todas las cachés estan llenas se prosigue a utilizar la memoria RAM que es mas lenta si se le compara con los cachés esto hace que se deteriore el desempeño del equipo ya que no podra seguir con la velocidad de antes. Es por eso que cada vez que aumenta el numero de N el tiempo de demora aumenta cada vez mas, realizando de vez en cuando unos "saltos" que demuestras este tipo de cambios del procesador y las cachés. 
 - A continuación se presenta el comportamiento de los procesadores al ejecutar los programas para cada caso: <br>
 Para el caso 1:
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/procesador%20caso1.png) <br> 
Para el caso 2:
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/procesador%20caso2.png) <br>
Para el caso 3:
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/procesador%20caso3.png)

# Entrega 6 - Desempeño de Ax = B
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/Entrega%206/graficoEntrega6.png) <br>

Como se puede apreciar en el grafico podemos ver que ciertas funciones tienen mejor desempeño que otras, es casi una costante para casi todos los valores de N que la funcion A_invB es la con peor desempeño por lo que para ningun caso se recomiendo su uso en terminos del ahorro de tiempo. Por el contrario si entramos a analizar las funciones con mejor desempeño destaca a priori la funcion A_invB_npSolve la cual en promedio tiene el mejor desempeño para matrices con un N menor a 200, sin embargo al aumentar N esta funcion se vuelve obsoleta ya que es superada por la mayoria de las funciones. Para N mayores a 200 hay 2 funciones que destacan por sobre todas, la A_invB_spSolve_pos_overwrite_a y A_invB_spSolve_pos_overwrite_b. Estas funciones van codo a codo para cada N en terminos de desempeño por lo que para N muy grandes se recomienda usar cualquiera de estas 2 funciones. Sin embrago existe una diferencia minima entre los tiempos de cada una para N = 10000 haciendo que la primera funcion (A_invB_spSolve_pos_overwrite_a) sea 0,3s mas rapida, tal vez esta diferencia sea insignificante pero al compararlas con N mucho mas elevados la diferencia sera mucho mas notable. Una razon probalbe de que estas funciones sean las mas rapidas es porque ocupan menos variables al sobreescribir datos en las matrcices A y B respectivamente y al ser la matriz A la mas grande sobreescribir en esta conlleva a un gran ahorro en memoria por lo que la informaciones necesaria sera almacenada por las cachés lo que hara que aumente considerablemente la velocidad. En resumen se recomienda: No usar la funcion A_invB - Usar A_invB_npSolve para N menores a 200 - Usar A_invB_spSolve_pos_overwrite_a para valores de N muy elevados.


# Matrices dispersas y complejidad computacional

Codigo de ensamblaje matriz laplaciana: <br>
```
from numpy import zeros, fill_diagonal, float64
def matriz_laplaceana(N,dtype=float64):
    
    A=zeros((N,N), dtype=dtype)
    fill_diagonal(A,2)
    for i in range(N):
        for j in range(N):
            if (abs(i-j)==1):
                A[i,j]=-1       
    return A
 ```
 

![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/Entrega%207/MATMUL%20MATRICES%20LLENAS.png) <br>
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/Entrega%207/MATMUL%20MATRICES%20DISPERSAS.png) <br>
1. Para este caso se puede apreciar que la diferencia de tiempo para la solucion entre los dos tipos de matrices es muy desigual, el tiempo de solucion de la matriz llena es mucho mayor a la de las dispersas. Lo anterior se puede deber simplemente a que los calculos en las dispersas eran solo las diagonales y no la matriz entera por lo era evidente que se iba a demorar mucho menos a su contraparte. Por otro lado el tiempo de ensamblaje es muy parecido ya que para los valors mas grande e N estos se demoraron no mas de 1 segundo. Cabe destacar que el N max para este calculo fue de 800 porque mas que eso el codigo se demoraba mucho en correr, de igual manera se llevo a una exigencia razonable al computador. <br>
2. La complejidad asintótica para los 2 casos es que el programa no va a terminar nunca de, primero crear las matrices y segundo en resolverlas, osea que no pasaria de la primera parte. Esto crearía un problema en la memoria del computador donde tarde o temprano (dependiendo del tipo) esta se acabará y no habra lugar para guardar mas informacion por lo que el programa dejaria de correr y no se podria cumplir la tarea. <br>
3. <br>
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/Entrega%207/INV%20MATRICES%20LLENAS.png) <br>
![alt text](https://github.com/Javcia98/MCOC2020-P0/blob/master/Entrega%207/INV%20MATRICES%20DISPERSAS.png) <br>
1. Para la inversion de matrices podemos apreciar que no se ven diferencias a grandes rasgos, pero mas detalladamente si hay. Claro esta que para el ensamblaje los tiempos para cada tipo de matriz son casi identicos por lo que se puede hacer de cualquiera de las 2 formas y no tendria grandes consecuencias. Ahora hablando del tiempo de solucion si hay diferencias,podemos ver que el tiempo para las matrices disperas en el rango N = [0,2000] aproximadamente es mas rapido usar matrices llenas esto se puede deber a que para calculos de inversion tener los ceros disponibles puede acelerar los calculos ya que es cosa de hacer las operaciones solamente, en cambio las dispersas para realizar el mismo calculo deberá crear de igual manera esos ceros para hacer la operacion lo que lo retrasaria en tiempo.Para N mas grandes al rango anterior los 2 graficos se comportar similarmente. En terminos de ensablaje podemos ver tambien que las matrices llenas son ligeramnte mas rapidas que las dispersas. <br<
2. La complejidad asintótica para los 2 casos es que el programa no va a terminar nunca de, primero crear las matrices y segundo en resolverlas, osea que no pasaria de la primera parte. Esto crearía un problema en la memoria del computador donde tarde o temprano (dependiendo del tipo) esta se acabará y no habra lugar para guardar mas informacion por lo que el programa dejaria de correr y no se podria cumplir la tarea. <br>
