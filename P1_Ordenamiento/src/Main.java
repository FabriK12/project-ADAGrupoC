import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        long startTime, endTime;
        Character[] arrLetters_Quick = new Character[100];
        Character[] arrLetters_QuickInsertion = new Character[100];
        Character[] arrLetters_Insertion = new Character[100];
        Character[] arrLetters_Heap = new Character[100];

        Integer[] arr_Quick = new Integer[1000];
        Integer[] arr_QuickInsertion = new Integer[1000];
        Integer[] arr_Insertion = new Integer[1000];
        Integer[] arr_Heap =  new Integer[1000];

        System.out.println("Generando arreglos numericos...");
        generateIntegers_Array(arr_Quick, 1200);
        System.arraycopy(arr_Quick,0, arr_QuickInsertion, 0, 1000);
        System.arraycopy(arr_Quick,0, arr_Insertion, 0, 1000);
        System.arraycopy(arr_Quick,0, arr_Heap, 0, 1000);
//        generateLetters_Array(arr_letters);

        systemPause();
        System.out.println("Todos los metodos tienen este arreglo:");
        print_shortArray(arr_Quick);

        System.out.println("Tiempos QuickSort, InsertionSort y HeapSort");
        System.out.println("\nQuickSort: ");
        startTime = System.nanoTime();
        QuickSort.quickSort(arr_Quick);
        endTime = System.nanoTime();
        print_shortArray(arr_Quick);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);

        System.out.println("\nInsertionSort: ");
        startTime = System.nanoTime();
        InsertionSort.insertionSort(arr_Insertion);
        endTime = System.nanoTime();
        print_shortArray(arr_Insertion);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);


        System.out.println("\nQuick-InsertionSort: ");
        startTime = System.nanoTime();
        QuickSort.quick_insertionSort(arr_QuickInsertion);
        endTime = System.nanoTime();
        print_shortArray(arr_QuickInsertion);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);

        System.out.println("\nHeapSort: ");
        startTime = System.nanoTime();
        HeapSort.heapSort(arr_Heap);
        endTime = System.nanoTime();
        print_shortArray(arr_Heap);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);


        System.out.println("Generando arreglos alfanumericos...");
        generateLetters_Array(arrLetters_Quick);
        System.arraycopy(arrLetters_Quick,0, arrLetters_QuickInsertion, 0, 100);
        System.arraycopy(arrLetters_Quick,0, arrLetters_Insertion, 0, 100);
        System.arraycopy(arrLetters_Quick,0, arrLetters_Heap, 0, 100);

        systemPause();
        System.out.println("Todos los metodos tienen este arreglo:");
        print_shortArray(arrLetters_Quick);

        System.out.println("Tiempos QuickSort, InsertionSort, Quick-InsertionSort y HeapSort");
        System.out.println("\nQuickSort: ");
        startTime = System.nanoTime();
        QuickSort.quickSort(arrLetters_Quick);
        endTime = System.nanoTime();
        print_shortArray(arrLetters_Quick);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);

        System.out.println("\nInsertionSort: ");
        startTime = System.nanoTime();
        InsertionSort.insertionSort(arrLetters_Insertion);
        endTime = System.nanoTime();
        print_shortArray(arrLetters_Insertion);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);


        System.out.println("\nQuick-InsertionSort: ");
        startTime = System.nanoTime();
        QuickSort.quick_insertionSort(arrLetters_QuickInsertion);
        endTime = System.nanoTime();
        print_shortArray(arrLetters_QuickInsertion);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);

        System.out.println("\nHeapSort: ");
        startTime = System.nanoTime();
        HeapSort.heapSort(arrLetters_Heap);
        endTime = System.nanoTime();
        print_shortArray(arrLetters_Heap);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);
        /*
        systemPause();

        printArray(arr);
        QuickSort.quick_insertionSort(arr);
        printArray(arr);
         */
    }

    public static <E> void printArray(E[] arr) {
        for (E obj : arr) {
            System.out.print(obj + " ");
        }
        System.out.println();
    }

    public static <E> void print_shortArray(E[] arr) {
        int limit = 8;
        System.out.println("Tamano del arreglo: " + arr.length);
        for(int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
            if(i == limit){
                i = arr.length-(limit+1);
                System.out.print("... ");
            }
        }
        System.out.println();
    }

    public static void generateIntegers_Array(Integer[] arr, int max) {
        for (int i = 0; i < arr.length; i++)
            arr[i] = (int) (Math.random()*max)+1;
    }

    public static void generateLetters_Array(Character[] arr) {
        for (int i = 0; i < arr.length; i++) {
            int numberASCII = (int) (Math.random() * (122 - 65)) + 65;
            arr[i] = (char) (numberASCII);
        }
    }

    public static void systemPause() {
        String seguir;
        Scanner scan = new Scanner(System.in);
        System.out.print("Press Enter key to continue...");
        try
        {
            seguir = scan.nextLine();
        }
        catch(Exception e)
        {}
    }
}
