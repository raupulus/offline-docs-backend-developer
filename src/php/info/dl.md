---
title: dl
description: Carga una extensión PHP dinámicamente
source_url: https://www.php.net/manual/es/function.dl.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/info/functions/dl.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: info
translation_status: ready
translation_reviewed: true
translation_revision: a89c6d71c
order: 38760
---

dl

Carga una extensión PHP dinámicamente

## Descripción

```php
dl(string $extension_filename): bool
```php

Carga la extensión PHP `extension_filename` dinámicamente.

Utilice la función `extension_loaded` para verificar si una extensión está cargada o no. Esta función funciona tanto con extensiones nativas como con extensiones cargadas dinámicamente (vía el `php.ini` o `dl`).

> [!WARNING]
> Esta función solo está disponible para los SAPI CLI e integrados, y el SAPI CGI cuando se ejecuta desde la línea de comandos.

## Parámetros

`extension_filename`  
Este parámetro es *solo* el nombre de archivo de la extensión, que depende de la plataforma. Por ejemplo la extensión [sockets](#ref.sockets) (si compilada como módulo compartido, y no por defecto), se llamará `sockets.so` bajo Unix, y `php_sockets.dll` bajo Windows.

La carpeta desde la cual se cargan las extensiones depende de la plataforma:

Windows - Si no se indica explícitamente en el archivo `php.ini`, la extensión se carga desde `C:\php5\` por defecto.

Unix - Si no se indica explícitamente en el archivo `php.ini`, la carpeta de extensiones depende de

- Si PHP fue compilado con la opción `--enable-debug` o no

- Si PHP fue compilado con soporte para ZTS (`Zend Thread Safety`) o no

- de la constante interna `ZEND_MODULE_API_NO` (versión interna de API de módulo Zend, que en realidad es la fecha en que se realizó una modificación importante de la API, por ejemplo `20010901`)

Considerando estos parámetros, la carpeta de extensiones será entonces `<install-dir>/lib/php/extensions/ <debug-or-not>-<zts-or-not>-ZEND_MODULE_API_NO`, por ejemplo `/usr/local/php/lib/php/extensions/debug-non-zts-20010901` o `/usr/local/php/lib/php/extensions/no-debug-zts-20010901`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Si la funcionalidad de carga de módulos no está disponible, o ha sido desactivada (desactivando la directiva [enable_dl](#ini.enable-dl) en el `php.ini`) se emitirá un `E_ERROR` y la ejecución del script será detenida. Si la función `dl` falla porque la biblioteca no pudo ser encontrada, `dl` retornará `false` y emitirá un mensaje de advertencia `E_WARNING`.

## Ejemplos

Ejemplos con `dl`

```
<?php
// Carga para todas las plataformas
if (!extension_loaded('sqlite')) {
    if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
        dl('php_sqlite.dll');
    } else {
        dl('sqlite.so');
    }
}

// O usar la constante PHP_SHLIB_SUFFIX
if (!extension_loaded('sqlite')) {
    $prefix = (PHP_SHLIB_SUFFIX === 'dll') ? 'php_' : '';
    dl($prefix . 'sqlite.' . PHP_SHLIB_SUFFIX);
}
?>

    
```php

## Notas

> [!NOTE]
> `dl` es sensible a mayúsculas/minúsculas en plataformas Unix.

## Véase también

[Directivas de carga de extensiones](#ini.extension), `extension_loaded`
