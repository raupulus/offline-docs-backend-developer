---
title: SplFileInfo::getType
description: Obtiene el tipo del fichero
source_url: https://www.php.net/manual/es/splfileinfo.gettype.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/gettype.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84190
---

SplFileInfo::getType

Obtiene el tipo del fichero

## Descripción

```php
public SplFileInfo::getType(): string
```php

Devuelve el tipo de el fichero referenciado.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Un `string` representando el tipo de la entrada. Puede ser `file`, `link`, `dir`, `block`, `fifo`, `char`, `socket`, o `unknown`, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` en caso de error.

## Ejemplos

Ejemplo de `SplFileInfo::getType`

```
<?php

$info = new SplFileInfo(__FILE__);
echo $info->getType().PHP_EOL;

$info = new SplFileInfo(dirname(__FILE__));
echo $info->getType();

?>

    
```php

Resultado del ejemplo anterior es similar a:

    file
    dir
