---
title: odbc_connection_string_quote
description: Pone entre comillas un valor de string de conexión ODBC
source_url: https://www.php.net/manual/es/function.odbc-connection-string-quote.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/uodbc/functions/odbc-connection-string-quote.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: uodbc
translation_status: ready
translation_reviewed: true
translation_revision: d80850163
order: 98720
---

odbc_connection_string_quote

Pone entre comillas un valor de string de conexión ODBC

## Descripción

```php
odbc_connection_string_quote(string $str): string
```php

Pone entre comillas un valor de string de conexión, según las reglas ODBC. Es decir, se rodeará de comillas, y cualquier llave de cierre será escapada. Esto debería hacerse para todos los valores de string de conexión que provienen de la entrada del usuario. No hacerlo puede provocar problemas durante el análisis de la string de conexión, o valores inyectados en la string de conexión.

Tenga en cuenta que esta función no verifica si la string ya está entre comillas, ni si la string necesita ser puesta entre comillas. Para ello, llamar a `odbc_connection_string_is_quoted` y a `odbc_connection_string_should_quote`.

## Parámetros

`str`  
La string sin comillas.

## Valores devueltos

Una string, rodeada de comillas, y correctamente escapada.

## Ejemplos

Ejemplo de `odbc_connection_string_quote`

Este ejemplo pone entre comillas una string, luego la coloca en una string de conexión. Tenga en cuenta que la string está entre comillas, y el carácter de comilla de cierre en medio de la string ha sido escapado.

```
<?php
$value = odbc_connection_string_quote("foo}bar");
$connection_string = "DSN=PHP;UserValue=$value";
echo $connection_string;
?>

   
```php

Resultado del ejemplo anterior es similar a:

    DSN=PHP;UserValue={foo}}bar}

## Véase también

`odbc_connection_string_is_quoted`, `odbc_connection_string_should_quote`
