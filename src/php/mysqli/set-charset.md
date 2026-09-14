---
title: mysqli::set_charset
description: Define el juego de caracteres del cliente
source_url: https://www.php.net/manual/es/mysqli.set-charset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/set-charset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: f977ae030
order: 55360
---

mysqli::set_charset

mysqli_set_charset

Define el juego de caracteres del cliente

## Descripción

Estilo orientado a objetos

```php
public mysqli::set_charset(string $charset): bool
```php

Estilo procedimental

```php
mysqli_set_charset(mysqli $mysql, string $charset): bool
```

Define el juego de caracteres a utilizar al enviar datos desde y hacia el servidor de base de datos.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

`charset`  
El juego de caracteres a definir.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si el informe de errores de mysqli está habilitado (`MYSQLI_REPORT_ERROR`) y la operación solicitada falla, se genera una advertencia. Si, además, el modo está configurado como `MYSQLI_REPORT_STRICT`, se lanza una `mysqli_sql_exception` en su lugar.

## Ejemplos

Ejemplo con mysqli::set_charset

Estilo orientado a objetos

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "test");

printf("Juego de caracteres inicial: %s\n", $mysqli->character_set_name());

/* Cambio del juego de resultados a utf8mb4 */
$mysqli->set_charset("utf8mb4");

printf("Juego de caracteres actual: %s\n", $mysqli->character_set_name());
?>

   
```

Estilo procedimental

```php
<?php
mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$link = mysqli_connect('localhost', 'my_user', 'my_password', 'test');

printf("Juego de caracteres inicial: %s\n", mysqli_character_set_name($link));

/* Cambio del juego de resultados a utf8mb4 */
mysqli_set_charset($link, "utf8mb4");

printf("Juego de caracteres actual: %s\n", mysqli_character_set_name($link));
?>

   
```

Los ejemplos anteriores mostrarán algo similar a:

    Juego de caracteres inicial: latin1
    Juego de caracteres actual: utf8mb4

## Notas

> [!NOTE]
> Esta es la mejor forma de modificar el juego de caracteres. No se recomienda utilizar la función `mysqli_query` para definirlo (como con la consulta `SET NAMES utf8`). Ver la sección [Conceptos de juegos de caracteres de MySQL](#mysqlinfo.concepts.charset) para más información.

## Véase también

`mysqli_character_set_name`, `mysqli_real_escape_string`, [Conceptos de juegos de caracteres de MySQL](#mysqlinfo.concepts.charset), [Lista de juegos de caracteres soportados por MySQL](http://dev.mysql.com/doc/mysql/en/charset-charsets.html)
