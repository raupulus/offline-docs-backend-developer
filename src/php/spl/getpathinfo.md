---
title: SplFileInfo::getPathInfo
description: Obtiene un objeto SplFileInfo para la ruta
source_url: https://www.php.net/manual/es/splfileinfo.getpathinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/getpathinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84140
---

SplFileInfo::getPathInfo

Obtiene un objeto SplFileInfo para la ruta

## Descripción

```php
public SplFileInfo::getPathInfo([string $class]): SplFileInfo
```php

Obtiene un objeto `SplFileInfo` para el padre de el fichero actual.

## Parámetros

`class`  
Nombre de una clase `SplFileInfo` derivada a usar, o ella misma si `null`.

## Valores devueltos

Devuelve un objeto `SplFileInfo` para la ruta padre de el fichero en caso de éxito, o `false` en caso de error.

## Historial de cambios

| Versión | Descripción                |
|---------|----------------------------|
| 8.0.0   | `class` es ahora anulable. |

## Ejemplos

Ejemplo de `SplFileInfo::getPathInfo`

```
<?php
$info = new SplFileInfo('/usr/bin/php');
$parent_info = $info->getPathInfo();
var_dump($parent_info->getRealPath());
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(8) "/usr/bin"

## Véase también

SplFileInfo::setInfoClass
