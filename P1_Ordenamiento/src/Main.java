public class Main {
    public static void main(String[] args) {
        Integer[] arr = {4, 3, 2, 3, 5, 10};
        Integer a = 1;
        Integer b = 2;

        printArray(arr);
        HeapSort.heapSort(arr);
        printArray(arr);
    }

    public static <E> void printArray(E[] arr) {
        for (E obj : arr) {
            System.out.print(obj + " ");
        }
        System.out.println();
    }
}
