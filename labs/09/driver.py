''' A program that uses the Employee class to determine the maximum and minimum salaries of a list of employees.
November 3, 2016
Lab 9 Exercise 9.4, 9.5, 9.6
@author Ian Christensen (igc2) '''

from employee import Employee

employees = []

with open('employees.txt', 'r') as file:
    for line in file:
        employees.append(Employee(line))
print(len(employees))

if len(employees) == 0:
    print('No employees')

elif len(employees) >= 1:
    totals = {}
    count = {}
    max_employee = employees[0]
    min_employee = employees[0]
    for employee in employees:
        if employee.get_rank() in totals:
            totals[employee.get_rank()] += int(employee.get_salary())
            count[employee.get_rank()] += 1
        else:
            totals[employee.get_rank()] = int(employee.get_salary())
            count[employee.get_rank()] = 1
            
        if int(employee.get_salary()) > int(max_employee.get_salary()):
            max_employee = employee
        if int(employee.get_salary()) < int(min_employee.get_salary()):
            min_employee = employee

def print_averages(totals, count, outFile):
    ''' A function that finds the average salary of an employee. '''
    outFile.write('Rank\tAverage Salary\n')
    for rank in totals.keys():
        average_salary = int(totals[rank]) / int(count[rank])
        outFile.write('{0}\t{1}\n'.format(rank, average_salary))


if __name__ == '__main__':
    ''' Writes the appropriate values to a file. '''
    with open('employee_stats.txt', 'w') as outFile:
        outFile.write('Maximum Salary:\t{0}\n'.format(max_employee))
        outFile.write('Minimum Salary:\t{0}\n'.format(min_employee))
        print_averages(totals, count, outFile)