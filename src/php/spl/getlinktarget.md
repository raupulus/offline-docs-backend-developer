---
title: SplFileInfo::getLinkTarget
description: Obtiene el destino de un enlace del sistema de ficheros
source_url: https://www.php.net/manual/es/splfileinfo.getlinktarget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getlinktarget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84100
---

SplFileInfo::getLinkTarget

Obtiene el destino de un enlace del sistema de ficheros

## Descripción

```php
public SplFileInfo::getLinkTarget(): string
```php

Obtiene el destino de un enlace del sistema de ficheros.

> [!NOTE]
> El destino no puede ser una ruta real en el sistema de ficheros. Use SplFileInfo::getRealPath para determinar la ruta verdadera en el sistema de fucheros.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el destino de el enlace del sistema de ficheros en caso de éxito, o `false` en caso de error.

## Errores/Excepciones

Lanza una `RuntimeException` en caso de error.

## Ejemplos

Ejemplo de `SplFileInfo::getLinkTarget`

```
<?php
$info = new SplFileInfo('/Users/bbieber/workspace');
if ($info->isLink()) {
    var_dump($info->getLinkTarget());
    var_dump($info->getRealPath());
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(19) "Documents/workspace"
    string(34) "/Users/bbieber/Documents/workspace"

## Véase también

SplFileInfo::isLink, SplFileInfo::getRealPath
