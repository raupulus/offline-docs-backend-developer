---
title: RarArchive::isBroken
description: Comprobar si un archivo está dañado (incompleto)
source_url: https://www.php.net/manual/es/rararchive.isbroken.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/isbroken.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68440
---

RarArchive::isBroken

rar_broken_is

Comprobar si un archivo está dañado (incompleto)

## Descripción

Estilo orientado a objetos (método):

```php
public RarArchive::isBroken(): bool
```php

Estilo procedimental:

```php
rar_broken_is(RarArchive $rarfile): bool
```

Esta función determina si un archivo está incompleto, por ejemplo, Si un volumen no se encuentra o un volumen está truncado.

## Parámetros

`rarfile`  
Un objeto `RarArchive`, abierto con `rar_open`.

## Valores devueltos

Devuelve `true` si el archivo está dañado, `false` en caso contrario. Esta función puede también devolver `false` si el archivo pasado fue cerrado. La única manera para poder distinguir aparte ambos casos es habilitando y permitiendo excepciones con RarException::setUsingExceptions; sin embargo, esto debería ser innecesario, ya que un programa no debe funcionar con archivos cerrados.

## Ejemplos

Estilo orientado a objetos

```php
<?php
function retnull() { return null; }
$file = dirname(__FILE__) . "/multi_broken.part1.rar";
/* El tercer argumento es utilizado para omitir avisos */
$arch = RarArchive::open($file, null, 'retnull');
var_dump($arch->isBroken());
?>

    
```

Resultado del ejemplo anterior es similar a:

    bool(true)

Estilo procedimental

```php
<?php
function retnull() { return null; }
$file = dirname(__FILE__) . "/multi_broken.part1.rar";
/* El tercer argumento es utilizado para omitir avisos */
$arch = rar_open($file, null, 'retnull');
var_dump(rar_broken_is($arch));
?>

    
```

## Véase también

RarArchive::setAllowBroken
