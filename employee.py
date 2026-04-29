class Employee:
    """a class to represent an employee"""

    def __init__(self, first_name, last_name, salary):
        """initialize the employee's attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, amount=5000):
        """add a raise to the employee's salary"""
        self.salary += amount