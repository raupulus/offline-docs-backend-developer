---
title: mysql_real_escape_string
description: Escapa caracteres especiales en una cadena para su uso en una sentencia
  SQL
source_url: https://www.php.net/manual/es/function.mysql-real-escape-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-real-escape-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52430
---

mysql_real_escape_string

Escapa caracteres especiales en una cadena para su uso en una sentencia SQL

> [!WARNING]
> Esta extensión estaba obsoleta en PHP 5.5.0, y fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_real_escape_string
>
> </div>
>
> <div data-wrapper="1" role="alternatives">
>
> PDO::quote
>
> </div>

## Descripción

```php
mysql_real_escape_string(string $unescaped_string, [resource $link_identifier]): string
```php

Escapa caracteres especiales en la cadena dada por `unescaped_string`, teniendo en cuenta el conjunto de caracteres en uso de la conexión, para que sea seguro usarla en `mysql_query`. Si se van a insertar datos binarios, se ha de usar esta función.

`mysql_real_escape_string` llama a la función mysql_real_escape_string de la biblioteca de MySQL, la cual antepone barras invertidas a los siguientes caracteres: `\x00`, `\n`, `\r`, `\`, `'`, `"` y `\x1a`.

Esta función siempre debe usarse (con pocas excepciones) para hacer seguros los datos antes de enviar una consulta a MySQL.

> [!CAUTION]
> El conjunto de caracteres debe ser establecido o bien a nivel del servidor, o bien con la función `mysql_set_charset` de la API para que afecte a `mysql_real_escape_string`. Véase la sección sobre los conceptos de [conjuntos de caracters](#mysqlinfo.concepts.charset) para más información.

## Parámetros

`unescaped_string`  
La cadena a escapar.

`link_identifier`  
La conexión MySQL. Si no se especifica, se utilizará la última conexión abierta con la función `mysql_connect`. Si no se encuentra una conexión de este tipo, la función intentará abrir una conexión, como si la función `mysql_connect` hubiera sido llamada sin argumento. Si no se encuentra o establece una conexión, se generará una alerta de nivel `E_WARNING`.

## Valores devueltos

Devuelve la cadena escapada, o `false` en caso de error.

## Errores/Excepciones

Ejecutar esta función sin una conexión de MySQL presente también emitirá errores de nivel `E_WARNING` de PHP. Solo se ha de ejecutar con una conexión de MySQL válida presente.

## Ejemplos

Ejemplo sencillo de `mysql_real_escape_string`

```
<?php
// Conexión
$enlace = mysql_connect('anfitrión_mysql', 'usuario_mysql', 'contraseña_mysql')
    OR die(mysql_error());

// Consulta
$consulta = sprintf("SELECT * FROM users WHERE user='%s' AND password='%s'",
            mysql_real_escape_string($usuario),
            mysql_real_escape_string($contraseña));
?>

   
```php

`mysql_real_escape_string` requiere una conexión

Este ejemplo muestra lo que sucede si no hay presente una conexión de MySQL al invocar a esta función.

```
<?php
// No nos hemos conectado a MySQL

$apellido  = "O'Reilly";
$_apellido = mysql_real_escape_string($apellido);

$consulta = "SELECT * FROM actors WHERE last_name = '$_apellido'";

var_dump($_apellido);
var_dump($consulta);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Warning: mysql_real_escape_string(): No such file or directory in /this/test/script.php on line 5
    Warning: mysql_real_escape_string(): A link to the server could not be established in /this/test/script.php on line 5

    bool(false)
    string(41) "SELECT * FROM actors WHERE last_name = ''"

Un ejemplo de ataque de inyección de SQL

```
<?php
// No hemos comprobado $_POST['password'], ¡podría ser cualquier cosa que el usuario quisiera! Por ejemplo:
$_POST['username'] = 'aidan';
$_POST['password'] = "' OR ''='";

// Consultar la base de datos para comprobar si existe algún usuario que coincida
$consulta = "SELECT * FROM users WHERE user='{$_POST['username']}' AND password='{$_POST['password']}'";
mysql_query($consulta);

// Esto significa que la consulta enviada a MySQL sería:
echo $consulta;
?>

   
```php

La consulta enviada a MySQL:

    SELECT * FROM users WHERE user='aidan' AND password='' OR ''=''

       

Esto permitiría a alguien acceder a una sesión sin una contraseña válida.

## Notas

> [!NOTE]
> Se requiere una conexión a MySQL antes de usar `mysql_real_escape_string`, si no, se generará un error de nivel `E_WARNING`, y se devolverá `false`. Si `link_identifier` no está definido, se usará la última conexión a MySQL.

> [!NOTE]
> Si esta función no se utiliza para escapar los datos, la consulta es vulnerable a [Ataques de inyección SQL](#security.database.sql-injection).

> [!NOTE]
> `mysql_real_escape_string` no escapa `%` ni `_`. Estos son comodines en MySQL si se combinan con `LIKE`, `GRANT`, o `REVOKE`.

## Véase también

mysql_set_charset

mysql_client_encoding
