import re

def clean_content(content):
    step_1 = re.sub(r"[^а-яА-Я0-9.,!?\- ]", "", content)
    step_2 = re.sub(r"\s+", " ", step_1).strip()
    return step_2