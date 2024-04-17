# Group Project ParkSpot_Monitor

README is available in the following languages:
<a href="https://https://github.com/olegdenko/ParkSpot_Monitor/blob/dev/README.md">
<img src="https://em-content.zobj.net/thumbs/120/apple/354/flag-ukraine_1f1fa-1f1e6.png" alt="UA" width="40" height="40"></a>
<a href="https://github.com/olegdenko/ParkSpot_Monitor/blob/dev/README.eng.md">
<img src="https://em-content.zobj.net/thumbs/120/apple/354/flag-united-states_1f1fa-1f1f8.png" alt="EN" width="40" height="40"></a>


## :purple_circle: **Overview**

**This is a group project of the *Park Spot Monitor* application for Django.**

## How could you use it

* Parking access control system
* Vehicle tracking system
* Time control of vehicles entrance and exit

## **Main Functionality**

The application has the following main functionality:
* Authentication and authorization
     * User and admin roles

* Administration
     * Adding users to the blacklist
     * Parking price management

* Work with license plates:
     * Addition, deletion of license plates
     * Recognition of the car number by the photo (using EasyOCR module)

* Payment for parking
     * Balance check
     * Payment for parking
     * Downloading data to a csv file

##  ** Installation and Project Launch** 

To work with the project, you need an `.env` file with environment variables.
Create it with the following content and *replace with your values*:

```dotenv
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_PORT=
POSTGRES_HOST= 

SECRET_KEY=

EMAIL_HOST_USER=example@meta.ua
EMAIL_HOST_PASSWORD=
EMAIL_PORT=465
EMAIL_HOST=smtp.meta.ua
```

Run the following commands in the project root:

* * Start the database
```bash
docker-compose up -d
```
## Sphinx Documentation
* [Sphinx] ()

## Project Authors
* [Oleg](https://github.com/olegdenko)
* [Viktoriia](https://github.com/Nilinzo)
* [Serhii](https://github.com/SerhiiAndreiko)
* [Oleksandr](https://github.com/SVcheburator)
* [Nikita](https://github.com/Nikita-devel)
