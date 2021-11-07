public class HeapSort {
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

    public static <E> void swap(E[] arr, int a, int b){
        E aux = arr[a];
        arr[a] = arr[b];
        arr[b] = aux;
    }
    public static <E> void printArray(E[] arr){
        for (E a : arr){
            System.out.print(a + " ");
        }
    }
}
