public class Main {
    public static void main(String[] args) {
        Integer[] arr = {4, 3, 2, 3, 5, 10};
        printArray(arr);
        InsertionSort.InsertionSort(arr);
        printArray(arr);
    }

    public static <E> void printArray(E[] arr) {
        for (E obj : arr) {
            System.out.print(obj + " ");
        }
        System.out.println();
    }
}
