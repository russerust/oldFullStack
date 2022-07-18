using System;
using System.Collections.Generic;
using System.IO;

namespace SectionA // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        
        public delegate void  createNewLists();
        

        // read all employee records
        public static void readHRMasterList()
        {
            string path = @"HRMasterlist.txt";
            if(File.Exists(path)) {
                using (StreamReader sr = File.OpenText(path)) {
                    string s;
                    while ((s = sr.ReadLine()) != null) {
                        Console.WriteLine(s);
                    }
                }
            }
            
        }

        public static void generateInfoForCorpAdmin()
        {
            string path = @"CorporateAdmin.txt";
            List<Employee> employeeList = FormatForHR.ReadTextFile();
            if(!File.Exists(path)) {
                using (StreamWriter sw = File.CreateText(path)) {
                    foreach (var i in employeeList) {
                        sw.WriteLine(i.InfoForCorpAdmin());
                    }
                }  
            }
            else {
                Console.WriteLine("File already exists!");
            }
        }

        public static void generateInfoForITDepartment()
        {
            string path = @"ITDepartment.txt";
            List<Employee> employeeList = FormatForHR.ReadTextFile();
            if(!File.Exists(path)) {
                using (StreamWriter sw = File.CreateText(path)) {
                    foreach (var i in employeeList) {
                        sw.WriteLine(i.InfoForITDepartment());
                    }
                }  
            }
            else {
                Console.WriteLine("File already exists!");
            }
        }

        public static void generateInfoForProcurement()
        {
            string path = @"Procurement.txt";
            List<Employee> employeeList = FormatForHR.ReadTextFile();
            if(!File.Exists(path)) {
                using (StreamWriter sw = File.CreateText(path)) {
                    foreach (var i in employeeList) {
                        sw.WriteLine(i.InfoForProcurement());
                    }
                }  
            }
            else {
                Console.WriteLine("File already exists!");
            }
        }


        static void Main(string[] args)
        {
            readHRMasterList();
            createNewLists createHRFiles = generateInfoForProcurement;
            createHRFiles += generateInfoForITDepartment;
            createHRFiles += generateInfoForCorpAdmin;
            createHRFiles.Invoke();
            
        }

        
}
}