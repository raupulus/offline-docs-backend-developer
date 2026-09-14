---
title: pclose
description: Cierra un proceso de un puntero a un fichero
source_url: https://www.php.net/manual/es/function.pclose.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/pclose.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 1ad5dfe5e
order: 23920
---

pclose

Cierra un proceso de un puntero a un fichero

## Descripción

```php
pclose(resource $handle): int
```php

Cierra un puntero a un fichero hacia una tubería abierta por `popen`.

## Parámetros

`handle`  
El puntero al fichero debe ser válido, y debe haber sido devuelto por una llamada exitosa a `popen`.

## Valores devueltos

Devuelve el estado de terminación del proceso que se estaba ejecutando. En caso de error, se devuelve `-1`.

> [!NOTE]
> Si PHP ha sido compilado con la opción de configuración --enable-sigchild, el valor devuelto de esta función será indefinido.

## Ejemplos

Ejemplo de `pclose`

```
<?php
$gestor = popen('/bin/ls', 'r');
pclose($gestor);
?>

    
```php

## Notas

> [!NOTE]
> `pclose` está internamente implementada usando la llamada al sistema de `waitpid(3)`. Para obtener el código de estado de salida real debería usarse la función `pcntl_wexitstatus`.

## Véase también

`popen`
