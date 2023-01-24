# salariedcommissionemployee.py
"""SalariedCommissionEmployee derived frm CommissionEmployee"""

from commissionemployee import CommissionEmployee
from decimal import Decimal

class SalariedCommissionEmployee(CommissionEmployee):
    """An employee who gets paid a salary plus commission based on
    on gross sales."""

    def __init__(self, first_name, last_name, ssn,
                 gross_sales, commission_rate, base_salary):
        """Initialize SalariedCommissionEmployee's attributes"""

        super().__init__(first_name, last_name, ssn,
                         gross_sales, commission_rate)

        self.base_salary = base_salary  # validate via property


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
        """Calculate and return earnings."""
        return super().earnings() + self.base_salary

    
    def __str__(self):
        """Return string representation of the object."""
        return('Salaried' + super().__str__() +
               f'base salary: {self.base_salary:.2f}\n')
