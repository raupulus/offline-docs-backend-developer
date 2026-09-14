---
title: Vtiful\Kernel\Excel::__construct
description: Vtiful\Kernel\Excel constructor
source_url: https://www.php.net/manual/es/vtiful-kernel-excel.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xlswriter/xlsx-kernel/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xlswriter
translation_status: ready
translation_reviewed: false
translation_revision: c44e9cb68
order: 102470
---

Vtiful\Kernel\Excel::\_\_construct

Vtiful\Kernel\Excel constructor

## Descripción

```php
public Vtiful\Kernel\Excel::__construct(array $config)
```php

`Vtiful\Kernel\Excel` constructor, crea un objeto de clase.

## Parámetros

`config`  
Configuración de la exportación de archivos XLSX

## Ejemplos

ejemplo

```
<?php
$config = [
  'path' => '/home/viest'
];

$excelObject = new \Vtiful\Kernel\Excel($config);
?>

   
```php
