---
title: mysql_escape_string
description: Escapa una cadena para ser usada en mysql_query
source_url: https://www.php.net/manual/es/function.mysql-escape-string.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql/functions/mysql-escape-string.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql
translation_status: ready
translation_revision: 15d88bef8
order: 52140
---

mysql_escape_string

Escapa una cadena para ser usada en mysql_query

> [!WARNING]
> Esta función estaba obsoleta en PHP 4.3.0, y toda la [extensión original MySQL](#book.mysql) fue eliminada en PHP 7.0.0. En su lugar, se puede utilizar la extensión [MySQLi](#book.mysqli) o la extensión [PDO_MySQL](#ref.pdo-mysql). Ver también [MySQL: elegir una API](#mysqlinfo.api.choosing) de la guía. Alternativas a esta función:
>
> <div data-wrapper="1" role="alternatives">
>
> mysqli_escape_string
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
mysql_escape_string(string $unescaped_string): string
```php

Esta función escapará `unescaped_string`, para que sea segura ponerla en una `mysql_query`. Esta función está obsoleta.

Esta función es idéntica a `mysql_real_escape_string` excepto que `mysql_real_escape_string` toma un gestor de conexión y escapa la cadena de acuerdo con el juego de caracteres actual. `mysql_escape_string` no toma un argumento de conexión y no respeta la configuración del juego de caracteres actual.

## Parámetros

`unescaped_string`  
La cadena que va a ser escapada.

## Valores devueltos

Devuelve la cadena escapada.

## Ejemplos

Ejemplo de `mysql_escape_string`

```
<?php
$elemento = "Zak's Laptop";
$elemento_escapado = mysql_escape_string($elemento);
printf("Cadena escapada: %s\n", $elemento_escapado);
?>

   
```php

El ejemplo anterior mostrará:

    Cadena escapada: Zak\'s Laptop

## Notas

> [!NOTE]
> `mysql_escape_string` no escapa los caracteres `%` y `_`.

## Véase también

mysql_real_escape_string
