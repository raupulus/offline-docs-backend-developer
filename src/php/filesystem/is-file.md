---
title: is_file
description: Indica si el fichero es un fichero verdadero
source_url: https://www.php.net/manual/es/function.is-file.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-file.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 3d6879be7
order: 23760
---

is_file

Indica si el fichero es un fichero verdadero

## Descripción

```php
is_file(string $filename): bool
```php

Indica si el fichero es un fichero verdadero. Si `filename` es un enlace simbólico, se resolverá el enlace y se proporcionará información sobre el fichero referenciado.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve `true` si el nombre de fichero existe y es un fichero regular, `false` en caso contrario.

> [!NOTE]
> Como el tipo entero de PHP es firmado y que muchas plataformas utilizan enteros de 32 bits, algunas funciones relacionadas con el sistema de archivos pueden retornar resultados extraños para ficheros de tamaño superior a 2 Go.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Ejemplo con `is_file`

```
<?php
var_dump(is_file('a_file.txt')) . "\n";
var_dump(is_file('/usr/bin/')) . "\n";
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`is_dir`, `is_link`, `SplFileInfo`
