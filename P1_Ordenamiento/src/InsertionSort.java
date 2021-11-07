public class InsertionSort {
    /**
     * @param arr que es un arreglo de objetos
     *
     * @return un arreglo de objetos ordenado
     */
    public static <E extends Comparable<E>> void InsertionSort(E[] arr) {
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
