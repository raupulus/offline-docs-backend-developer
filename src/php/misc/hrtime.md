---
title: hrtime
description: Devuelve el tiempo de alta resolución del sistema
source_url: https://www.php.net/manual/es/function.hrtime.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/misc/functions/hrtime.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: misc
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 47120
---

hrtime

Devuelve el tiempo de alta resolución del sistema

## Descripción

```php
hrtime([bool $as_number]): array
```php

Devuelve el tiempo de alta resolución del sistema, contado a partir de un punto arbitrario en el tiempo. La marca de tiempo proporcionada es monótona y no puede ser ajustada.

## Parámetros

`as_number`  
Si el tiempo de alta resolución debe ser devuelto como `array` o como número.

## Valores devueltos

Devuelve un array de enteros en la forma \[segundos, nanosegundos\], si el argumento `as_number` es falso. De lo contrario, los nanosegundos son devueltos como `int` (plataformas de 64 bits) o como `float` (plataformas de 32 bits). Devuelve `false` en caso de error.

## Ejemplos

Ejemplo de `hrtime`

```
<?php
echo hrtime(true), PHP_EOL;
print_r(hrtime());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    10444739687370679
    Array
    (
        [0] => 10444739
        [1] => 687464812
    )

## Véase también

La extensión de

Gestión del tiempo de alta resolución

microtime
