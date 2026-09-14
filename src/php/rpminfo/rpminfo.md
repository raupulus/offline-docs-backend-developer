---
title: rpminfo
description: Devuelve información de un fichero RPM
source_url: https://www.php.net/manual/es/function.rpminfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpminfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72500
---

rpminfo

Devuelve información de un fichero RPM

## Descripción

```php
rpminfo(string $path, [bool $full], [string $error]): array
```php

Devuelve información sobre un fichero local, un paquete RPM.

## Parámetros

`path`  
La ruta de acceso del fichero RPM.

`full`  
Si `true`, se recupera toda la información de cabecera del fichero, de lo contrario, solo un conjunto mínimo.

`error`  
Si se proporciona, recibirá el mensaje de error posible, y evitará una advertencia de ejecución.

## Valores devueltos

Un `array` de información, o `null` en caso de error.

## Ejemplos

Un ejemplo de `rpminfo`

```
<?php
rpmaddtag(RPMTAG_BUILDTIME);
$info = rpminfo("./php-pecl-rpminfo-0.4.2-1.el8.remi.7.4.x86_64.rpm");
print_r($info);
?>

   
```php

El ejemplo anterior mostrará:

    Array
    (
        [Name] => php-pecl-rpminfo
        [Version] => 0.4.2
        [Release] => 1.el8
        [Summary] => RPM information
        [Buildtime] => 1586244821
        [Arch] => x86_64
    )

## Véase también

rpmaddtag
