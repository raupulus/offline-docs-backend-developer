---
title: is_link
description: Indica si el fichero es un enlace simbólico
source_url: https://www.php.net/manual/es/function.is-link.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/is-link.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: d5f735c7b
order: 23770
---

is_link

Indica si el fichero es un enlace simbólico

## Descripción

```php
is_link(string $filename): bool
```php

Indica si el fichero es un enlace simbólico.

## Parámetros

`filename`  
Ruta de acceso al fichero.

## Valores devueltos

Devuelve `true` si el nombre de fichero existe y es un enlace simbólico, `false` en caso contrario.

## Errores/Excepciones

En caso de fallo, se emitirá una advertencia de tipo `E_WARNING`.

## Ejemplos

Creación y verificación de un enlace simbólico

```
<?php
$link = 'uploads';

if (is_link($link)) {
    echo readlink($link);
} else {
    symlink('uploads.php', $link);
}
?>

    
```php

## Notas

> [!NOTE]
> Los resultados de esta función se almacenan en caché. Véase la función `clearstatcache` para más detalles.

> [!TIP]
> A partir de PHP 5.0.0, esta función también puede ser utilizada con *algunos* protocolos url. Lea [???](#wrappers) para conocer los protocolos que soportan la familia de funcionalidades de `stat`.

## Véase también

`is_dir`, `is_file`, `readlink`, `symlink`
