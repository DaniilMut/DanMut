# Информационный объем дискеты в байтах
diskette_capacity_bytes = 1.44 * 1024 * 1024

# Параметры книги
pages_per_book = 100
lines_per_page = 50
characters_per_line = 25
bytes_per_character = 4

# Рассчитаем объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * characters_per_line * bytes_per_character

# Рассчитаем количество книг, которое можно разместить на дискете
num_books = diskette_capacity_bytes // book_size_bytes
num_books = round(num_books)

print("Количество книг, помещающихся на дискету:", num_books)