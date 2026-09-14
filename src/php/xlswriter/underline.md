---
title: Vtiful\Kernel\Format::underline
description: Vtiful\Kernel\Format underline
source_url: https://www.php.net/manual/es/vtiful-kernel-format.underline.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-format/underline.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 547a556ea
order: 102420
---

Vtiful\Kernel\Format::underline

Vtiful\Kernel\Format underline

## Descripción

```php
public Vtiful\Kernel\Format::underline(resource $handle, int $style)
```php

`Vtiful\Kernel\Format` formato subrayado

## Parámetros

`handle`  
manejador de archivos xlsx

`style`  
constante `Vtiful\Kernel\Format`

## Valores devueltos

Recurso

## Ejemplos

Ejemplo de estilo subrayado

```
<?php
$config = [
    'path' => './tests'
];

$excel = new \Vtiful\Kernel\Excel($config);
$excel->fileName('tutorial01.xlsx');

$format = new \Vtiful\Kernel\Format($excel->getHandle());
$underlineStyle = $format->underline(\Vtiful\Kernel\Format::UNDERLINE_SINGLE)->toResource();

$excel->header(['name', 'age'])
    ->data([['viest', 21]])
    ->setColumn('A:A', 200, $underlineStyle)
    ->output();
?>

   
```php
