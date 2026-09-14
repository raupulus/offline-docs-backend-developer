---
title: mysqli::get_warnings
description: Lee el resultado de SHOW WARNINGS
source_url: https://www.php.net/manual/es/mysqli.get-warnings.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysqli/mysqli/get-warnings.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysqli
translation_status: ready
translation_reviewed: true
translation_revision: 2cc28adf4
order: 55140
---

mysqli::get_warnings

mysqli_get_warnings

Lee el resultado de

SHOW WARNINGS

## Descripción

Estilo orientado a objetos

```php
public mysqli::get_warnings(): mysqli_warning
```php

Estilo procedimental

```php
mysqli_get_warnings(mysqli $mysql): mysqli_warning
```

Devuelve una lista simplemente enlazada compuesta de `mysqli_warning` o `false` si no hay advertencias. Cada objeto de la lista corresponde a una línea única del resultado de `SHOW WARNINGS`. Llamar a mysqli_warning::next rellenará el objeto con los valores de la línea siguiente.

> [!NOTE]
> Para recuperar los mensajes de advertencia, se recomienda utilizar el comando SQL `SHOW WARNINGS [LIMIT row_count]` en lugar de esta función.

> [!WARNING]
> La lista enlazada no puede ser reinicializada ni recuperada nuevamente.

## Parámetros

`mysql`  
Solo estilo procedimental: Un objeto `mysqli` devuelto por `mysqli_connect` o `mysqli_init`

## Valores devueltos

Devuelve una lista simplemente enlazada compuesta de `mysqli_warning` o `false` si no hay advertencias.

## Ejemplos

Recorrer la lista enlazada para recuperar todas las advertencias

Estilo orientado a objetos

```php
<?php

mysqli_report(MYSQLI_REPORT_ERROR | MYSQLI_REPORT_STRICT);
$mysqli = new mysqli("localhost", "my_user", "my_password", "world");

$mysqli->query("SELECT 1/0, CAST('NULL' AS UNSIGNED)");

if ($mysqli->warning_count > 0) {
    $warning = $mysqli->get_warnings();
    if ($warning !== false) {
        do {
            printf("Número de error: %s\n", $warning->errno);
            printf("Mensaje: %s\n", $warning->message);
        } while ($warning->next());
    }
}

    
```

Los ejemplos anteriores mostrarán:

    Número de error: 1365
    Mensaje: División por 0
    Número de error: 1292
    Mensaje: Valor INTEGER incorrecto truncado: 'NULL'
