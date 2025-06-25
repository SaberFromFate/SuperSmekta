#python search.py Mechanicus --directory путь/к/директории

import os
import argparse

def search_in_file(file_path, search_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return search_string in file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Поиск строки в YAML-файлах.')
    parser.add_argument('search_string', type=str, help='Строка для поиска')
    parser.add_argument('--directory', type=str, default='.', help='Директория для поиска (по умолчанию: текущая)')
    args = parser.parse_args()

    found = False
    for root, _, files in os.walk(args.directory):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                file_path = os.path.join(root, file)
                if search_in_file(file_path, args.search_string):
                    print(f"Найдено в файле: {file_path}")
                    found = True

    if not found:
        print("Совпадений не найдено.")

if __name__ == '__main__':
    main()