
def fourth (val):
    if val >= 3000:
        val = val-(3000*0.25)
        # return val
        print (f'Your take home is {val}; fourth deductible')
    else:   
        val = val-(val*0.25)
        print (f'Your take home is {val}; fourth deductible')
        val = val-(val*0.25)
        return val
        
def third(val):
    if val >= 501:
        val = val-(501*0.175)
        if val<3000:
            print (f'Your take home is {val}; thrid deductible')
        else:
            return fourth(val)
    else: 
        val = val-(val*0.175)
        if val<3000:
            print (f'Your take home is {val}; third deductible')
        else:
            return fourth(val)  
        
def second(val):
        if val >= 130:
            val = val-(130*0.1)
            if val<501:
                print (f'Your take home is {val}; second deductible')
            else:
                return third(val)
        else:  
            val = val-(val*0.1)
            if val<501:
                print (f'Your take home is {val}; second deductible')
            else:
                return third(val)
            
            
def first(val):
        if val >= 110:
            val = val-(110*0.05)
            if val<130:
                print (f'Your take home is {val}; first deductible')
            else:
                return second(val)
        else:   
            val = val-(val*0.05)
            if val<130:
                val = val-(val*0.05)   
                print (f'Your take home is {val}; first deductible')
            else:
                return second(val)


    
class Tax:
    """
    Calculates the taxable income on a given salary.
    salary (int or float): amount to be taxed.
    """
    

    def fourth (val):
        if val >= 3000:
            val = val-(3000*0.25)
            # return val
            print (f'Your take home is {val}; fourth deductible')
        else:   
            val = val-(val*0.25)
            print (f'Your take home is {val}; fourth deductible')
            val = val-(val*0.25)
            return val

    def third(val):
        if val >= 501:
            val = val-(501*0.175)
            if val<3000:
                print (f'Your take home is {val}; thrid deductible')
            else:
                return fourth(val)
        else: 
            val = val-(val*0.175)
            if val<3000:
                print (f'Your take home is {val}; third deductible')
            else:
                return fourth(val)  

    def second(val):
            if val >= 130:
                val = val-(130*0.1)
                if val<501:
                    print (f'Your take home is {val}; second deductible')
                else:
                    return third(val)
            else:  
                val = val-(val*0.1)
                if val<501:
                    print (f'Your take home is {val}; second deductible')
                else:
                    return third(val)


    def first(val):
            if val >= 110:
                val = val-(110*0.05)
                if val<130:
                    print (f'Your take home is {val}; first deductible')
                else:
                    return second(val)
            else:   
                val = val-(val*0.05)
                if val<130:
                    val = val-(val*0.05)   
                    print (f'Your take home is {val}; first deductible')
                else:
                    return second(val)
    
    def __init__(self, salary):
        self.salary = salary
        hidden1 = self.salary - 365
        if self.salary <= 0 or hidden1 <=0:
            print (f'A salary of {self.salary} is not a valid salary')
        else:
            first(hidden1)
         
    