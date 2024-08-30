from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    def test_add_new_book_not_add_book_with_long_name(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и методы рационального мышления')

        assert len(collector.books_genre) == 0

    def test_add_new_book_new_book_have_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер и Узник Азкабана')

        assert collector.books_genre['Гарри Поттер и Узник Азкабана'] == ''

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Гордость и предубеждение и зомби', 'Комедии'],
            ['Что делать, если ваш кот хочет вас убить', 'Детективы']
        ]
    )
    def test_set_book_genre_set_genres_from_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.books_genre[name] == genre

    def test_set_book_genre_set_genre_not_from_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Драма')

        assert collector.books_genre['Гордость и предубеждение и зомби'] == ''

    @pytest.mark.parametrize('name, genre', [['Дюна', 'Фантастика'], ['Солярис', 'Фантастика']])
    def test_get_book_genre_can_find_genre_by_book_name(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', [['Дюна', 'Фантастика'], ['Солярис', 'Фантастика']])
    def test_get_books_with_specific_genre_with_genre_from_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre(genre) == [name]

    def test_get_books_with_specific_genre_with_genre_from_list_for_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна', 'Солярис']

    def test_test_get_books_with_specific_genre_from_list_genre_not_from_list_not_add_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит или туда и обратно')
        collector.set_book_genre('Хоббит или туда и обратно', 'Биография')

        assert collector.get_books_with_specific_genre('Биография') == []

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дом, в котором')

        assert collector.get_books_genre() == {'Дом, в котором': ''}

    def test_get_books_for_children_genre_not_in_age_rating_add_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Ловец снов')
        collector.set_book_genre('Ловец снов', 'Фантастика')

        assert collector.get_books_for_children() == ['Ловец снов']

    def test_get_books_for_children_genre_in_age_rating_not_add_to_list(self):
        collector = BooksCollector()
        collector.add_new_book('Ловец снов')
        collector.set_book_genre('Ловец снов', 'Ужасы')
        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize('name', ['Ловец снов', 'Темная Башня'])
    def test_get_list_of_favorites_books_add_book_to_list_show_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    @pytest.mark.parametrize('name', ['Ловец снов', 'Темная Башня'])
    def test_delete_book_from_favorites_book_deleted(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites == [name]
        collector.delete_book_from_favorites(name)
        assert collector.favorites == []

    @pytest.mark.parametrize('name, genre', [['Дюна', 'Фантастика'], ['Солярис', 'Фантастика']])
    def test_get_books_with_specific_genre_from_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_books_with_specific_genre(genre) == [name]
