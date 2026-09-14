---
title: RarArchive::close
description: Cerrar archivo RAR y liberar todos los recursos
source_url: https://www.php.net/manual/es/rararchive.close.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rar/rararchive/close.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rar
translation_status: ready
translation_reviewed: false
translation_revision: ee741f54f
order: 68400
---

RarArchive::close

rar_close

Cerrar archivo RAR y liberar todos los recursos

## Descripción

Estilo orientado a objetos (método):

```php
public RarArchive::close(): bool
```php

Estilo procedimental:

```php
rar_close(RarArchive $rarfile): bool
```

Cerar archivo RAR y liberar todos los recursos asignados.

## Parámetros

`rarfile`  
Un objeto `RarArchive`, abierto con `rar_open`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL rar 2.0.0 | Las entradas RAR devueltas por RarArchive::getEntry y RarArchive::getEntries son ahora invalidadas cuando se llama a este método. Esto significa que todos los métodos de instancia llamados por tales entradas y no garantizan el éxito. |

## Ejemplos

Estilo orientado a objetos

```php
<?php
$rar_arch = RarArchive::open('latest_winrar.rar');
echo $rar_arch."\n";
$rar_arch->close();
echo $rar_arch."\n";
?>

    
```

Resultado del ejemplo anterior es similar a:

    RAR Archive "D:\php_rar\trunk\tests\latest_winrar.rar"
    RAR Archive "D:\php_rar\trunk\tests\latest_winrar.rar" (closed)

Estilo procedimental

```php
<?php
$rar_arch = rar_open('latest_winrar.rar');
echo $rar_arch."\n";
rar_close($rar_arch);
echo $rar_arch."\n";
?>

    
```
