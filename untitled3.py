

1)import matplotlib.pyplot as plt
  grades = [2, 3, 3, 2, 5, 5, 3, 4, 5, 4]
  plt.hist(grades, bins=[2, 3, 4, 5, 6], edgecolor='black')
  plt.xlabel('Оценки')
  plt.ylabel('Количество учеников')
  plt.titile('Распределение оценок по матиматике в классе')
  plt.show()

2) import numpy as np
   random_array = np.random.randint(1, 11, size=(4, 4))
   print(random_array)

3) import matplotlib.pvplot as plt
   total_students = 32
   boys = 15
   girls = 17
   labels = ['Мальчики', 'Девочки']
   sizes = [boys, girls]
   colors = ['blue', 'pink']
   plt.p1e(sizes, labels=labels, colors=colors, autopct='%1.1%%', startangle=90)
   plt.axis('equal') # Равные оси, чтобы круг был кругом
   plt.title('Соотношение мальчиков и девочек в классе')
   plt.show()
