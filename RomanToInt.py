def romanToInt(s: str) -> int:
        num =0                        #some exceptions
        s=s.replace("IV","IIII");     #for 4
        s=s.replace("IX","VIIII");    #for 9
        s=s.replace("XL","XXXX");     #for 40
        s=s.replace("XC","LXXXX");    #for 90
        s=s.replace("CD","CCCC");     #for 400 
        s=s.replace("CM","DCCCC");    #for 900
        for _ in s:
            if _ == 'I':
                num += 1
            elif _ == 'V':
                num+= 5
            elif _ == 'X':
                num+= 10
            elif _ == 'L':
                num+= 50
            elif _ == 'C':
                num+= 100
            elif _ == 'D':
                num+= 500
            elif _ == 'M':
                num+= 1000
            else:
                print("enter the correct value")          
        return num  
            
print("Enter the Roman number (all in capital letters):")
n = input()
print(romanToInt(n))
    
            
            

