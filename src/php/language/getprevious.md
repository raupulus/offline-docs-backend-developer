---
title: Error::getPrevious
description: Devuelve el objeto Throwable anterior
source_url: https://www.php.net/manual/es/error.getprevious.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/error/getprevious.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: e565d17dc
order: 3210
---

Error::getPrevious

Devuelve el objeto Throwable anterior

## Descripción

```php
final public Error::getPrevious(): Throwable
```php

Devuelve el objeto Throwable anterior (el tercer parámetro de Error::\_\_construct).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el objeto `Throwable` anterior si está disponible, o `null` en caso contrario.

## Ejemplos

Ejemplo de Error::getPrevious

Recorrer e imprimir la traza de errores.

```
<?php
class MiErrorPersonalizado extends Error {}

function hacerCosas() {
    try {
        throw new TypeError("¡Lo está haciendo mal!", 112);
    } catch(Error $e) {
        throw new MiErrorPersonalizado("Ocurrió algo", 911, $e);
    }
}

try {
    hacerCosas();
} catch(Error $e) {
    do {
        printf("%s:%d %s (%d) [%s]\n", $e->getFile(), $e->getLine(), $e->getMessage(), $e->getCode(), get_class($e));
    } while($e = $e->getPrevious());
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    /home/bjori/ex.php:8 Ocurrió algo (911) [MiErrorPersonalizado]
    /home/bjori/ex.php:6 ¡Lo está haciendo mal! (112) [TypeError]

## Véase también

Throwable::getPrevious
