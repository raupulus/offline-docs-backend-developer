---
title: rpmdbinfo
description: Devuelve la información de un RPM instalado
source_url: https://www.php.net/manual/es/function.rpmdbinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmdbinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72440
---

rpmdbinfo

Devuelve la información de un RPM instalado

## Descripción

```php
rpmdbinfo(string $nevr, [bool $full]): array
```php

Recupera la información sobre un paquete instalado, desde la base de datos RPM del sistema.

## Parámetros

`nevr`  
El nombre con opcionalmente el epoch, la versión y la release.

`full`  
Si es `true`, se recupera toda la información de cabecera del fichero, de lo contrario, solo un conjunto mínimo.

## Valores devueltos

Un `array` de `array` de información o NULL en caso de error.

## Ejemplos

Un ejemplo de `rpmdbinfo`

```
<?php
rpmaddtag(RPMTAG_INSTALLTIME);
$info = rpmdbinfo("php-pecl-rpminfo");
print_r($info);
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => Array
            (
                [Name] => php-pecl-rpminfo
                [Version] => 0.4.2
                [Release] => 1.fc31
                [Summary] => RPM information
                [Installtime] => 1586244687
                [Arch] => x86_64
            )
    )

## Véase también

rpmaddtag
