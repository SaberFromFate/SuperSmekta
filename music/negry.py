import os

# Путь к папке с .ogg файлами (замени на свой путь, если нужно)
folder_path = "./"  # текущая папка

# Имя выходного текстового файла
output_file = "music_list.txt"

# Получаем список всех файлов в папке
files = os.listdir(folder_path)

# Фильтруем только .ogg файлы
ogg_files = [f for f in files if f.endswith(".ogg")]

with open(output_file, "w", encoding="utf-8") as out:
    for ogg in ogg_files:
        name = ogg[:-4]  # убираем ".ogg"
        block = f"""music = {{
\tname = "{name}"
\tfile = "{ogg}"
\tvolume = 0.5
}}\n"""
        out.write(block)

print(f"Готово! Файл '{output_file}' создан.")


output_file = "music_list_radio.txt"

# Получаем список всех файлов в папке
files = os.listdir(folder_path)

# Фильтруем только .ogg файлы
ogg_files = [f for f in files if f.endswith(".ogg")]

with open(output_file, "w", encoding="utf-8") as out:
    for ogg in ogg_files:
        name = ogg[:-4]  # убираем ".ogg"
        block = f"""music = {{
\tname = "{name}"
}}\n"""
        out.write(block)

print(f"Готово! Файл '{output_file}' создан.")
