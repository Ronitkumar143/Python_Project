class cpiCalculate():
    def marksInput(self):
        dataScience=float(input("Enter the marks in Data Scince: "))
        dsa=float(input("Enter the marks in DSA: "))
        mathematics=float(input("Enter the marks in Mathematics: "))
        cap=float(input("Enter the marks in Capstone Project: "))

    def cpiGrade(self):
        if dataScience < 40:
            print("Grade of Data Science is : FF")
        elif dataScience > 40 & dataScience < 60:
            print("Grade of Data Science is : DD")
        elif dataScience > 60 & dataScience < 70:
            print("Grade of Data Science is : CC")
        elif dataScience > 70 & dataScience < 80:
            print("Grade of Data Science is : BB")
        elif dataScience > 80 & dataScience < 90:
            print("Grade of Data Science is : AA")
        else:
            print("Grade of Data Science is : AA+")

        if dsa < 40:
            print("Grade of DSA is : FF")
        elif dsa > 40 & dsa < 60:
            print("Grade of DSA is : DD")
        elif dsa > 60 & dsa < 70:
            print("Grade of DSA is : CC")
        elif dsa > 70 & dsa < 80:
            print("Grade of DSA is : BB")
        elif dsa > 80 & dsa < 90:
            print("Grade of DSA is : AA")
        else:
            print("Grade of DSA is : AA+")

        if mathematics < 40:
            print("Grade of Mathematics is : FF")
        elif mathematics > 40 & mathematics < 60:
            print("Grade of Mathematics is : DD")
        elif mathematics > 60 & mathematics < 70:
            print("Grade of Mathematics is : CC")
        elif mathematics > 70 & mathematics < 80:
            print("Grade of Mathematics is : BB")
        elif mathematics > 80 & mathematics < 90:
            print("Grade of Mathematics is : AA")
        else:
            print("Grade of Mathematics is : AA+")

        if cap < 40:
            print("Grade of DSA is : FF")
        elif cap > 40 & cap < 60:
            print("Grade of DSA is : DD")
        elif cap <60 & cap < 70:
            print("Grade of DSA is : CC")
        elif cap > 70 & cap < 80:
            print("Grade of DSA is : BB")
        elif cap > 80 & cap < 90:
            print("Grade of DSA is : AA")
        else:
            print("Grade of DSA is : AA+")

    def cpiCal(self):
        cpi=(dataScience + mathematics + cap + dsa)//4
        print("CPI IN THIS SEMESTER IS : ",cpi)


ans=cpiCalculate()
ans.marksInput()
ans.cpiGrade()
ans.cpiCal()