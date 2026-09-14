---
title: SplFileObject::setFlags
description: Establece flags para el SplFileObject
source_url: https://www.php.net/manual/es/splfileobject.setflags.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/setflags.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84600
---

SplFileObject::setFlags

Establece flags para el SplFileObject

## Descripción

```php
public SplFileObject::setFlags(int $flags): void
```php

Establece las flags a ser usadas por el `SplFileObject`.

## Parámetros

`flags`  
Bitmask de las flags a establecer. Véase las [Constantes SplFileObject](#splfileobject.constants) para una lista de flags disponibles.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de SplFileObject::setFlags

```
<?php
$file = new SplFileObject("datos.csv");
$file->setFlags(SplFileObject::READ_CSV);
foreach ($file as $fields) {
    var_dump($fields);
}
?>

    
```php

## Véase también

SplFileObject::getFlags
