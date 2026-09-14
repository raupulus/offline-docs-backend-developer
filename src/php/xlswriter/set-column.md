---
title: Vtiful\Kernel\Excel::setColumn
description: Vtiful\Kernel\Excel setColumn
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.setColumn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/set-column.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 547a556ea
order: 102570
---

Vtiful\Kernel\Excel::setColumn

Vtiful\Kernel\Excel setColumn

## Descripción

```php
public Vtiful\Kernel\Excel::setColumn(string $range, float $width, [resource $format])
```php

Establece el formato de la columna.

## Parámetros

`range`  
Las cadenas de coordenadas de inicio y fin de la celda

`width`  
ancho de la columna

`format`  
recurso de formato de celdas

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

## Ejemplos

Ejemplo de setColumn

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

   
```php
