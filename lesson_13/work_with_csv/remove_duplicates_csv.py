import csv


# Зчитування з двох work_with_csv-файлів
def read_csv_rows(filepath):
    with open(filepath, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


rows1 = read_csv_rows("r-m-c.csv")
rows2 = read_csv_rows("random.csv")

# Поєднання списків і перетворення кожного рядка на кортеж (щоб можна було додати у множину)
combined_rows = rows1 + rows2
unique_rows = set(tuple(row) for row in combined_rows)

# Повертаємо назад у список списків
unique_rows_list = [list(row) for row in unique_rows]

# Запис у файл
with open("result_Romanchenko.csv", "w", newline="", encoding="utf-8") as result_file:
    writer = csv.writer(result_file)
    writer.writerows(unique_rows_list)

print("✅ Успішно збережено унікальні рядки у result_Romanchenko.csv")
