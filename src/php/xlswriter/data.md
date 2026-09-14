---
title: Vtiful\Kernel\Excel::data
description: Vtiful\Kernel\Excel data
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.data.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/data.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102480
---

Vtiful\Kernel\Excel::data

Vtiful\Kernel\Excel data

## Descripción

```php
public Vtiful\Kernel\Excel::data(array $data)
```php

Escribe un dato en la hoja de trabajo.

## Parámetros

`data`  
datos de la hoja de trabajo

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
      ['wjx', 23],
    ]);
?>

   
```php
