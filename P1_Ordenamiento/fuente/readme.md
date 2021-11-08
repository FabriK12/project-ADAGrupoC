# Proyecto 1 - Algoritmos de Ordenamiento
## Insertion Sort
En este algoritmo los elementos se van moviendo de uno en uno hasta encontrar la posicion correcta. En cada una de las iteraciones se puede comprobar 
que los elementos anteriores estan ordenados. Se suele asemejar mucho al ordenamiento de un mazo de cartas en la vida real. Es mejor que el BubbleSort y otros similares.
Pero a medida que los elementos crecen, este algoritmo se vuelve menos eficiente.

### Código Java de InsertionSort
~~~
public static <E extends Comparable<E>> void insertionSort(E[] arr) {
        for (int i = 0; i < arr.length; i++) {
            E key = arr[i];
            int j = i - 1;

            while (j >= 0 && key.compareTo(arr[j]) < 0){
                arr[j + 1] = arr[j];
                j -= 1;
            }
            arr[j + 1] = key;
        }
    }
}
~~~

### Analisis de Complejidad 
En la linea numero 6 se aprecia el ciclo while anidado a un for externo, para el mejor caso , solo realizaria una comparacion, por lo que solo tendria influencia el indice i.
Obteniendo asi que la sumatoria de i=0 hasta N-2 con una constante uno (producto de hacerse solo una comparacion) el codigo se ejecuta N-1 veces.

Por otro lado, cuando el arreglo esta ordenado en sentido contrario al elegido, es seguro que cada elemento se comparará con el resto hasta llegar al indice i. Por ende
en el peor caso, el numero de comparaciones y/o ejecuciones del codigo son:

![sumatoria_peorCaso](https://user-images.githubusercontent.com/82843202/140671214-5ffd1cab-5c9e-417e-8239-46396255afea.png)

Concluyendo asi que en el mejor caso el tiempo es lineal, pudiendo decir que es O(n) mientras que en el peor caso el orden es O(n^2), es decir un orden cuadratico.

## Quick Sort
Este algoritmo es muy conocido por el paradigma "Divide y venceras", consiste en dividir el arreglo en dos partes, siguiendo de forma recursiva el mismo metodo. Suele ser
muy eficiente de ahi su nombre.

### Código Java de QuickSort
~~~
public static <E extends Comparable> void quickSort(E[] arr, int izq, int der) {
    if(izq < der) {
        int piv = particion(arr, izq, der);
        quickSort(arr, izq, piv-1);
        quickSort(arr, piv+1, der);
    }
}
public static <E extends Comparable> int particion(E[] arr, int izq, int der) {
    int p = selectPivoting(izq, der);
    swap(arr, p, der);
    int store = izq;
    for (int i = izq; i < der; i++) {
        if(arr[i].compareTo(arr[der]) <= 0) {
          swap(arr, i, store);
          store++;
        }
    }
    swap(arr, store, der);
    return store;
}
~~~

### Analisis de Complejidad 
Es un algoritmo dificil de explicar linea por linea pero la funcion se puede resumir de la siguiente manera:

![functionQuickSort](https://user-images.githubusercontent.com/82843202/140671241-da28d218-d82f-4d51-a0ff-2a0f481feacf.png)

Para la solucion de esta funcion se usara el teorema Maestro para funciones que se van dividiendo:

![teoremaMaestroDividing](https://user-images.githubusercontent.com/82843202/140671255-8d476b35-0fd7-4529-b4e8-d20bf2e7ef38.png)

Por lo que nos encontramos en el caso 2 cuando p es mayor a -1, Obteniendo asi que la complejidad del algoritmo es O(nLog(n))

### Caso especial: Quick-Insertion Sort
Como se comprueba en la figura de abajo, Insertion Sort resulta eficiente para tamaños pequeños, en el caso de este proyecto se trabaja con el limite 16, lo cual quiere 
decir que cada vez que el tamaño a ordenar sea menor a 16, el algoritmo a operar sera InsertionSort en vez de QuickSort.

~~~
public static <E extends Comparable> void quick_insertionSort(E[] arr, int izq, int der) {
    if(izq < der) {
        if ((der - izq + 1) > 16) {
            int piv = particion(arr, izq, der);
            quickSort(arr, izq, piv-1);
            quickSort(arr, piv+1, der);
        }else {
            InsertionSort.insertionSort(arr, izq, der);
        }
    }
}
~~~

Para el limite se tomo el siguiente articulo de referencia, que ademas de probar la mezcla Quick-InsertionSort, tambien se hace con MergeSort. En este se mencionan
4 limites posibles: 8, 16, 32, 64. Siendo el de mejhor efectividad el limite 16. A continuacion enlace hacia el articulo:
[article_quickInsertionSort](https://seminar.ilkom.unsri.ac.id/index.php/ars/article/view/763)

## Heap Sort
Este algoritmo extiende del concepto de los arboles binarios, en este caso completo lo cual significa que los nodos estan lo mas pegado a la izquierda posible. Se puede
clasificar como un min-heap o max-heap. Para el calculo de los hijos en el arbol se toma como referencia el nivel en el arbol, suponiendo que sea I se calcula el hijo izquierdo
por 2xI + 1 en caso el arreglo comienze en 0 y el hijo derecho de similar forma siendo: 2xI + 2.

### Código Java de HeapSort
~~~
    public static <E extends Comparable> void heapSort(E[] arr){
        builHeap(arr);
        //System.out.println();
        for (int i = arr.length - 1; i >= 1; i--){
            swap(arr, 0, i);
            heapify(arr, 0, i);
        }
    }

    public static <E extends Comparable> void builHeap(E[] arr){
        for (int i = arr.length/2 - 1; i >= 0; i--){
            heapify(arr, i, arr.length);
        }
    }

    public static <E extends Comparable> void heapify(E[] arr, int index, int max){
        int largest = index;
        int izq = 2*index + 1;
        int der = 2*index + 2;

        if (izq < max && arr[izq].compareTo(arr[index]) > 0) {
            largest = izq;
        }
        if (der < max && arr[der].compareTo(arr[largest]) > 0) {
            largest = der;
        }
        if (largest != index) {
            swap(arr, index, largest);
            //printArray(arr);
            //System.out.println();
            heapify(arr, largest, max);
        }
    }
~~~
Como se aprecia en el codigo lo primero es construir el arbol para su posterior ordenacion.

### Analisis de Complejidad 
El algoritmo recorre el arreglo desde la mitad hasta el primer elemento. Al finalizar ese proceso de recorrido para construir el heap, se inicia el proceso de ordenacion
en el cual se intercambia el primer elemento por el ultimo. Como se sabe el recorrido en arboles es de tiempo O(log(n)). Siendo entonces la complejidad de HeapSort: O(nLog(n)),
en el cual se tiene en cuenta el proceso de construccion del arbol y el proceso de ordenacion. 
