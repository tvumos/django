# Проект разработки сайта Совета депутатов муниципального округа "Якиманка" города Москвы
### Текущая версия сайта: http://mo-yakimanka.ru/

Сайт разрабатывается для замены текущей версии портала и добавления новых функций 
и возможностей по взаимодействию с гражданами района.

Текущий статус:
- Проект разрабатывается на Django
- Спроектирована и реализована стартовая структура базы данных
- Реализованы 3 дополнительных команды:
    * fill_db - первоначальное заполнение базы;
    * select_db - просмотр всех таблиц базы данных
    * clear_db - очистка записей всех таблиц базы данных
    
Требуемые библиотеки указаны в файле:
requirement.txt

Для первонаяальной загрузки данные берутся из CSV файлов с каталоге "content".
В каталоге "content" находится графическая схема базы данных, файл shema.png.




