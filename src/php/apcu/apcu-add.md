---
title: apcu_add
description: Almacena en caché una nueva variable en el almacén de datos
source_url: https://www.php.net/manual/es/function.apcu-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 4970
---

apcu_add

Almacena en caché una nueva variable en el almacén de datos

## Descripción

```php
apcu_add(string $key, mixed $var, [int $ttl]): bool
```php

```php
apcu_add(array $values, [mixed $unused], [int $ttl]): array
```

Almacena en caché una variable en el almacén de datos, solo si no ha sido ya almacenada.

> [!NOTE]
> A diferencia de muchos otros mecanismos en PHP, las variables almacenadas utilizando `apcu_add` persistirán entre las peticiones (hasta que sus valores sean retirados del caché).

## Parámetros

`key`  
Almacena la variable utilizando este nombre de clave. Cada clave es única en el caché, intentar utilizar `apcu_add` para almacenar un dato con una clave `key` ya existente no sobrescribirá el dato sino que devolverá el valor `false`. (Esta es la única diferencia entre las funciones `apcu_add` y `apcu_store`.)

`var`  
La variable a almacenar.

`ttl`  
Duración de vida; almacena la variable `var` en el caché durante `ttl` segundos. Después de la expiración de `ttl`, la variable almacenada será retirada del caché (en la próxima petición). Si no se pasa ningún valor a `ttl` (o si el valor de `ttl` es `0`), la variable persistirá hasta que sea retirada manualmente del caché, o, de lo contrario, fallará al salir del caché (durante un borrado, reinicio, etc.).

`values`  
Los nombres son proporcionados por las claves del array values, las variables por los valores.

## Valores devueltos

Devuelve TRUE si una variable ha sido efectivamente añadida al caché, FALSE en caso contrario. La segunda sintaxis devuelve un array con las claves erróneas.

## Ejemplos

Un ejemplo con `apcu_add`

```php
<?php
$bar = 'BAR';
apcu_add('foo', $bar);
var_dump(apcu_fetch('foo'));
echo "\n";
$bar = 'NEVER GETS SET';
apcu_add('foo', $bar);
var_dump(apcu_fetch('foo'));
echo "\n";
?>

   
```

El ejemplo anterior mostrará:

    string(3) "BAR"
    string(3) "BAR"

## Véase también

apcu_store

apcu_fetch

apcu_delete
