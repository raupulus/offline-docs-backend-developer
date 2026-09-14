---
title: Vtiful\Kernel\Format::italic
description: Vtiful\Kernel\Format italic
source_url: https://www.php.net/manual/es/vtiful-kernel-format.italic.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-format/italic.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 547a556ea
order: 102410
---

Vtiful\Kernel\Format::italic

Vtiful\Kernel\Format italic

## Descripción

```php
public Vtiful\Kernel\Format::italic(resource $handle)
```php

`Vtiful\Kernel\Format` formato cursivo

## Parámetros

`handle`  
manejador de archivos xlsx

## Valores devueltos

Recurso

## Ejemplos

Ejemplo de estilo cursiva

```
<?php
$config = [
    'path' => './tests'
];

$excel = new \Vtiful\Kernel\Excel($config);
$excel->fileName('tutorial01.xlsx');

$format = new \Vtiful\Kernel\Format($excel->getHandle());
$italicStyle = $format->italic()->toResource();

$excel->header(['name', 'age'])
    ->data([['viest', 21]])
    ->setColumn('A:A', 200, $italicStyle)
    ->output();
?>

   
```php
