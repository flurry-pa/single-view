# Music Works Single View. REST API test project
## About
A Single View application aggregates and reconciles data from multiple
sources to create a single view of an entity, in this case, a musical work.

This is a test project.

Application creates the Works Single View from the metadata in works_metadata.csv file.
This implies parsing the input file, detecting duplicate musical works and storing reconciled
works in a PostgreSQL database.
Metadata from some sources may be incomplete, the aim of the Works
Single View is to have, for each musical work, the most complete
metadata without duplicates.

Works Single View REST API is a simple API to query the Works Single View by
ISWC (International Standard Musical Work Code) in order to get the metadata related to that work.

Technology stack:
 - Python3
 - Django Framework
 - Django REST framework
 - PostgreSQL DB, SQLite DB
 - Docker, Docker Compose
 - Swagger OpenAPI documentation

 Designed by flurry <mailto:flurry.pa@gmail.com>

## Preview

<img alt="a relative link" src="/home/flurry/projects/031_test_Fevernova_BMAT_Spain/sv/static/sv/images/Swagger_OpenApi.png"/>

## Build
### install from source
Make sure you've installed Python3 (version >= 3.7).
The current code has been tested using Python v.3.10.
There are 2 options for installing the app: 
- in a virtual environment. Here app use SQLite DB, so, you need Python only;
- using Docker. If necessary, download it from the official source: https://docs.docker.com/get-docker/

### Option 1. Build with Docker
#### 1. Go to project directory:
```bash
cd <project directory>
```
#### 2. Build 2 containers
```bash
docker-compose build
```
#### 3. Run app from app root directory. 
Next time, start from this point
```bash
docker-compose up
```
#### 4. Look in browser
Single View Rest API documentation.
Try real requests!

 - Swagger OpenApi documentation: http://localhost:8000/sv/api/docs/
 - Redoc UI: http://localhost:8000/sv/redoc/ 

API request examples. 
 - list of the music works: http://localhost:8000/sv/api/v1/music_works/ 
 - list of the authors: http://localhost:8000/sv/api/v1/authors/ 

It's fully workable. You can test any API endpoint, any CRUD operation.
All data in DB will be restored from 'csv' file every time with new launch.

#### 4. To finish:
Quit the Django server with CONTROL-C. With this you are stopped all working containers.

### Option 2. Build in virtual environment
#### 1. Create virtual environment in app root directory and activate it.
```bash
python3 -m venv venv
source venv/bin/activate
```
#### 2. Install requirements in virtual environment and then deactivate virtual environment.
```bash
pip install -r requirements.txt
deactivate
``` 
#### 3. Run app from app root directory. 
Next time, start from this point
```bash
cd <app_root_directory>
bash run
```
#### 4. Look in browser
The same as for Docker case.

#### 5. To finish:
Quit the Django server with CONTROL-C.

Deactivate virtual environment:
```bash
deactivate
```
Well done!
