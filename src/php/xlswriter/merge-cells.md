---
title: Vtiful\Kernel\Excel::mergeCells
description: Vtiful\Kernel\Excel mergeCells
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.mergeCells.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/merge-cells.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102550
---

Vtiful\Kernel\Excel::mergeCells

Vtiful\Kernel\Excel mergeCells

## Descripción

```php
public Vtiful\Kernel\Excel::mergeCells(string $scope, string $data)
```php

Combinar Celdas.

## Parámetros

`scope`  
Cadenas de coordenadas de inicio y fin de la celda

`data`  
Cadena de datos

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

## Ejemplos

ejemplo

```
<?php
$config = [
    'path' => './tests'
];

$excel = new \Vtiful\Kernel\Excel($config);

$excel->fileName("test.xlsx")
        ->mergeCells('A1:C1', 'Merge cells')
        ->output();

   
```php
