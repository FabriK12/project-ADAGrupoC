# Proyecto 2 : Recorrido en Grafos
En este proyecto se busca implementar los recorridos en grafos DFS (búsqueda en profundidad) y BFS (búsqueda en anchura) en una matriz de numeros que representan una imagen.

## Recursos
Se utilizo dos imagenes para realizar las pruebas y experimentacion se encuentran en la carpeta [Imagenes](https://github.com/FabriK12/project-ADAGrupoC/tree/main/P2_RecorridoGrafos/images)
Como ayuda se uso la libreria OpenCV y numpy para interpretar en una matriz una imagen [OpenCV-Python](https://pypi.org/project/opencv-contrib-python/)

## OpenCV
La libreria OpenCV es util para esta solucion puesto que contiene funciones que permiten la lectura y escritura de una imagen mediante numpy arrays. Esto facilito mucho la tarea
de interpretar en blanco y negro la imagen.

## [DFS](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/DFS.py) y [BFS](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/BFS.py)
Estos dos archivos son de gran utilidad, ya que facilitan el uso de mas funciones exteriores al main y asi hacer llamado a una unica funcion dentro de **main.py**

## Lectura de Datos
Para la imagen es recomendable usar las imagenes de formato jpg o png. Tambien debe indicar rango deseado entre [0-255]. En el codigo dentro de **main.py** se podra cambiar
facilmente la ruta de la imagen deseada.
Las imagenes de muestra son dos [Nemo](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/nemo.jpg) y [Dory](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/dory.jpg)

### Recorridos en la imagen
En los recorridos BFS y DFS, se tiene en cuenta el valor de la imagen a usar, es por ello que se crea una copia para interactuar con ella, asi mismo en la escritura del resultado
luego del recorrido, se guarda con un solo nombre, por ello debe tener cuidado al ejecutar varias veces ya que el resultado anterior se podria perder.

Además, se necesita subrayar que los dos recorridos estan implementados iterativamente, así puede despreocuparse de errores en los recorridos con imagenes enormes. 

Al final, además se debería indicar que el 'repintado' de las imagenes permanecen dadas por un **color referente**, esto significa que el color que forma a un elemento k, 
esta dado por el primer color agregado en aquel elemento para los dos recorridos, esto para que el resultado logre compararse con la imagen inicial y además que de tener 
un color natural y no forzado. 

### Escritura
Como se menciono la salida tiene un nombre en especifico, se puede cambiar dentro de **main.py** la ruta y nombre de salida del archivo. Para esto se recomienda las extensiones 
**.jpg** o **.png**

## Análisis de salidas

### Salidas con rangos de 10, 30, 50
Se mostrara a continuacin las salidas tomando rangos diferentes, especificamente 3, sobre la misma imagen. Se cargo y guardaron los resultados con sus rangos correspondientes 10, 30 y 50:

#### [Dory](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/dory.jpg)
Resultados con los 3 rangos de referencia en **dory.jpg**

**Rango de 10** ![rango de 10](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/dory_10.jpg)  
**Rango de 30** ![rango de 30](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/dory_30.jpg)  
**Rango de 50** ![rango de 50](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/dory_50.jpg)

Con esta imagen al tener rango de colores muy similares se recomienda usar valores por debajo de 20, para mantener la forma de los objetos en la imagen.

#### [Nemo](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/nemo.jpg)
Resultados con los 3 rangos de referencia en **nemo.jpg**

**Rango de 10** ![rango de 10](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/nemo_10.jpg)  
**Rango de 30** ![rango de 30](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/nemo_30.jpg)  
**Rango de 50** ![rango de 50](https://github.com/FabriK12/project-ADAGrupoC/blob/main/P2_RecorridoGrafos/images/nemo_50.jpg)

En esta imagen excederse en valores altos no es tan peligroso como la anterior, puesto que el fondo esta bien diferenciado del objeto o en este caso el pez.

Esta como trabajo futuro, identificar las componentes de la imagen, y extraer las capas de cada una.
