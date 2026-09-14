---
title: mysqli::$connect_error
description: Devuelve una descripción del último error de conexión
source_url: https://www.php.net/manual/es/mysqli.connect-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/connect-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: a87dfa338
order: 54970
---

mysqli::\$connect_error

mysqli_connect_error

Devuelve una descripción del último error de conexión

## Descripción

Estilo orientado a objetos

string

null

mysqli-\>connect_error

Estilo procedimental

```php
mysqli_connect_error(): string
```php

Devuelve el mensaje de error del último intento de conexión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Una cadena que describe el error o `null` si no se produce ningún error.

Devuelve el último código de error de conexión, independientemente de la instancia en la que se invoque.

## Ejemplos

Ejemplo con `$mysqli->connect_error`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_OFF);

/* @ se utiliza para suprimir las advertencias */
$mysqli = @new mysqli('localhost', 'fake_user', 'wrong_password', 'does_not_exist');

if ($mysqli->connect_error) {
    /* Utilice su método preferido de registro de errores aquí */
    error_log('Connection error: ' . $mysqli->connect_error);
}

   
```php

Estilo procedimental

```
<?php

mysqli_report(MYSQLI_REPORT_OFF);

/* @ se utiliza para suprimir las advertencias */
$link = @mysqli_connect('localhost', 'fake_user', 'wrong_password', 'does_not_exist');

if (!$link) {
    /* Utilice su método preferido de registro de errores aquí */
    error_log('Connection error: ' . mysqli_connect_error());
}

   
```php

## Véase también

`mysqli_connect`, `mysqli_connect_errno`, `mysqli_errno`, `mysqli_error`, `mysqli_sqlstate`
