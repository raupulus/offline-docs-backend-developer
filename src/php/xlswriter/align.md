---
title: Vtiful\Kernel\Format::align
description: Vtiful\Kernel\Format align
source_url: https://www.php.net/manual/es/vtiful-kernel-format.align.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-format/align.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 547a556ea
order: 102390
---

Vtiful\Kernel\Format::align

Vtiful\Kernel\Format align

## Descripción

```php
public Vtiful\Kernel\Format::align(resource $handle, int $style)
```php

establece la alineación de la celda

## Parámetros

`handle`  
manejador de archivos xlsx

`style`  
constante `Vtiful\Kernel\Format`

## Valores devueltos

Recurso

## Ejemplos

Ejemplo de estilo de alineación

```
<?php
$config = [
    'path' => './tests'
];

$excel = new \Vtiful\Kernel\Excel($config);
$excel->fileName('tutorial01.xlsx');

$format = new \Vtiful\Kernel\Format($excel->getHandle());
$alignStyle = $format->align(\Vtiful\Kernel\Format::FORMAT_ALIGN_LEFT)->toResource();

$excel->header(['name', 'age'])
    ->data([['viest', 21]])
    ->setColumn('A:A', 200, $alignStyle)
    ->output();
?>

   
```php
