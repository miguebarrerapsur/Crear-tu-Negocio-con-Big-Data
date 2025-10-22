crear entorno pyhon 
python3 -m venv venv/

conectarte entorno
source venv/bin/activate

instalar dependencias 
pip install -r requirements.txt

crear contenedor mysql
docker build -t mysql-image -f Dockerfile .

ejecutar contenedor mysql

docker run -d \
  --name mysql-container \
  -v ./data/:/var/lib/mysql \
  -e MYSQL_DATABASE=bigdata_db \
  -e MYSQL_USER=bigdata_user \
  -e MYSQL_PASSWORD=bigdata_password \
  -e MYSQL_ROOT_PASSWORD=root_password \
  -p 3307:3306 \
  mysql-image


crear contenedor maria db
docker build -t mariadb-image -f Dockerfile .

ejecutar contenedor mariadb
docker run --detach --name mariadb-container --env MARIADB_USER=bigdata_user --env MARIADB_PASSWORD=bigdata_password --env MARIADB_DATABASE=bigdata_db --env MARIADB_ROOT_PASSWORD=root_password -p 8081:8081 mariadb-image