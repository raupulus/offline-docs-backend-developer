---
title: xhprof_sample_disable
description: Detiene el perfilado xhprof por muestreo
source_url: https://www.php.net/manual/es/function.xhprof-sample-disable.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xhprof/functions/xhprof-sample-disable.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xhprof
translation_status: ready
translation_revision: a9220267e
order: 102330
---

xhprof_sample_disable

Detiene el perfilado xhprof por muestreo

## Descripción

```php
xhprof_sample_disable(): array
```php

Detiene el perfilado xhprof por muestreo y devuelve la información de perfilado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `array` de datos de muestreo xhprof, procedentes de su ejecución. Devuelve `null` si el perfilado no está activado.

## Ejemplos

Ejemplo con `xhprof_sample_disable`

```
<?php
xhprof_sample_enable();

for ($i = 0; $i <= 10000; $i++) {
    $a = strlen($i);
    $b = $i * $a;
    $c = rand();
}

$xhprof_data = xhprof_sample_disable();

print_r($xhprof_data);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [1272935300.800000] => main()
        [1272935300.900000] => main()
    )
