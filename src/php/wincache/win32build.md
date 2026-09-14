---
title: Compilación en Windows
source_url: https://www.php.net/manual/es/wincache.win32build.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/win32build.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: 8b6d16942
order: 101840
---

## Compilación en Windows

## Prerrequisitos

Para compilar la extensión WinCache, se necesitará:

1.  el código fuente de PHP
2.  un entorno de compilación PHP
3.  el código fuente de WinCache

Para completar los dos primeros pasos, siga la guía paso a paso [Compilar PHP en Windows](https://wiki.php.net/internals/windows/stepbystepbuild).

Para obtener el código fuente de WinCache, siga las instrucciones descritas en [Descargar extensiones PECL](#install.pecl.downloads).

## Compilar y construir

Los siguientes pasos describen cómo compilar y construir WinCache en Windows:

1.  Abra una ventana de comandos utilizada para compilar PHP

2.  Vaya al directorio raíz donde se encuentran las fuentes de PHP

3.  Ejecute el comando:

```php
    cscript.exe win32\build\buildconf.js

          
    ```

4.  Ejecute el comando:

```php
    configure.bat --help

          
    ```

    La salida contendrá una nueva opción `--enable-wincache`.

5.  Ejecute el comando:

```php
    configure.js [todas las opciones usadas para compilar PHP] --enable-wincache

          
    ```

    `--enable-wincache` es la única opción adicional requerida para asegurarse de que la extensión WinCache se compile correctamente. Esta opción permite construir WinCache y enlazarlo estáticamente con la DLL de PHP. Para construir la extensión como una DLL externa, use la opción `--enable-wincache=shared`.

6.  Ejecute el comando:

```php
    nmake

          
    ```

## Verificar la compilación

Los siguientes pasos describen cómo verificar que WinCache se ha compilado correctamente:

1.  Vaya al directorio donde se construyen los archivos PHP.

2.  Ejecute el comando:

```php
    php.exe -n -d extension=php_wincache.dll -re wincache

          
    ```

    Si WinCache se ha compilado correctamente, la salida de este comando listará las directivas INI y las funciones soportadas por WinCache.
