# tests/test_usefixtures.py
import pytest

# Фикстура для очистки данных из базы данных
@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Удаляем все данные из базы данных")

# Фикстура для заполнения данных в базу данных
@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Создаем новые данные в базе данных")

# Тест с использованием одной фикстуры через usefixtures
@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print("Тест: читаем все книги в библиотеке")
    # Здесь можно писать проверки, например, что книги созданы
    assert True

# Класс с несколькими тестами и несколькими фикстурами через usefixtures
@pytest.mark.usefixtures('clear_books_database', 'fill_books_database')
class TestLibrary:
    def test_read_book_from_library(self):
        print("Тест: читаем книгу из библиотеки")
        assert True

    def test_delete_book_from_library(self):
        print("Тест: удаляем книгу из библиотеки")
        assert True