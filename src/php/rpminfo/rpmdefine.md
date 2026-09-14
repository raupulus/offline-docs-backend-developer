---
title: rpmdefine
description: Define o cambia el valor de una macro RPM
source_url: https://www.php.net/manual/es/function.rpmdefine.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rpminfo/functions/rpmdefine.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rpminfo
translation_status: ready
translation_reviewed: true
translation_revision: 1d4f5d151
order: 72460
---

rpmdefine

Define o cambia el valor de una macro RPM

## Descripción

```php
rpmdefine(string $text): bool
```php

Define o cambia el valor de una macro RPM.

Puede ser utilizado para seleccionar la ruta de acceso de la base de datos y el motor a utilizar en lugar del predeterminado del sistema.

## Parámetros

`text`  
El nombre de la macro, las opciones, el cuerpo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Un ejemplo de `rpmdefine`

```
<?php
// utiliza una base de datos antigua (bdb) de un chroot EL-8
rpmdefine("_dbpath /var/lib/mock/almalinux-8-x86_64/root/var/lib/rpm");
rpmdefine("_db_backend bdb_ro");
print_r(rpmdbinfo("almalinux-release")[0]["Summary"]);

// utiliza una base de datos nueva (sqlite) de un chroot Fedora-41
rpmdefine("_dbpath /var/lib/mock/fedora-41-x86_64/root/usr/lib/sysimage/rpm");
rpmdefine("_db_backend sqlite");
print_r(rpmdbinfo("fedora-release")[0]["Summary"]);
?>

   
```php

El ejemplo anterior mostrará:

    AlmaLinux release file
    Fedora release files

## Véase también

rpmexpand

rpmdbinfo
