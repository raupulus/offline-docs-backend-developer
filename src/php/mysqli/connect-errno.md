---
title: mysqli::$connect_errno
description: Devuelve el código de error de la última llamada de conexión
source_url: https://www.php.net/manual/es/mysqli.connect-errno.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/connect-errno.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: false
translation_revision: a87dfa338
order: 54960
---

mysqli::\$connect_errno

mysqli_connect_errno

Devuelve el código de error de la última llamada de conexión

## Descripción

Estilo orientado a objetos

int

mysqli-\>connect_errno

Estilo procedimental

```php
mysqli_connect_errno(): int
```php

Devuelve el código de error del último intento de conexión.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un código de error para el último intento de conexión, si falla. Cero significa que no ha ocurrido ningún error.

Devuelve el último código de error de conexión, independientemente de la instancia en la que se llame.

## Ejemplos

Ejemplo con `$mysqli->connect_errno`

Estilo orientado a objetos

```
<?php

mysqli_report(MYSQLI_REPORT_OFF);

/* @ se utiliza para suprimir las advertencias */
$mysqli = @new mysqli('localhost', 'fake_user', 'wrong_password', 'does_not_exist');

if ($mysqli->connect_errno) {
    /* Utilice su método preferido de registro de errores aquí */
    error_log('Error de conexión: ' . $mysqli->connect_errno);
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
    error_log('Error de conexión: ' . mysqli_connect_errno());
}

   
```php

## Véase también

`mysqli_connect`, `mysqli_connect_error`, `mysqli_errno`, `mysqli_error`, `mysqli_sqlstate`
