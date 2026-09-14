---
title: RarArchive::isSolid
description: Comprueba si el archivo RAR es sólido
source_url: https://www.php.net/manual/es/rararchive.issolid.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/issolid.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_revision: ee741f54f
order: 68450
---

RarArchive::isSolid

rar_solid_is

Comprueba si el archivo RAR es sólido

## Descripción

Estilo orientado a objetos (método):

```php
public RarArchive::isSolid(): bool
```php

Estilo procedimental:

```php
rar_solid_is(RarArchive $rarfile): bool
```

Comprueba si el archivo RAR es sólido. La extracción individual de ficheros es más lenta en archivos sólidos.

## Parámetros

`rarfile`  
La instancia del `RarArchive`, abierto con `rar_open`.

## Valores devueltos

Devuelve `true` si el archivo es sólido, de lo contrario retorna `false`.

## Ejemplos

Estilo orientado a objetos

```php
<?php
$arch1 = RarArchive::open("store_method.rar");
$arch2 = RarArchive::open("solid.rar");
echo "$arch1: " . ($arch1->isSolid()?'yes':'no') ."\n";
echo "$arch2: " . ($arch2->isSolid()?'yes':'no') . "\n";
?>

    
```

Resultado del ejemplo anterior es similar a:

    RAR Archive "C:\php_rar\trunk\tests\store_method.rar": no
    RAR Archive "C:\php_rar\trunk\tests\solid.rar": yes

Estilo procedimental

```php
<?php
$arch1 = rar_open("store_method.rar");
$arch2 = rar_open("solid.rar");
echo "$arch1: " . (rar_solid_is($arch1)?'yes':'no') ."\n";
echo "$arch2: " . (rar_solid_is($arch2)?'yes':'no') . "\n";
?>

    
```
