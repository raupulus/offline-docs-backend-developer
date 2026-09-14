---
title: SplFileInfo::__construct
description: Construir un objeto nuevo SplFileInfo
source_url: https://www.php.net/manual/es/splfileinfo.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 84010
---

SplFileInfo::\_\_construct

Construir un objeto nuevo SplFileInfo

## Descripción

```php
public SplFileInfo::__construct(string $filename)
```php

Crea un nuevo objeto para el SplFileInfo nombre_archivo especificado. El fichero no tiene por qué existir, o ser de lectura.

## Parámetros

`filename`  
Ruta del fichero.

## Ejemplos

`SplFileInfo::__construct` ejemplo

```
<?php
$info = new SplFileInfo('example.php');
if ($info->isFile()) {
    echo $info->getRealPath();
}
?>

    
```php
