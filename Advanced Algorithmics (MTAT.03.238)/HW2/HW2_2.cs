using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advance_Algorithmics
{
    class HW2_2
    {
        int n;              // Total Random Data to be Generated
        int[] Data_Array;   // Array Holding Random values


        static void Main(string[] args)
        {
            HW2_2 obj = new HW2_2();
            string repeat;
            do
             {
                Console.Clear();
                    Console.WriteLine("Enter the amount of Random values...");
                    obj.n = int.Parse(Console.ReadLine());
                    obj.Data_Array = new int[obj.n];
                    obj.Populate_Random_Data(ref obj.Data_Array);   //Populate array with random data


                var watch = System.Diagnostics.Stopwatch.StartNew();
                obj.Dual_Pivot_QuickSort(obj.Data_Array, 0, obj.Data_Array.Length - 1);         // Dual Pivot Quick Sort

                //Array.Sort(obj.Data_Array, 0, obj.Data_Array.Length - 1);                        // Built-in Sort

                watch.Stop();
                var elapsedMs = watch.Elapsed;
                Console.WriteLine("\n\n Time Taken by Sort in Ticks " + elapsedMs + " on " + obj.n + " Inputs");

                Console.WriteLine("\n\nNext Iteration ? Y/N");
                    repeat = Console.ReadLine().ToString();


        } while (!(repeat.ToLower().Equals("n")));

            //obj.Display_Array(obj.Data_Array);
            //Console.ReadKey();
        }



        /**
         * Dual-Pivot QuickSort..
         * Takes 3 arguments, The Array to be sorted 'A'[]
         * The lower boundery of the array 'lower'
         * The upper boundery of the array 'higher'
         **/
        void Dual_Pivot_QuickSort(int[] A, int lower, int higher)
        {
      
            if (higher <= lower)
                return;

            int p1 = A[lower];
            int p2 = A[higher];


            if (p1 > p2)
            {
                Swapping(A, lower, higher);
                p1 = A[lower];
                p2 = A[higher];
            }


            int i = lower + 1;
            int lt = lower + 1;
            int gt = higher - 1;

            while (i <= gt)
            {

                if (A[i] < p1)
                {
                    Swapping(A, i++, lt++);
                }
                else if (p2 < A[i])
                {
                    Swapping(A, i, gt--);
                }
                else
                {
                    i++;
                }

            }
            Swapping(A, lower, --lt);
            Swapping(A, higher, ++gt);


            // Recursion Split

            Dual_Pivot_QuickSort(A, lower, lt - 1);
            Dual_Pivot_QuickSort(A, lt + 1, gt - 1);
            Dual_Pivot_QuickSort(A, gt + 1, higher);

        }



        /**
         * Helper Method for swapping
         **/
        void Swapping(int[] A, int i, int j)
        {
            int temp = A[i];
            A[i] = A[j];
            A[j] = temp;
        }

        /**
         * Populate array and display it
         * NB!: Comment Print Statements in this method if you are interested in time elapsed only
         **/
        void Populate_Random_Data(ref int[] A)
        {
            Random rand = new Random();
           // Console.WriteLine("\n--------< Random Array >--------\n");
            for (int i = 0; i < A.Length; i++)
            {
                A[i] = rand.Next(100);
                //Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }


        /**
         * Display Array
         **/
        void Display_Array(int[] A)
        {
           // Console.WriteLine("\n--------< Sorted Array >--------\n");
            for (int i = 0; i < A.Length; i++)
            {
               // Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }

        //=================================================================================


        

    }
}
