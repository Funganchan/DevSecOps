import os
import json
import xml.etree.ElementTree as ET
import zipfile
import psutil

class DiskInfo:
    @staticmethod
    def print_disk_info():
        """ Вывод информации о логических дисках """
        print(f"{'Диск':<10} {'Метка':<20} {'Размер (ГБ)':<15} {'Свободно (ГБ)':<15} {'ФС'}")
        print("=" * 80)
        
        # Получение списка всех логических дисков
        partitions = psutil.disk_partitions(all=False)  # Все партиции на системе
        for partition in partitions:
            try:
                # Получаем информацию о диске
                usage = psutil.disk_usage(partition.mountpoint)
                label = partition.device
                filesystem = partition.fstype
                
                # Форматируем вывод
                print(f"{partition.device:<10} {partition.mountpoint:<20} "
                      f"{usage.total / (1024 ** 3):<15.2f} {usage.free / (1024 ** 3):<15.2f} {filesystem}")
            except Exception as e:
                print(f"Ошибка при получении информации о {partition.device}: {e}")

    @staticmethod
    def main():
        """ Основной метод запуска """
        print("Информация о логических дисках:")
        DiskInfo.print_disk_info()

class FileManager:
    @staticmethod
    def create_file():
        """ Создание файла """
        filename = input("Введите имя файла для создания: ")
        with open(filename, 'w') as f:
            data = input("Введите строку для записи в файл: ")
            f.write(data)
        print(f"Файл {filename} создан и данные записаны.")

    @staticmethod
    def read_file():
        """ Чтение файла """
        filename = input("Введите имя файла для чтения: ")
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                print(f"Содержимое файла {filename}:")
                print(f.read())
        else:
            print(f"Файл {filename} не найден.")

    @staticmethod
    def delete_file():
        """ Удаление файла """
        filename = input("Введите имя файла для удаления: ")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Файл {filename} удален.")
        else:
            print(f"Файл {filename} не найден.")

class JSONManager:
    @staticmethod
    def create_json_file(filename):
        """ Создание JSON файла """
        obj = {}
        obj['name'] = input("Введите имя: ")
        obj['age'] = input("Введите возраст: ")
        
        with open(filename, 'w') as f:
            json.dump(obj, f, indent=4)

    @staticmethod
    def read_json_file(filename):
        """ Чтение JSON файла """
        with open(filename, 'r') as f:
            data = json.load(f)
            print("Данные из JSON файла:", data)

    @staticmethod
    def delete_json_file(filename):
        """ Удаление JSON файла """
        os.remove(filename)
        print(f"Файл {filename} удален.")

class XMLManager:
    @staticmethod
    def create_xml_file(filename):
        """ Создание XML файла """
        root = ET.Element("data")
        name = input("Введите имя: ")
        age = input("Введите возраст: ")
        
        ET.SubElement(root, "name").text = name
        ET.SubElement(root, "age").text = age
        
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Файл {filename} создан.")

    @staticmethod
    def read_xml_file(filename):
        """ Чтение XML файла """
        tree = ET.parse(filename)
        root = tree.getroot()
        for child in root:
            print(f"{child.tag}: {child.text}")

    @staticmethod
    def delete_xml_file(filename):
        """ Удаление XML файла """
        os.remove(filename)
        print(f"Файл {filename} удален.")

class ZipManager:
    @staticmethod
    def create_zip(zip_name):
        """ Создание ZIP архива """
        with zipfile.ZipFile(zip_name, 'w') as zipf:
            file_to_add = input("Введите имя файла для добавления в архив: ")
            zipf.write(file_to_add)
            print(f"Файл {file_to_add} добавлен в архив {zip_name}")


    @staticmethod
    def extract_zip(zip_name):
        """ Извлечение ZIP архива """
        with zipfile.ZipFile(zip_name, 'r') as zipf:
            zipf.extractall("extracted")
            print(f"Архив {zip_name} извлечен в папку 'extracted'.")

    @staticmethod
    def get_zip_size(zip_name):
        """ Получение размера ZIP архива """
        size = os.path.getsize(zip_name) / (1024 ** 2)  # в мегабайтах
        print(f"Размер архива {zip_name}: {size:.2f} MB")

    @staticmethod
    def delete_file(zip_file_name):
        """ Удаление ZIP файла """
        if os.path.exists(zip_file_name):
            os.remove(zip_file_name)
            print(f"{zip_file_name} был удален.")
        else:
            print(f"{zip_file_name} не найден.")

def main_menu():
    while True:
        print("\nВыберите действие:")
        print("1. Просмотр информации о дисках")
        print("2. Создать файл")
        print("3. Прочитать файл")
        print("4. Удалить файл")
        print("5. Создать JSON файл")
        print("6. Прочитать JSON файл")
        print("7. Удалить JSON файл")
        print("8. Создать XML файл")
        print("9. Прочитать XML файл")
        print("10. Удалить XML файл")
        print("11. Создать ZIP архив")
        print("12. Извлечь ZIP архив")
        print("13. Получить размер ZIP архива")
        print("14. Удалить ZIP файл")
        print("15. Выход")

        choice = input("Введите номер действия: ")

        if choice == '1':
            DiskInfo.print_disk_info()
        elif choice == '2':
            FileManager.create_file()
        elif choice == '3':
            FileManager.read_file()
        elif choice == '4':
            FileManager.delete_file()
        elif choice == '5':
            json_file_name = input("Введите имя для создания JSON файла: ")
            JSONManager.create_json_file(json_file_name)
        elif choice == '6':
            json_file_name = input("Введите имя JSON файла для чтения: ")
            JSONManager.read_json_file(json_file_name)
        elif choice == '7':
            json_file_name = input("Введите имя JSON файла для удаления: ")
            JSONManager.delete_json_file(json_file_name)
        elif choice == '8':
            xml_file_name = input("Введите имя для создания XML файла: ")
            XMLManager.create_xml_file(xml_file_name)
        elif choice == '9':
            xml_file_name = input("Введите имя XML файла для чтения: ")
            XMLManager.read_xml_file(xml_file_name)
        elif choice == '10':
            xml_file_name = input("Введите имя XML файла для удаления: ")
            XMLManager.delete_xml_file(xml_file_name)
        elif choice == '11':
            zip_file_name = input("Введите имя для создания ZIP архива: ")
            ZipManager.create_zip(zip_file_name)
        elif choice == '12':
            zip_file_name = input("Введите имя ZIP архива для извлечения: ")
            ZipManager.extract_zip(zip_file_name)
        elif choice == '13':
            zip_file_name = input("Введите имя ZIP архива для получения размера: ")
            ZipManager.get_zip_size(zip_file_name)
        elif choice == '14':
            zip_file_name = input("Введите имя ZIP архива для удаления: ")
            ZipManager.delete_file(zip_file_name)
        elif choice == '15':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор, пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main_menu()
