---
title: Vtiful\Kernel\Format::bold
description: Vtiful\Kernel\Format bold
source_url: https://www.php.net/manual/es/vtiful-kernel-format.bold.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-format/bold.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 547a556ea
order: 102400
---

Vtiful\Kernel\Format::bold

Vtiful\Kernel\Format bold

## Descripción

```php
public Vtiful\Kernel\Format::bold(resource $handle)
```php

`Vtiful\Kernel\Format` formato en negrita

## Parámetros

`handle`  
manejador de archivos xlsx

## Valores devueltos

Recurso

## Ejemplos

Ejemplo de estilo negrita

```
<?php
$config = [
    'path' => './tests'
];

$excel = new \Vtiful\Kernel\Excel($config);
$excel->fileName('tutorial01.xlsx');

$format = new \Vtiful\Kernel\Format($excel->getHandle());
$boldStyle = $format->bold()->toResource();

$excel->header(['name', 'age'])
    ->data([['viest', 21]])
    ->setColumn('A:A', 200, $boldStyle)
    ->output();
?>

   
```php
