using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advance_Algorithmics_HW1
{
    class HW1
    {
        int n;              // Total Random Data to be Generated
        int[] Data_Array;   // Array Holding Random values


        static void Main(string[] args)
        {
            HW1 obj = new HW1();
            string repeat=null;
            do
            {
                    Console.Clear();
                    Console.WriteLine("Enter the amount of Random values...");
                    obj.n = int.Parse(Console.ReadLine());
                    obj.Data_Array = new int[obj.n];                

                    obj.Populate_Random_Data(ref obj.Data_Array);   // Populate array with Random Data
                    obj.Custom_Sort(ref obj.Data_Array);            // Calling Insertion Sort
                    //obj.Built_In_Sort(ref obj.Data_Array);        // or Use Built-in Sort

                    Console.WriteLine("\n\nNext Iteration ? Y/N");
                    repeat = Console.ReadLine().ToString();
               
                
            } while (!(repeat.ToLower().Equals("n")));
           
        }


        /**
         * Populate array and display it
         * NB!: Comment Print Statements in this method if you are interested in time elapsed only
         **/
        void Populate_Random_Data(ref int[] A)
        {
            Random rand = new Random(int.MaxValue);
            Console.WriteLine("\n--------< Random Array >--------\n");
            for (int i=0; i< A.Length;i++)
            {
                A[i] = rand.Next();
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }


        /**
         * Sort Referenced array using Insertion Sort
         **/
        void Custom_Sort(ref int[] A)
        {
            var watch = System.Diagnostics.Stopwatch.StartNew();
           
            for (int i =0;i< A.Length-1;i++)
            {
                for(int j=i+1;j>0 ;j--)
                {
                    if (A[j - 1] > A[j])
                    {
                        int temp = A[j];
                        A[j] = A[j - 1];
                        A[j - 1] = temp;
                    }
                }
            }

            watch.Stop();
            var elapsedMs = watch.Elapsed;

            Console.WriteLine("\n--------< Sorted Array >--------\n");
            for (int i = 0; i < A.Length; i++)
            {
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }

            /**
             * NB!: Comment above loop and Print Statements
             *      if you are interested in time elapsed only
             **/

            Console.WriteLine("\n\n Time Taken by Custom Sort in Ticks " + elapsedMs + " on " + A.Length+ " Inputs");
        }


        /**
         * Sort Referenced array using Built-in Array-Sort
         **/
        void Built_In_Sort(ref int[] A)
        {
            var watch = System.Diagnostics.Stopwatch.StartNew();
            Array.Sort(A);
            watch.Stop();
            var elapsedMs = watch.Elapsed;

            Console.WriteLine("\n--------< Sorted Array >--------\n");
            for (int i = 0; i < A.Length; i++)
            {
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }

            /**
            * NB!: Comment above loop and Print Statements
            *      if you are interested in time elapsed only
            **/

            Console.WriteLine("\n\n Time Taken in Ticks by Built-in Sort " + elapsedMs + " on " + A.Length + " Inputs");
        }


        /**
         * Method to Display array if required
         **/
        void Display_Array(ref int[] A)
        {
            Console.WriteLine("\n\n");
            for (int i = 0; i < A.Length; i++)
            {
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }
    }
}
