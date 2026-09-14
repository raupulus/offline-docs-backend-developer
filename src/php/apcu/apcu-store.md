---
title: apcu_store
description: Almacena una variable en la caché de datos
source_url: https://www.php.net/manual/es/function.apcu-store.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-store.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 5100
---

apcu_store

Almacena una variable en la caché de datos

## Descripción

```php
apcu_store(string $key, mixed $var, [int $ttl]): bool
```php

```php
apcu_store(array $values, [mixed $unused], [int $ttl]): array
```

Almacena una variable en la caché de datos.

> [!NOTE]
> A diferencia de muchos otros mecanismos en PHP, las variables almacenadas utilizando `apcu_store` persistirán entre las peticiones (hasta que sus valores sean retirados de la caché).

## Parámetros

`key`  
Almacena la variable utilizando este nombre de clave. Cada clave es única en la caché, almacenar un segundo valor con el mismo parámetro `key` sobrescribirá el valor original.

`var`  
La variable a almacenar.

`ttl`  
Duración de vida; almacena la variable `var` en la caché durante un tiempo de `ttl` segundos. Después de la expiración de `ttl`, la variable almacenada será retirada de la caché (en la próxima petición). Si no se pasa ningún valor al parámetro `ttl` (o si el valor de `ttl` es `0`), la variable persistirá hasta que sea retirada manualmente de la caché, o, de lo contrario, fallará al salir de la caché (durante un borrado, reinicio, etc.).

`values`  
Los nombres son proporcionados por las claves del array `values`, las variables por los valores.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. La segunda sintaxis devuelve un array con las claves erróneas.

## Ejemplos

Un ejemplo con `apcu_store`

```php
<?php
$bar = 'BAR';
apcu_store('foo', $bar);
var_dump(apcu_fetch('foo'));
?>

   
```

El ejemplo anterior mostrará:

    string(3) "BAR"

## Véase también

apcu_add

apcu_fetch

apcu_delete
