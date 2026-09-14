---
title: apcu_entry
description: Recupera o genera de forma atómica una entrada de caché
source_url: https://www.php.net/manual/es/function.apcu-entry.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/apcu/functions/apcu-entry.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: apcu
translation_status: ready
translation_revision: 804d8a054
order: 5040
---

apcu_entry

Recupera o genera de forma atómica una entrada de caché

## Descripción

```php
apcu_entry(string $key, callable $callback, [int $ttl]): mixed
```php

Intenta de forma atómica encontrar `key` en la caché; si no se encuentra, se llama a `callback`, pasando `key` como único argumento. El valor de retorno de la llamada se almacena en caché con el `ttl` especificado opcionalmente y se devuelve.

> [!NOTE]
> Cuando el control entra en `apcu_entry`, se adquiere de forma exclusiva el bloqueo de la caché, que se libera cuando el control sale de `apcu_entry`. En efecto, esto convierte el cuerpo de `callback` en una sección crítica, impidiendo que dos procesos ejecuten las mismas rutas de código concurrentemente. Además, prohíbe la ejecución concurrente de cualquier otra función de APCu, ya que adquirirán el mismo bloqueo.

> [!WARNING]
> La única función de APCu que puede llamarse de forma segura desde `callback` es `apcu_entry`.

## Parámetros

`key`  
Identificador de la entrada de caché

`callback`  
Una retrollamada que acepta `key` como único argumento y devuelve el valor a almacenar en caché.

`ttl`  
Tiempo de vida; almacena el valor de retorno del `callback` en la caché durante `ttl` segundos. Después de que `ttl` haya transcurrido, la entrada almacenada será eliminada de la caché (en la siguiente petición). Si no se proporciona `ttl` (o si el `ttl` es `0`), el valor persistirá hasta que se elimine manualmente de la caché, o deje de existir en la caché (limpieza, reinicio, etc.).

## Valores devueltos

Devuelve el valor almacenado en caché

## Ejemplos

Un ejemplo de `apcu_entry`

```
<?php
$config = apcu_entry("config", function($key) {
 return [
   "fruit" => apcu_entry("config.fruit", function($key){
     return [
       "apples",
       "pears"
     ];
   }),
   "people" => apcu_entry("config.people", function($key){
     return [
      "bob",
      "joe",
      "niki"
     ];
   })
 ];
});

var_dump($config);
?>

   
```php

El ejemplo anterior mostrará:

    array(2) {
      ["fruit"]=>
      array(2) {
        [0]=>
        string(6) "apples"
        [1]=>
        string(5) "pears"
      }
      ["people"]=>
      array(3) {
        [0]=>
        string(3) "bob"
        [1]=>
        string(3) "joe"
        [2]=>
        string(4) "niki"
      }
    }

## Véase también

apcu_store

apcu_fetch

apcu_delete
