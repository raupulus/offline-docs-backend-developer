---
title: Exception::getPrevious
description: Devuelve la Throwable anterior
source_url: https://www.php.net/manual/es/exception.getprevious.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/exception/getprevious.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_revision: 09c49da6f
order: 3350
---

Exception::getPrevious

Devuelve la Throwable anterior

## Descripción

```php
final public Exception::getPrevious(): Throwable
```php

Devuelve la `Throwable` anterior (el tercer parámetro de Exception::\_\_construct).

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la `Throwable` anterior si está disponible o `null` si no.

## Ejemplos

Ejemplo de Exception::getPrevious

Recorrer, e imprimir la traza de una excepción.

```
<?php
class MiPropiaExcepción extends Exception {}

function hacerCosas() {
    try {
        throw new InvalidArgumentException("¡Lo está haciendo mal!", 112);
    } catch(Exception $e) {
        throw new MiPropiaExcepción("Ocurrió algo", 911, $e);
    }
}

try {
    hacerCosas();
} catch(Exception $e) {
    do {
        printf("%s:%d %s (%d) [%s]\n", $e->getFile(), $e->getLine(), $e->getMessage(), $e->getCode(), get_class($e));
    } while($e = $e->getPrevious());
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    /home/bjori/ex.php:8 Ocurrió algo (911) [MiPropiaExcepción]
    /home/bjori/ex.php:6 ¡Lo está haciendo mal! (112) [InvalidArgumentException]

## Véase también

Throwable::getPrevious
