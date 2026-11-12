#
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

chunks = ["Оплата", "Доставка", "Возврат", "Адрес"]

# Подключаем расчет сходства между строками таблиц.
query = [[1.0, 0.0]]
# Задаем один учебный вектор запроса как таблицу из одной строки.
vectors = [[1.0, 0.0],
           [0.8, 0.6],
           [0.0, 1.0],
           [-1.0, 0.0]]
# Задаем четыре направления с двумя координатами в каждом.
matrix = cosine_similarity(query, vectors)
# Сравниваем единственный запрос со всеми четырьмя строками базы.
print(matrix.shape)

# Получаем первую строку оценок
scores = matrix[0]

# Получаем индексы и сортируем по убыванию
indices = np.argsort(scores)[::-1]

# Берём первые два индекса
top_results = indices[:2]

# Выводим тексты и оценки
for index in top_results:
    print(f"{chunks[index]} {scores[index]:.3f}")
