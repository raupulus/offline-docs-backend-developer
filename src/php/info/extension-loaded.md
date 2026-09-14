---
title: extension_loaded
description: Determina si una extensión está cargada o no
source_url: https://www.php.net/manual/es/function.extension-loaded.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/extension-loaded.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: c44475e1f
order: 38770
---

extension_loaded

Determina si una extensión está cargada o no

## Descripción

```php
extension_loaded(string $extension): bool
```php

Determina si una extensión está cargada o no.

## Parámetros

`extension`  
El nombre de la extensión. Este argumento no es sensible a mayúsculas/minúsculas.

Los nombres de las diferentes extensiones PHP pueden ser conocidos utilizando la función `phpinfo` o bien si se utiliza la versión `CGI` o `CLI` de PHP, se puede utilizar la opción de línea de comandos `-m` para mostrar todas las extensiones disponibles :

    $ php -m
    [PHP Modules]
    xml
    tokenizer
    standard
    sockets
    session
    posix
    pcre
    overload
    mysql
    mbstring
    ctype

    [Zend Modules]

           

## Valores devueltos

Retorna `true` si la extensión `extension` ha sido cargada, `false` en caso contrario.

## Ejemplos

Ejemplo con `extension_loaded`

```
<?php
if (!extension_loaded('gd')) {
    if (!dl('gd.so')) {
        exit;
    }
}
?>

    
```php

## Véase también

`get_loaded_extensions`, `get_extension_funcs`, `phpinfo`, `dl`, `function_exists`
