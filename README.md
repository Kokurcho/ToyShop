# Run venv + start server
```console
cd C:\virtualenv
python -m venv kokurcho
kokurcho\Scripts\activate.bat
cd C:\django\toy_shop
python manage.py runserver
```
# Django Admin
```url
http://127.0.0.1:8000/admin/
```
# Django ORM
```console
python manage.py shell
```
```shell
>>> from toyshop.models import Toy
>>> from toyshop.models import Manufacturer
```
Первый способ создания записи - сделать объект и через save() сохранить его в БД
```shell
>>> Manufacturer(name = 'AliBaba', address = 'China Town 9 Street')
<Manufacturer: AliBaba>
>>> m1 = _
>>> m1
<Manufacturer: AliBaba>
>>> m1.save()
```
Второй способ создания записи - через object manager
```shell
>>> # objects
>>> Manufacturer.objects
<django.db.models.manager.Manager object at 0x000001A8BA2FDE70>
>>> m5 = Manufacturer.objects.create(name = 'ZID', address = 'Kovrov, Lenin Street')
>>> m5
<Manufacturer: ZID>
```
Обратиться к полю объекта через точку
```shell
>>> m[3].address
'Kovrov Degtiarev Street 6'
```
Вывести все объекты модели Manufacturer через all()
```shell
>>> Manufacturer.objects.all()
<QuerySet [<Manufacturer: OOO "Detskiy MIR">, <Manufacturer: OAO Aliexpress>, <Manufacturer: AliBaba>, <Manufacturer: OOO Signal>, <Manufacturer: ZID>]>

```
Вывести все объекты модели Manufacturer через цикл
```shell
>>> for mi in m:
...     print(mi.name)
...
OOO "Detskiy MIR"
OAO Aliexpress
AliBaba
OOO Signal
ZID
```
Фильтр по конкретному значению
```shell
>>> m6 = Manufacturer.objects.create(name = 'KMZ', address = 'Kovrov, Lenin Street')
>>> Manufacturer.objects.filter(address = 'Kovrov, Lenin Street')
<QuerySet [<Manufacturer: ZID>, <Manufacturer: KMZ>]>
```
Фильтр с условием pk >= 3
```shell
>>> Manufacturer.objects.filter(pk__gte=3)
<QuerySet [<Manufacturer: AliBaba>, <Manufacturer: OOO Signal>, <Manufacturer: ZID>, <Manufacturer: KMZ>]>
```
Фильтр с условием pk <= 3
```shell
>>> Manufacturer.objects.filter(pk__lte=3)
<QuerySet [<Manufacturer: OOO "Detskiy MIR">, <Manufacturer: OAO Aliexpress>, <Manufacturer: AliBaba>]>
```
Вывести все записи, у которых pk != 3
```shell
>>> Manufacturer.objects.exclude(pk=3)
<QuerySet [<Manufacturer: OOO "Detskiy MIR">, <Manufacturer: OAO Aliexpress>, <Manufacturer: OOO Signal>, <Manufacturer: ZID>, <Manufacturer: KMZ>]>
```
Получить запись по ключу через get
```shell
>>> Manufacturer.objects.get(pk=3)
<Manufacturer: AliBaba>
```
Два запроса подряд - фильтр и сортировка
```shell
>>> Manufacturer.objects.filter(pk__lte=4).order_by('name')
<QuerySet [<Manufacturer: AliBaba>, <Manufacturer: OAO Aliexpress>, <Manufacturer: OOO "Detskiy MIR">, <Manufacturer: OOO Signal>]>
```
Сортировка в обычном порядке
```shell
>>> Manufacturer.objects.order_by('name')
<QuerySet [<Manufacturer: AliBaba>, <Manufacturer: KMZ>, <Manufacturer: OAO Aliexpress>, <Manufacturer: OOO "Detskiy MIR">, <Manufacturer: OOO Signal>, <Manufacturer: ZID>]>
```
Сортировка в обратном порядке
```shell
>>> Manufacturer.objects.order_by('-name')
<QuerySet [<Manufacturer: ZID>, <Manufacturer: OOO Signal>, <Manufacturer: OOO "Detskiy MIR">, <Manufacturer: OAO Aliexpress>, <Manufacturer: KMZ>, <Manufacturer: AliBaba>]>
```
Изменение записи
```shell
>>> mu = Manufacturer.objects.get(pk=2)
>>> mu
<Manufacturer: OAO Aliexpress>
>>> mu.title = 'OAO Aliexpress 2'
>>> mu.address = 'Japanese Street, 7'
>>> mu.save()
```
Удаление записей
```shell
>>> md = Manufacturer.objects.filter(pk__gte=4)
>>> md
<QuerySet [<Manufacturer: OOO Signal>, <Manufacturer: ZID>, <Manufacturer: KMZ>]>
>>> md.delete()
(3, {'toyshop.Manufacturer': 3})
```
Выйти из Shell
```shell
>>> quit()
```