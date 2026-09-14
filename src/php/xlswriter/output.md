---
title: Vtiful\Kernel\Excel::output
description: Vtiful\Kernel\Excel output
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.output.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/output.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102560
---

Vtiful\Kernel\Excel::output

Vtiful\Kernel\Excel output

## Descripción

```php
public Vtiful\Kernel\Excel::output()
```php

Salida del archivo xlsx al disco.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Ruta de archivo XLSX;

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

$path = $file->output();
?>

   
```php
