---
title: PDO::__construct
description: Crea una instancia PDO que representa una conexión a la base de datos
source_url: https://www.php.net/manual/es/pdo.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/pdo/pdo/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: pdo
translation_status: ready
translation_reviewed: false
translation_revision: 7dd805d34
order: 61850
---

PDO::\_\_construct

Crea una instancia PDO que representa una conexión a la base de datos

## Descripción

```php
public #[\SensitiveParameter] PDO::__construct(string $dsn, [string $username], [string $password], [array $options])
```php

Crea un objeto PDO que representa una conexión a la base de datos.

## Parámetros

`dsn`  
El Data Source Name, o DSN, que contiene las informaciones requeridas para conectarse a la base de datos.

Generalmente, un DSN está compuesto por el nombre del controlador PDO, seguido de una sintaxis específica del controlador. Más detalles están disponibles en la documentación [PDO](#pdo.drivers) de cada controlador.

El parámetro `dsn` soporta tres métodos diferentes para especificar los argumentos necesarios para la creación de la base de datos:

Invocación de controlador  
`dsn` contiene el DSN completo.

Invocación URI  
`dsn` está compuesto por `uri:` seguido por una URI que define la localización del fichero que contiene la cadena DSN. La URI puede especificar un fichero local o remoto.

`uri:file:///path/to/dsnfile`

Alias  
`dsn` está compuesto por un nombre `name` que corresponde a `pdo.dsn.name` en el fichero `php.ini`, y que define la cadena DSN.

> [!NOTE]
> El alias debe ser definido en el fichero `php.ini`, y no en un fichero `.htaccess` o `httpd.conf`

`username`  
El nombre de usuario para la cadena DSN. Este parámetro es opcional para algunos controladores PDO.

`password`  
La contraseña de la cadena DSN. Este parámetro es opcional para algunos controladores PDO.

`options`  
Un array clave=\>valor con las opciones específicas de conexión.

## Errores/Excepciones

Se lanza una excepción `PDOException` si el intento de conexión a la base de datos solicitada falla, independientemente del `PDO::ATTR_ERRMODE` actualmente definido.

## Ejemplos

Crea una instancia PDO mediante una invocación de controlador

```
<?php

$dsn = 'mysql:dbname=testdb;host=127.0.0.1';
$user = 'dbuser';
$password = 'dbpass';

$dbh = new PDO($dsn, $user, $password);

?>

    
```php

Crea una instancia PDO mediante una invocación URI

El ejemplo siguiente supone que el fichero `/usr/local/dbconnect` existe con permisos de acceso que permiten a PHP acceder a él. El fichero contiene entonces el DSN de PDO, para conectarse a una base de datos DB2, con el controlador PDO_ODBC:

    odbc:DSN=SAMPLE;UID=john;PWD=mypass

        

El script PHP puede entonces crear una conexión a la base de datos, pasando en la URL el parámetro `uri:` y apuntando a la URI del fichero:

```
<?php

$dsn = 'uri:file:///usr/local/dbconnect';
$user = '';
$password = '';

$dbh = new PDO($dsn, $user, $password);

?>

    
```php

Crea una instancia PDO con un alias

El ejemplo siguiente supone que el fichero `php.ini` contiene la directiva siguiente para activar una conexión a un servidor MySQL, con el alias `mydb`:

```
[PDO]
pdo.dsn.mydb="mysql:dbname=testdb;host=localhost"
    
```php

```
<?php

$dsn = 'mydb';
$user = '';
$password = '';

$dbh = new PDO($dsn, $user, $password);

?>

    
```php
