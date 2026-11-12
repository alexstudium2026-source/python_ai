#
results = [("Оплата", 0.25),
           ("Доставка", 0.91),
           ("Возврат", 0.62),
           ("Адрес", 0.13)
           ]
results.sort(key=lambda item: item[1], reverse=True)

top_results = results[:2]

for text, score in top_results:
    print(f"{text} {score:.3f}")