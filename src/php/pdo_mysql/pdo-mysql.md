---
title: La clase Pdo\Mysql
source_url: https://www.php.net/manual/es/class.pdo-mysql.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo_mysql/pdo-mysql.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo_mysql
translation_status: ready
translation_reviewed: true
translation_revision: ae7db14ea
order: 62400
---

## Introducción

Una subclase de `PDO` que representa una conexión utilizando el controlador PDO MySQL.

Este controlador admite un analizador de consultas SQL dedicado para el dialecto MySQL. Puede gestionar los siguientes elementos:

- Literales entre comillas simples y dobles con duplicación y barra invertida como mecanismos de escape

- Literales con acento grave con duplicación como mecanismo de escape

- Dos guiones, comentarios de estilo C y comentarios de tipo hash

## Sinopsis de la clase

Pdo\Mysql

extends

PDO

Constantes heredadas

Constantes

public

const

int

Pdo\Mysql::ATTR_USE_BUFFERED_QUERY

public

const

int

Pdo\Mysql::ATTR_LOCAL_INFILE

public

const

int

Pdo\Mysql::ATTR_LOCAL_INFILE_DIRECTORY

public

const

int

Pdo\Mysql::ATTR_INIT_COMMAND

public

const

int

Pdo\Mysql::ATTR_MAX_BUFFER_SIZE

public

const

int

Pdo\Mysql::ATTR_READ_DEFAULT_FILE

public

const

int

Pdo\Mysql::ATTR_READ_DEFAULT_GROUP

public

const

int

Pdo\Mysql::ATTR_COMPRESS

public

const

int

Pdo\Mysql::ATTR_DIRECT_QUERY

public

const

int

Pdo\Mysql::ATTR_FOUND_ROWS

public

const

int

Pdo\Mysql::ATTR_IGNORE_SPACE

public

const

int

Pdo\Mysql::ATTR_MULTI_STATEMENTS

public

const

int

Pdo\Mysql::ATTR_SERVER_PUBLIC_KEY

public

const

int

Pdo\Mysql::ATTR_SSL_KEY

public

const

int

Pdo\Mysql::ATTR_SSL_CERT

public

const

int

Pdo\Mysql::ATTR_SSL_CA

public

const

int

Pdo\Mysql::ATTR_SSL_CAPATH

public

const

int

Pdo\Mysql::ATTR_SSL_CIPHER

public

const

int

Pdo\Mysql::ATTR_SSL_VERIFY_SERVER_CERT

Métodos

Métodos heredados

## Constantes predefinidas

`Pdo\Mysql::ATTR_USE_BUFFERED_QUERY`  
Por omisión, todas las consultas se ejecutan en [modo almacenado en búfer](#mysqlinfo.concepts.buffering). Si este atributo se define como `false` en un objeto `Pdo\Mysql`, el controlador MySQL utilizará el modo sin búfer.

Activación del modo sin búfer MySQL

```php
<?php
$pdo = new Pdo\Mysql("mysql:host=localhost;dbname=world", 'my_user', 'my_password');
$pdo->setAttribute(PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, false);

$unbufferedResult = $pdo->query("SELECT Name FROM City");
foreach ($unbufferedResult as $row) {
    echo $row['Name'] . PHP_EOL;
}
?>

       
```

`Pdo\Mysql::ATTR_LOCAL_INFILE`  
Activa `LOAD LOCAL INFILE`.

> [!NOTE]
> Puede utilizarse únicamente en el array `driver_options` al construir una nueva conexión a la base de datos.

`Pdo\Mysql::ATTR_LOCAL_INFILE_DIRECTORY`  
Permite restringir la carga de datos locales a los ficheros situados en este directorio designado.

`Pdo\Mysql::ATTR_INIT_COMMAND`  
El comando a ejecutar al conectarse al servidor MySQL. Se reejecutará automáticamente al reconectar.

`Pdo\Mysql::ATTR_READ_DEFAULT_FILE`  
Leer las opciones del fichero de opciones nombrado en lugar de `my.cnf`.

> [!NOTE]
> Esta opción no está disponible si se utiliza mysqlnd, ya que mysqlnd no lee los ficheros de configuración mysql.

`Pdo\Mysql::ATTR_READ_DEFAULT_GROUP`  
Lee las opciones del grupo nombrado del fichero `my.cnf` o el fichero especificado con `Pdo\Mysql::ATTR_READ_DEFAULT_FILE`.

> [!NOTE]
> Esta opción no está disponible si se utiliza mysqlnd, ya que mysqlnd no lee los ficheros de configuración mysql.

`Pdo\Mysql::ATTR_COMPRESS`  
Activa la compresión de la comunicación de red.

`Pdo\Mysql::ATTR_DIRECT_QUERY`  
Alias de `PDO::ATTR_EMULATE_PREPARES`.

`Pdo\Mysql::ATTR_FOUND_ROWS`  
Devuelve el número de filas encontradas (coincidentes), no el número de filas modificadas.

`Pdo\Mysql::ATTR_IGNORE_SPACE`  
Permite espacios después de los nombres de funciones SQL. Convierte todos los nombres de funciones SQL en palabras reservadas.

`Pdo\Mysql::ATTR_MAX_BUFFER_SIZE`  
El tamaño máximo del búfer. Por omisión, 1 MB.

> [!NOTE]
> Esta constante no está soportada cuando se compila sin mysqlnd.

`Pdo\Mysql::ATTR_MULTI_STATEMENTS`  
Desactiva la ejecución de consultas múltiples en PDO::prepare y PDO::query cuando se define como `false`.

`Pdo\Mysql::ATTR_SERVER_PUBLIC_KEY`  
RSA la ruta del fichero de clave pública utilizada con la autenticación basada en SHA-256.

`Pdo\Mysql::ATTR_SSL_KEY`  
La ruta del fichero de clave SSL.

`Pdo\Mysql::ATTR_SSL_CERT`  
La ruta del certificado SSL.

`Pdo\Mysql::ATTR_SSL_CA`  
La ruta del certificado de autoridad SSL.

`Pdo\Mysql::ATTR_SSL_CAPATH`  
La ruta del directorio que contiene los certificados de autoridad SSL CA, almacenados en formato PEM.

`Pdo\Mysql::ATTR_SSL_CIPHER`  
Una lista de uno o más cifrados autorizados para utilizar con SSL, en un formato comprendido por OpenSSL. Por ejemplo: `DHE-RSA-AES256-SHA:AES128-SHA`

`Pdo\Mysql::ATTR_SSL_VERIFY_SERVER_CERT`  
Proporciona un medio para desactivar la verificación del certificado del servidor SSL.

> [!NOTE]
> Esta opción está disponible únicamente con mysqlnd.
