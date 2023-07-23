from datetime import datetime
from application import salary
from application.db import people

import matplotlib.pyplot as plt

def first_plot(x, y):   
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График')
    plt.grid()
    plt.plot(x, y, color='g')
    plt.scatter(x, y, color='g', marker='o')
    plt.show()
    

if __name__ == '__main__':
    print(datetime.now().strftime('%d.%m.%Y'))
    salary.calculate_salary()
    people.get_employees()
    x = [el for el in range(-5, 6)]
    y = [el ** 2 for el in x]
    first_plot(x, y)

