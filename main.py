file_size_gb = float(input("Введіть розмір файлу в гігабайтах: "))
internet_speed_bps = float(input("Введіть швидкість інтернет-з'єднання в бітах на секунду: "))
choice = input("Оберіть 'години', 'хвилини' або 'секунди' для обчислення часу завантаження (введіть '1' або '2' або '3'): ")
file_size_bits = file_size_gb * 8 * 1024 * 1024 * 1024
download_time_seconds = file_size_bits / internet_speed_bps
if choice == '1':
    download_time = download_time_seconds / 3600
    print(f"Час завантаження файлу: {download_time:.2f} годин.")
elif choice == '2':
    download_time = download_time_seconds / 60
    print(f"Час завантаження файлу: {download_time:.2f} хвилин.")
elif choice == '3':
    print(f"Час завантаження файлу: {download_time_seconds:.2f} секунд.")
else:
    print("Неправильний вибір. Будь ласка, введіть 'години', 'хвилини' або 'секунди'.")