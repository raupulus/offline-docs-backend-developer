---
title: Vtiful\Kernel\Excel::autoFilter
description: Vtiful\Kernel\Excel autoFilter
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.autoFilter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/auto-filter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 102450
---

Vtiful\Kernel\Excel::autoFilter

Vtiful\Kernel\Excel autoFilter

## Descripción

```php
public Vtiful\Kernel\Excel::autoFilter(string $scope)
```php

Añade el autofiltro a una hoja de trabajo.

## Parámetros

`scope`  
Celda de inicio y final de la cadena de coordenadas.

## Valores devueltos

instancia `Vtiful\Kernel\Excel`

## Ejemplos

ejemplo

```
<?php
$config = [
    'path' => './tests'
];

$fileObject  = new \Vtiful\Kernel\Excel($config);

$file = $fileObject->fileName('test.xlsx')
        ->header(['name', 'age'])
        ->data($data)
        ->autoFilter('A1:B11')  // auto filter
        ->output();
?>

   
```php
