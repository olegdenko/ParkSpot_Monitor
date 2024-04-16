# Груповий проект ParkSpot_Monitor

README доступно такими мовами:
<a href="https://https://github.com/olegdenko/ParkSpot_Monitor/blob/dev/README.md">
<img src="https://em-content.zobj.net/thumbs/120/apple/354/flag-ukraine_1f1fa-1f1e6.png" alt="UA" width="40" height="40"></a>
<a href="https://github.com/olegdenko/ParkSpot_Monitor/blob/dev/README.eng.md">
<img src="https://em-content.zobj.net/thumbs/120/apple/354/flag-united-states_1f1fa-1f1f8.png" alt="EN" width="40" height="40"></a>


## **Огляд**

**Це груповий проект Django застосунку *Park Spot Monitor*.**

## Як можна використовувати проект

* Система контролю доступу на парковку
* Система відстеження транспортних засобів
* Визначення часу заїзду та виїзду транспортних засобів

##  **Основний функціонал**

Застосунок має такий основний функціонал:
* Аутентифікація та авторизація
    * Створення користувача та адміністратора

* Адміністрування
    * Додавання користувачів в чорний список
    * Керування ціною за паркування

* Робота з номерними знаками:
    * Додавання, видалення номерних знаків
    * Розпізнавання номеру машини за фото

* Оплата за парковку
    * Перевірка балансу
    * Оплата за парковку
    * Завантаження даних у csv файл

## **Встановлення та запуск проекту** 

Для роботи проекта необхідний файл `.env` зі змінними оточення.
Створіть його з таким вмістом і *підставте свої значення*:

```dotenv
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=
POSTGRES_HOST= 


SECRET_KEY=
```

Виконайте наступні команди в корені проекту:
```bash
docker-compose up -d
```
## Sphinx документація
* [Sphinx] ()

##  **Автори проекту** 
* [Oleg](https://github.com/olegdenko)
* [Viktoriia](https://github.com/Nilinz)
* [Serhii](https://github.com/SerhiiAndreiko)
* [Oleksandr](https://github.com/SVcheburator)