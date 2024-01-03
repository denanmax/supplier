# Сеть по продаже электроники 

## Представляет собой иерархическую структуру из 3 уровней:

* Завод;
* Розничная сеть;
* Индивидуальный предприниматель.

_Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья - её уровень - 1._

## Каждое звено сети  обладает следующими элементами:

* Название;
* Контакты:
* Email;
* Страна;
* Город;
* Улица;
* Номер дома;
* Продукты:
* Название;
* Модель;
* Дата выхода продукта на рынок;
* Поставщик (предыдущий по иерархии объект сети);
* Задолженность перед поставщиком в денежном выражении с точностью до копеек;
* Время создания (заполняется автоматически при создании).

## На странице объекта сети имеется:

* ссылка на «Поставщика»;
* фильтр по названию города;
* «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

_CRUD для модели поставщика (запрещено обновление через API поля «Задолженность перед поставщиком»);_

_Добавлена возможность фильтрации объектов по определенной стране._

_Настроены права доступа к API так, чтобы только активные сотрудники имели доступ к API._