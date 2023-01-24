from decimal import Decimal

class ComissionEmployee:
    """
    ComissionEmployee base class
    
    Comission employees recieve a percentage of their turnover.
    """
    
    def __init__(self, name:str, gross_sales:Decimal, comission_rate:Decimal):
        """Initialize a ComissionEmployee."""
        self.name = name
        self.gross_sales = gross_sales
        self.comission_rate = comission_rate
    
    
    @property
    def gross_sales(self):
        """Return the employee's gross_sales."""
        return self._gross_sales
   

    @gross_sales.setter
    def gross_sales(self, gross_sales):
        """
        Set the employee's gross_sales.
        A ValueError will be raised if the provided gross sale is <= 0."""
        
        if gross_sales < Decimal('0.0'):
            raise ValueError('Gross sales must be greater than zero.')
            
        self._gross_sales = gross_sales
    
    
    @property
    def comission_rate(self):
        """Return the employee's comission_rate"""
        return self._comission_rate
    
    
    @comission_rate.setter
    def comission_rate(self, comission_rate):
        """
        Set the employee's comission_rate.
        A ValueError will be raised if the provided comission rate is not
        in range 0 < comission_rate < 1."""
        
        if not (Decimal('0.00') < comission_rate < Decimal('1.0')):
            raise ValueError('Interest rate must be greater than 0'
                             'and less than 1.')
            
        self._comission_rate = comission_rate

        
    def earnings(self):
        """Calculate and return earnings."""
        return self.gross_sales * self.comission_rate
    

    
class SalariedComissionEmployee(ComissionEmployee):
    """
    An employeee who gets paid a salary plus comission based on
    gross sales."""
    
    def __init__(self, 
                 name:str, 
                 gross_sales:Decimal, 
                 commission_rate:Decimal, 
                 base_salary:Decimal):
        """Initialize SalariedCommissionEmployee's attributes"""
        super().__init__(name, gross_sales, commission_rate)
        self.base_salary = base_salary


    @property
    def base_salary(self):
        return self._base_salary

    
    @base_salary.setter
    def base_salary(self, salary):
        """Set base salary or raise ValueError if invalid."""
        if salary < Decimal('0.00'):
            raise ValueError('Base salaray must be >= to 0')

        self._base_salary = salary
    
    
    def earnings(self):
        """Calculate and return earnings"""
        return self.base_salary + super().earnings()