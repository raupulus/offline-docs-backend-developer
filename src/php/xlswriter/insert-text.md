---
title: Vtiful\Kernel\Excel::insertText
description: Vtiful\Kernel\Excel insertText
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.insertText.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/insert-text.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: 8e2cfbdce
order: 102540
---

Vtiful\Kernel\Excel::insertText

Vtiful\Kernel\Excel insertText

## Descripción

```php
public Vtiful\Kernel\Excel::insertText(int $row, int $column, int $data, [string $format])
```php

Escribe texto en una celda.

## Parámetros

`row`  
fila de celdas

`column`  
columna de celdas

`data`  
los datos que se escribirán

`format`  
Cadena de formato

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

$file = $excel->fileName("free.xlsx")
    ->header(['name', 'money']);

for ($index = 0; $index < 10; $index++) {
    $file->insertText($index+1, 0, 'viest');
    $file->insertText($index+1, 1, 10000, '#,##0');
}

$file->output();

   
```php
