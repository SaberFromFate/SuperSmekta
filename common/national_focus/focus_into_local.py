import re

def parse_focus_file_regex(input_filename, output_filename):
    """
    Парсит файл с фокусами регулярками.
    """
    with open(input_filename, 'r', encoding='utf-8') as file:
        content = file.read()  # Читаем весь файл
    
    # Регулярное выражение для поиска блоков
    pattern = r'id\s*=\s*(\w+).+?}'
    matches = re.findall(pattern, content, flags=re.DOTALL)  # DOTALL — чтобы . захватывал переносы строк
    
    # Формируем строки для записи
    result_data = [f' {focus_id}: "" ' for focus_id in matches]
    
    
    # Пишем результат
    with open(output_filename, 'a', encoding='utf-8') as outfile:
        outfile.write('\n'.join(result_data))

# Используем функцию
parse_focus_file_regex('Svyat_focus.txt', 'output_regex.txt')