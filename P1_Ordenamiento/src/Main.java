import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        long startTime, endTime;
        Character[] arr_letters = new Character[100];
        Integer[] arr_100 = new Integer[100];
        Integer[] arr_1K = new Integer[1000];
        Integer[] arr_10K =  new Integer[10_000];
        Integer[] arr_Personalizado;

        String afirm = "";
        do{
            System.out.print("Desea generar un arreglo de tamano personalizado?(S/N)...");
            afirm = scan.nextLine();

            if(afirm.equals("S")){
                int size;
                try {
                    System.out.print("Ingrese el tamano del arreglo: ");
                    size = scan.nextInt();
                }catch (Exception e){
                    System.out.println("Error se aplicara el default = 2300...");
                    size = 2300;
                }
                arr_Personalizado = new Integer[size];
                break;
            }else if(afirm.equals("N")){
                break;
            }else{
                System.out.println("Solo S/N...");
            }

        }while(!afirm.equals("S") && !afirm.equals("N"));

        System.out.println("Generando arreglos...");
        generateIntegers_Array(arr_100, 50);
        generateIntegers_Array(arr_1K, 500);
        generateIntegers_Array(arr_10K, 500);
        generateLetters_Array(arr_letters);

        systemPause();
        print_shortArray(arr_100);
        print_shortArray(arr_1K);
        print_shortArray(arr_10K);
        print_shortArray(arr_letters);

        System.out.println("QuickSort, InsertionSort y HeapSort con arreglo de 100...");
        startTime = System.nanoTime();
        InsertionSort.insertionSort(arr_100);
        endTime = System.nanoTime();
        print_shortArray(arr_100);
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);
        startTime = System.nanoTime();
        InsertionSort.insertionSort(arr_100);
        endTime = System.nanoTime();
        System.out.println("--Tiempo promedio(μs): " + (endTime-startTime)/1000);
        startTime = System.nanoTime();
        InsertionSort.insertionSort(arr_100);
        endTime = System.nanoTime();
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
        System.out.println("\n");
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
