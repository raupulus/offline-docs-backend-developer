---
title: Vtiful\Kernel\Excel::insertFormula
description: Vtiful\Kernel\Excel insertFormula
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.insertFormula.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/insert-formula.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: '469121548'
order: 102520
---

Vtiful\Kernel\Excel::insertFormula

Vtiful\Kernel\Excel insertFormula

## Descripción

```php
public Vtiful\Kernel\Excel::insertFormula(int $row, int $column, string $formula)
```php

Inserta la fórmula de cálculo.

## Parámetros

`row`  
fila de celdas

`column`  
columna de celdas

`formula`  
Cadena de fórmula

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

for($index = 1; $index < 10; $index++) {
    $file->insertText($index, 0, 'viest');
    $file->insertText($index, 1, 10);
}

$file->insertText(12, 0, "Total");
$file->insertFormula(12, 1, '=SUM(B2:B11)'); // insertar la fórmula

$file->output();

   
```php
