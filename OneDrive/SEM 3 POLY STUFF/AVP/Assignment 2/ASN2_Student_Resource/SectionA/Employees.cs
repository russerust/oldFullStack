using System;
using System.Collections.Generic;
using System.IO;

namespace SectionA // Note: actual namespace depends on the project name.
{
    public class Employee
    {
        private string nric;
        private string fullname;
        private string salutation;
        private DateTime startDate;
        private string designation;
        private string department;
        private string mobileNo;
        private string hireType;
        private double salary;
        private double monthlyPayout;

        public Employee(string NRIC,
        string fullname,
        string salutation,
        DateTime startDate,
        string designation,
        string department,
        string mobileNo,
        string hireType,
        double salary,
        double monthlyPayout = 0.0
        )
        {
            this.nric = NRIC;
            this.fullname = fullname;
            this.salutation = salutation;
            this.startDate = startDate;
            this.designation = designation;
            this.department = department;
            this.mobileNo = mobileNo;
            this.hireType = hireType;
            this.salary = salary;
            this.monthlyPayout = monthlyPayout;
        }
        
        public string InfoForCorpAdmin(){
            return $"{this.fullname},{this.designation},{this.department}";
        }
        public string InfoForITDepartment(){
            return $"{this.nric},{this.fullname},{this.startDate},{this.department},{this.mobileNo}";
        }
        public string InfoForProcurement(){
            return $"{this.salutation},{this.fullname},{this.mobileNo},{this.designation},{this.department}";
        }
    



    }

    public class FormatForHR {
        public static List<Employee> ReadTextFile() {
            List<Employee> employees = new List<Employee>();
            string path = @"HRMasterlist.txt";
            if (File.Exists(path)) {
                using (StreamReader sr = File.OpenText(path)) {
                    string s;
                    while ((s = sr.ReadLine()) != null) {
                        string [] HRList = s.Split("|");
                        employees.Add(new Employee(HRList[0],HRList[1],HRList[2],DateTime.ParseExact(HRList[3],"dd/MM/yyyy", System.Globalization.CultureInfo.InvariantCulture),HRList[4],HRList[5],HRList[6],HRList[7],Convert.ToDouble(HRList[8])));
                    }
                }
                
            }
            return employees;
        }
    }

    
}