---
title: rpmdbsearch
description: Busca paquetes RPM
source_url: https://www.php.net/manual/es/function.rpmdbsearch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmdbsearch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72450
---

rpmdbsearch

Busca paquetes RPM

## Descripción

```php
rpmdbsearch(string $pattern, [int $rpmtag], [int $rpmmire], [bool $full]): array
```php

Busca paquetes en la base de datos RPM del sistema.

## Parámetros

`pattern`  
El valor a buscar.

`rpmtag`  
El criterio de búsqueda, una de las constantes `RPMTAG_*`.

`rpmmire`  
El tipo de patrón, una de las constantes `RPMMIRE_*`. Cuando \< 0 el criterio debe ser igual al valor, y el índice de la base de datos es utilizado si es posible.

`full`  
Si `true` toda la información de encabezado para el fichero es recuperada, de lo contrario solo un conjunto mínimo.

## Valores devueltos

Un `array` de `array` de información o `null` en caso de error.

## Ejemplos

Búsqueda del paquete que posee un fichero

```
<?php
$info = rpmdbsearch("/usr/bin/php", RPMTAG_INSTFILENAMES);
print_r($info);
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [Name] => php-cli
                [Version] => 7.4.4
                [Release] => 1.fc32
                [Summary] => Interfaz de línea de comandos para PHP
                [Arch] => x86_64
            )

    )

## Véase también

rpmaddtag
