public class QuickSort {
    public static <E extends Comparable> void quickSort(E[] arr) {
        quickSort(arr, 0, arr.length-1);
    }
    public static <E extends Comparable> void quickSort(E[] arr, int izq, int der) {
        if(izq < der) {
            int piv = particion(arr, izq, der);
            quickSort(arr, izq, piv-1);
            quickSort(arr, piv+1, der);
        }
    }
    public static <E extends Comparable> int particion(E[] arr, int izq, int der) {
        int p = selectPivoting(arr, izq, der);
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
    public static <E extends Comparable> int selectPivoting(E[] arr, int izq, int der) {
        return (int) (Math.random()*(der-izq)) + izq;
    }
    public static <E> void swap(E[] arr, int a, int b){
        E aux = arr[a];
        arr[a] = arr[b];
        arr[b] = aux;
    }
}
