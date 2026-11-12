#
from rag import get_vector, get_similar_chunks, get

# 1. Вопрос пользователя
question = "Сколько мне ждать товар?"

# 2. Получаем вектор вопроса
vector = get_vector(question)

# 3. Ищем два похожих фрагмента
results = get_similar_chunks(vector, top_k=2)

print("\nКоличество кандидатов:", len(results))

# for result in results:
#     print("\nТекст:", result["text"])
#     print("Оценка:", result["score"])
for result in results:
    print("\nТекст:", result[0])
    print("Оценка:", result[1])

# 4. Проверяем top_k=10
results_10 = get_similar_chunks(vector, top_k=10)

print("\nКандидатов при top_k=10:", len(results_10))

# 5. Проверяем top_k=0
try:
    get_similar_chunks(vector, top_k=0)
except ValueError as error:
    print("\nОжидаемая ошибка:", error)

# 6. Получаем готовый ответ
answer = get(question)

print("\nОтвет:", answer)
