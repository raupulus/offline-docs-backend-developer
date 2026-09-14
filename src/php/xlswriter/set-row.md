---
title: Vtiful\Kernel\Excel::setRow
description: Vtiful\Kernel\Excel setRow
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.setRow.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/set-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 8fc3f2a57
order: 102580
---

Vtiful\Kernel\Excel::setRow

Vtiful\Kernel\Excel setRow

## Descripción

```php
public Vtiful\Kernel\Excel::setRow(string $range, float $height, [resource $format])
```php

Establece el formato de la fila.

## Parámetros

`range`  
Las cadenas de coordenadas de inicio y fin de la celda

`height`  
altura de la fila

`format`  
recurso de formato de celdas

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

## Ejemplos

Ejemplo de setRow

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
    ->setRow('A1', 20, $boldStyle)
    ->output();

   
```php
