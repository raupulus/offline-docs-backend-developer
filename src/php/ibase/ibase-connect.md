---
title: ibase_connect
description: Abre una conexión a una base de datos
source_url: https://www.php.net/manual/es/function.ibase-connect.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-connect.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30250
---

ibase_connect

Abre una conexión a una base de datos

## Descripción

```php
ibase_connect([string $database], [string $username], [string $password], [string $charset], [int $buffers], [int $dialect], [string $role], [int $sync]): resource
```php

Abre una conexión a una base de datos Firebird/InterBase.

Si se realiza una segunda llamada con `ibase_connect`, pasando los mismos argumentos, no se abrirá una nueva conexión, sino que se devolverá la conexión ya abierta. La conexión se cerrará cuando el script termine, a menos que se cierre explícitamente con `ibase_close`, durante el script.

## Parámetros

`database`  
`database` debe ser una ruta válida hasta un fichero de base de datos en el servidor en el cual reside. Si el servidor es remoto, debe ser prefijado con un nombre de host 'hostname:' (TCP/IP), 'hostname/port:' (TCP/IP con un servidor interbase en un puerto TCP personalizado), '//hostname/' (NetBEUI) según el protocolo de comunicación utilizado.

`username`  
El nombre de usuario. Puede ser definido con la directiva `ibase.default_user` del fichero `php.ini`.

`password`  
La contraseña correspondiente al usuario `username`. Puede ser definida con la directiva `ibase.default_password` del fichero `php.ini`.

`charset`  
`charset` es el juego de caracteres por defecto para la base de datos.

`buffers`  
`buffers` es el número de buffers de base a asignar para la caché del servidor. Si se pasa a 0 o se omite, el servidor lo elegirá por sí mismo.

`dialect`  
`dialect` selecciona el dialecto SQL para las consultas ejecutadas con esta conexión y, por defecto, utiliza el mejor dialecto disponible.

`role`  
Funciona solo con InterBase 5 y superiores.

`sync`  

## Valores devueltos

Devuelve un identificador de conexión Firebird/InterBase en caso de éxito, o `false` si ocurre un error.

## Errores/Excepciones

Si se encuentran errores como `"arithmetic exception, numeric overflow, or string truncation. Cannot transliterate character between character sets"` (esto ocurre cuando se intenta utilizar algunos caracteres acentuados) al utilizar `ibase_connect` y después `ibase_query`, se debe especificar un juego de caracteres correcto (i.e. `ISO8859_1` o su juego de caracteres actual).

## Ejemplos

Ejemplo con `ibase_connect`

```
<?php
$host = 'localhost:/path/to/your.gdb';

$dbh = ibase_connect($host, $username, $password);
$stmt = 'SELECT * FROM tblname';
$sth = ibase_query($dbh, $stmt);
while ($row = ibase_fetch_object($sth)) {
    echo $row->email, "\n";
}
ibase_free_result($sth);
ibase_close($dbh);
?>

   
```php

## Véase también

ibase_pconnect

ibase_close
