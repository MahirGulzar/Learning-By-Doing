using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Advance_Algorithmics
{
    class HW2_1
    {
        Int64 n;              // Total Random Data to be Generated
        Int64[] Data_Array;   // Array Holding Random values


        static void Main(string[] args)
        {
            HW2_1 obj = new HW2_1();
            
                
                Console.WriteLine("Enter the amount of Random values...");
                obj.n = Int64.Parse(Console.ReadLine());
                obj.Data_Array = new Int64[obj.n];
                obj.Populate_Random_Data(ref obj.Data_Array);   //Populate array with random data
                Array.Sort(obj.Data_Array);                     // Sort array for binary search

            //------------------------------------------------------------------------------------------

           
            Console.WriteLine("Please Wait...Performing random element searches... ");
            Int64 to_search;


            Random rand = new Random();

           
            int search_count = 0;
            var watch = System.Diagnostics.Stopwatch.StartNew();
            do
                {
                to_search=rand.Next(int.MaxValue);
                    obj.B_Search(ref obj.Data_Array, to_search);
                search_count++;
                } while (watch.ElapsedMilliseconds < 60000);
                watch.Stop();

                var elapsedMs = watch.ElapsedMilliseconds;
            Console.WriteLine("\n\nTime Elapsed = "+(elapsedMs/1000)+" seconds...\nNumber of Binary Searches = "+search_count);
            

            Console.ReadKey();
          

        }

        /**
         * Binary Search method Takes sorted array reference
         * and element which is to be searched..
         **/
         bool B_Search(ref Int64[] A, Int64 elem)
        {

            Int64 lower_end = 0, mid, higher_end = A.Length - 1;

            while(lower_end<=higher_end)
            {
                mid = (lower_end + higher_end) / 2;
                if(elem< A[mid])
                {
                    higher_end = mid - 1;
                }
                else if(elem > A[mid])
                {
                    lower_end = mid + 1;
                }
                else
                {
                   // Console.WriteLine("Element found...");
                    return true;
                }
            }
           // Console.WriteLine("No Such Element");
            return false;
        }


        /**
         * Populate array and display it
         * NB!: Comment Print Statements in this method if you are interested in time elapsed only
         **/
        void Populate_Random_Data(ref Int64[] A)
        {
            Random rand = new Random();
           // Console.WriteLine("\n--------< Random Array >--------\n");
            for (Int64 i = 0; i < A.Length; i++)
            {
                A[i] = rand.Next(int.MaxValue);
                //Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }

    }
}
