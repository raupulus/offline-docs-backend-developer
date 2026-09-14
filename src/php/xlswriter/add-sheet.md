---
title: Vtiful\Kernel\Excel::addSheet
description: Vtiful\Kernel\Excel addSheet
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.addSheet.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/add-sheet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102440
---

Vtiful\Kernel\Excel::addSheet

Vtiful\Kernel\Excel addSheet

## Descripción

```php
public Vtiful\Kernel\Excel::addSheet(string $sheetName)
```php

Crea una nueva hoja de trabajo en el archivo xlsx.

## Parámetros

`sheetName`  
Nombre de la hoja de trabajo

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

$file = $fileObject->fileName('tutorial.xlsx', 'sheet_one')
    ->header(['name', 'age'])
    ->data([
        ['viest', 23],
        ['wjx', 23]
    ]);

$file->addSheet('sheet_two')
    ->header(['name', 'age'])
    ->data([
        ['james', 33],
        ['king', 33]
    ]);

$file->output();
?>

   
```php
