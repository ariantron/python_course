from datetime import datetime


class Employee:

    def __init__(self, hire_year, first_salary, salary_increment):
        self.hire_year = hire_year
        self.first_salary = first_salary
        self.salary_increment = salary_increment

    @staticmethod
    def cal_tax(salary):
        if salary > 2000:
            return salary * 0.15
        else:
            return 0

    def cal_current_salary(self):
        current_year = datetime.now().year
        return self.first_salary * (self.salary_increment ** (current_year - self.hire_year))

    def cal_net_salary(self):
        salary = self.cal_current_salary()

        # decrease salary for Insurance
        salary -= salary * 0.1

        # decrease for tax
        salary -= Employee.cal_tax(salary)

        return salary


jack = Employee(2021, 5000, 1.2)
print(jack.cal_net_salary())
