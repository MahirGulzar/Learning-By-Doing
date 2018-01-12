using System;

namespace HW3_Algorithms
{
    class HW3
    {
        int n;              // Total Random Data to be Generated
        byte[] byte_Array;   // Array Holding Random values
        int[] int_Array;   // Array Holding Random values
        long[] long_Array;   // Array Holding Random values


        static void Main(string[] args)
        {
            HW3 obj = new HW3();
            string repeat = null;
            do
            {
                Console.Clear();
                Console.WriteLine("Enter the amount of Random values...");
                obj.n = int.Parse(Console.ReadLine());
                obj.int_Array = new int[obj.n];
                obj.byte_Array = new byte[obj.n];
                obj.long_Array = new long[obj.n];


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
            for (int i = 0; i < A.Length; i++)
            {
                A[i] = rand.Next();
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }


        /**
        * Populate array and display it
        * NB!: Comment Print Statements in this method if you are interested in time elapsed only
        **/
        void Populate_Random_Data(ref byte[] A)
        {
            Random rand = new Random(byte.MaxValue);
            Console.WriteLine("\n--------< Random Array >--------\n");
            for (byte i = 0; i < A.Length; i++)
            {
                A[i] = (byte)rand.Next();
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }


        /**
       * Populate array and display it
       * NB!: Comment Print Statements in this method if you are interested in time elapsed only
       **/
        void Populate_Random_Data(ref long[] A)
        {
            Random rand = new Random(int.MaxValue);
            Console.WriteLine("\n--------< Random Array >--------\n");
            for (int i = 0; i < A.Length; i++)
            {
                A[i] = (long)rand.Next();
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }




        public void RadixSort(int[] a)
        {
            // our helper array 
            int[] t = new int[a.Length];

            // number of bits our group will be long 
            int r = 4; // try to set this also to 2, 8 or 16 to see if it is 
                       // quicker or not 

            // number of bits of a C# int 
            int b = 32;

            // counting and prefix arrays
            // (note dimensions 2^r which is the number of all possible values of a 
            // r-bit number) 
            int[] count = new int[1 << r];
            int[] pref = new int[1 << r];

            // number of groups 
            int groups = (int)Math.Ceiling((double)b / (double)r);

            // the mask to identify groups 
            int mask = (1 << r) - 1;

            // the algorithm: 
            for (int c = 0, shift = 0; c < groups; c++, shift += r)
            {
                // reset count array 
                for (int j = 0; j < count.Length; j++)
                    count[j] = 0;

                // counting elements of the c-th group 
                for (int i = 0; i < a.Length; i++)
                    count[(a[i] >> shift) & mask]++;

                // calculating prefixes 
                pref[0] = 0;
                for (int i = 1; i < count.Length; i++)
                    pref[i] = pref[i - 1] + count[i - 1];

                // from a[] to t[] elements ordered by c-th group 
                for (int i = 0; i < a.Length; i++)
                    t[pref[(a[i] >> shift) & mask]++] = a[i];

                // a[]=t[] and start again until the last group 
                t.CopyTo(a, 0);
            }
            // a is sorted 
        }

        public void RadixSort(byte[] a)
        {
            // our helper array 
            byte[] t = new byte[a.Length];

            // number of bits our group will be long 
            byte r = 4; // try to set this also to 2, 8 or 16 to see if it is 
                        // quicker or not 

            // number of bits of a C# int 
            byte b = 32;

            // counting and prefix arrays
            // (note dimensions 2^r which is the number of all possible values of a 
            // r-bit number) 
            int[] count = new int[1 << r];
            int[] pref = new int[1 << r];

            // number of groups 
            int groups = (int)Math.Ceiling((double)b / (double)r);

            // the mask to identify groups 
            int mask = (1 << r) - 1;

            // the algorithm: 
            for (int c = 0, shift = 0; c < groups; c++, shift += r)
            {
                // reset count array 
                for (int j = 0; j < count.Length; j++)
                    count[j] = 0;

                // counting elements of the c-th group 
                for (int i = 0; i < a.Length; i++)
                    count[(a[i] >> shift) & mask]++;

                // calculating prefixes 
                pref[0] = 0;
                for (int i = 1; i < count.Length; i++)
                    pref[i] = pref[i - 1] + count[i - 1];

                // from a[] to t[] elements ordered by c-th group 
                for (int i = 0; i < a.Length; i++)
                    t[pref[(a[i] >> shift) & mask]++] = a[i];

                // a[]=t[] and start again until the last group 
                t.CopyTo(a, 0);
            }
            // a is sorted 
        }

        public void RadixSort(long[] a)
        {
            // our helper array 
            long[] t = new long[a.Length];

            // number of bits our group will be long 
            int r = 4; // try to set this also to 2, 8 or 16 to see if it is 
                        // quicker or not 

            // number of bits of a C# int 
            int b = 32;

            // counting and prefix arrays
            // (note dimensions 2^r which is the number of all possible values of a 
            // r-bit number) 
            int[] count = new int[1 << r];
            int[] pref = new int[1 << r];

            // number of groups 
            int groups = (int)Math.Ceiling((double)b / (double)r);

            // the mask to identify groups 
            int mask = (1 << r) - 1;

            // the algorithm: 
            for (int c = 0, shift = 0; c < groups; c++, shift += r)
            {
                // reset count array 
                for (int j = 0; j < count.Length; j++)
                    count[j] = 0;

                // counting elements of the c-th group 
                for (int i = 0; i < a.Length; i++)
                    count[(a[i] >> shift) & mask]++;

                // calculating prefixes 
                pref[0] = 0;
                for (int i = 1; i < count.Length; i++)
                    pref[i] = pref[i - 1] + count[i - 1];

                // from a[] to t[] elements ordered by c-th group 
                for (int i = 0; i < a.Length; i++)
                    t[pref[(a[i] >> shift) & mask]++] = a[i];

                // a[]=t[] and start again until the last group 
                t.CopyTo(a, 0);
            }
            // a is sorted 
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


        /**
        * Method to Display array if required
        **/
        void Display_Array(ref byte[] A)
        {
            Console.WriteLine("\n\n");
            for (int i = 0; i < A.Length; i++)
            {
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }

        /**
       * Method to Display array if required
       **/
        void Display_Array(ref long[] A)
        {
            Console.WriteLine("\n\n");
            for (int i = 0; i < A.Length; i++)
            {
                Console.WriteLine("Data_Array [" + i + "] = " + A[i]);
            }
        }
    }
}
