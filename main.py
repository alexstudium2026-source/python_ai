#
# from sentence_transformers import SentenceTransformer
# # Импортируем класс для создания объекта модели.
# model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu", local_files_only=True)
# # Загружаем модель для английских учебных текстов на обычный процессор.
# embedding = model.encode("Hello World!", show_progress_bar=False)
# # Получаем один вектор из одной переданной строки.
# print(embedding.shape)
# # Выводим форму массива одного embedding.
# texts = ["shipping", "delivery", "cat"]
# # Подготавливаем три текста в определенном порядке.
# embeddings = model.encode(texts, show_progress_bar=False)
# # Получаем одну строку координат на каждый текст списка.
# print(embeddings.shape)
# # Проверяем число строк и число координат в каждой строке.
# print(embeddings[0].shape)
# # Берем первую строку, то есть вектор текста shipping.
#
#
# from sentence_transformers import SentenceTransformer
# # Подключаем загрузку модели embeddings.
# from sklearn.metrics.pairwise import cosine_similarity
# # Подключаем вычисление сходства для строк числовых таблиц.
# model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu", local_files_only=True)
# # Создаем одну модель до кодирования всех слов примера.
# texts = ["shipping", "delivery", "banana"]
# # Берем два слова о доставке и одно слово о фрукте.
# vectors = model.encode(texts, show_progress_bar=True)
# # Получаем таблицу из трех векторов в порядке texts.
# near = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
# # Сравниваем shipping с delivery и достаем числовую оценку.
# far = cosine_similarity([vectors[0]], [vectors[2]])[0][0]
# # Сравниваем shipping с banana той же операцией.
# print(f"shipping / delivery: {near:.3f}")
# # Печатаем первую оценку с тремя знаками после точки.
# print(f"shipping / banana: {far:.3f}")
# # Печатаем вторую оценку в том же формате.
#
#
# from sentence_transformers import SentenceTransformer
# # Подключаем класс моделей для получения embeddings.
# from sklearn.metrics.pairwise import cosine_similarity
# # Подключаем функцию сравнения векторов.
# name = "paraphrase-multilingual-MiniLM-L12-v2"
# # Выбираем многоязычную модель из русского примера архива.
# model = SentenceTransformer(name, device="cpu")
# # Загружаем ее один раз перед кодированием трех фраз.
# texts = []
# # Создаем список фраз в заранее известном порядке.
# texts.append("Я попал в ДТП и повредил свой автомобиль")
# # Добавляем описание автомобильной аварии.
# texts.append("Со мной случилась авария, помял крыло моей машины")
# # Добавляем ту же тему, выраженную другими словами.
# texts.append("Я отлично прогулялся вчера пешком и отдохнул")
# # Добавляем фразу о прогулке для сравнения.
# vectors = model.encode(texts, show_progress_bar=False)
# # Превращаем все три фразы в строки числовой таблицы.
# scores = cosine_similarity([vectors[0]], vectors)[0]
# # Сравниваем первую фразу со всеми тремя и берем строку оценок.
# for index, score in enumerate(scores):
# # Перебираем позицию и оценку каждого сравниваемого текста.
#     print(index, f"{score:.3f}")
#     # Печатаем индекс фразы и ее сходство с первой фразой.


# fruit = {"title": "Apple", "price": 0.9}
# # Создаем словарь с именованными полями товара.
# print(fruit["title"], fruit["price"])
# # Достаем значения по названиям ключей словаря.
# pair = ("Apple", 0.9)
# # Создаем кортеж, в котором название стоит первым, а цена вторым.
# print(pair[0], pair[1])
# # Достаем элементы кортежа по индексам 0 и 1.
# fruits = [("Orange", 2.3), ("Apple", 0.9), ("Banana", 2.4)]
# # Создаем список из трех пар, как в архивном примере.
# print(type(fruit).__name__, type(pair).__name__)
# # Показываем, что словарь и кортеж имеют разные типы.
# print(type(fruits).__name__)
# # Проверяем, что внешняя коллекция пар является списком.
#
#
# fruits = [("Orange", 2.3), ("Apple", 0.9), ("Banana", 2.6)]
# # Создаем те же три пары, что и в примере сортировки из архива.
# fruits.sort()
# # Сортируем кортежи начиная с первого элемента — названия фрукта.
# print(fruits)
# # Видим алфавитный порядок Apple, Banana, Orange.
# fruits.sort(key=lambda item: item[1])
# # Сортируем по второй части пары — цене — от меньшей к большей.
# print(fruits)
# # Видим порядок Apple, Orange, Banana.
# fruits.sort(key=lambda item: item[1], reverse=True)
# # Меняем направление сортировки по цене на убывающее.
# print(fruits)
# # Видим порядок Banana, Orange, Apple.
#
# from sklearn.metrics.pairwise import cosine_similarity
# # Подключаем расчет сходства между строками таблиц.
# query = [[1.0, 0.2]]
# # Задаем один учебный вектор запроса как таблицу из одной строки.
# vectors = [[1.0, 0.0],
#            [0.8, 0.6],
#            [0.0, 1.0],
#            [-1.0, 0.0]]
# # Задаем четыре направления с двумя координатами в каждом.
# matrix = cosine_similarity(query, vectors)
# # Сравниваем единственный запрос со всеми четырьмя строками базы.
# print(matrix.shape)
# # Проверяем, что получили одну строку с четырьмя оценками.
# scores = matrix[0]
# print(matrix)
#
# # Достаем первую и единственную строку оценок.
# for score in scores:
# # Перебираем оценки в порядке исходных векторов базы.
#     print(f"{score:.3f}")
#     # Выводим текущую оценку с тремя знаками после точки.
#
