---
title: La clase WeakReference
source_url: https://www.php.net/manual/es/class.weakreference.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/weakreference.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: 911fe79de
order: 4360
---

## Introducción

Las referencias débiles permiten al programador mantener una referencia a un objeto sin impedir su destrucción. Son útiles para implementar estructuras como cachés. Si el objeto original ha sido destruido, `null` será devuelto al llamar al método WeakReference::get. El objeto original será destruido cuando el [contador de referencias](#features.gc.refcounting-basics) llegue a cero; la creación de referencias débiles no incrementa el `contador de referencias` del objeto referenciado.

Las `WeakReference`s no pueden ser serializadas.

## Sinopsis de la clase

final

WeakReference

Métodos

## Ejemplo con WeakReference

Uso Simple de WeakReference

```php
<?php

$obj = new stdClass();
$weakref = WeakReference::create($obj);

var_dump($weakref->get());

unset($obj);

var_dump($weakref->get());

?>

     
```

Resultado del ejemplo anterior es similar a:

    object(stdClass)#1 (0) {
    }
    NULL

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | La salida de WeakReference::\_\_debugInfo incluye ahora el objeto referenciado, o `null` si la referencia ya no es válida. |
