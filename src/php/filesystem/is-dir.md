---
title: is_dir
description: Indica si el fichero es un directorio
source_url: https://www.php.net/manual/es/function.is-dir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-dir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 871a231f4
order: 23740
---

is_dir

Indica si el fichero es un directorio

## Descripción

```php
is_dir(string $filename): bool
```php

Indica si el fichero es un directorio.

## Parámetros

`filename`  
Ruta de acceso al fichero. Si `filename` es un fichero relativo, será verificado relativamente al directorio de trabajo actual. Si `filename` es un enlace simbólico o un enlace convencional, el enlace será resuelto y verificado. Si se ha activado [open_basedir](#ini.open-basedir), pueden aplicarse más restricciones.

## Valores devueltos

Devuelve `true` si el nombre de fichero existe y es un directorio, `false` en caso contrario.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `is_dir`

```
<?php
var_dump(is_dir('a_file.txt'));
var_dump(is_dir('bogus_dir/abc'));

var_dump(is_dir('..')); // un directorio superior
?>

    
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(false)
    bool(true)

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`chdir`, `dir`, `opendir`, `is_file`, `is_link`
