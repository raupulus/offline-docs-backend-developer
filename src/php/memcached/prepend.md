---
title: Memcached::prepend
description: Prefijo de datos a un elemento existente
source_url: https://www.php.net/manual/es/memcached.prepend.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/prepend.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46700
---

Memcached::prepend

Prefijo de datos a un elemento existente

## Descripción

```php
public Memcached::prepend(string $key, string $value): bool
```php

`Memcached::prepend` añade los datos de `value` al principio de un elemento existente. La razón por la que `value` debe ser un string es que los otros tipos no soportan esta operación.

> [!NOTE]
> Si la constante `Memcached::OPT_COMPRESSION` está activada, la operación fallará y se emitirá una advertencia, ya que no es posible prependear datos comprimidos.

## Parámetros

`key`  
La clave del elemento a prependear.

`value`  
El string a prependear.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Devuelve `null` si la compresión está activada.

## Errores/Excepciones

Devuelve `null` y genera un `E_WARNING` si la compresión está activada.

## Ejemplos

Ejemplo con `Memcached::prepend`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);
$m->setOption(Memcached::OPT_COMPRESSION, false);

$m->set('foo', 'abc');
$m->prepend('foo', 'def');
var_dump($m->get('foo'));
?>

    
```php

El ejemplo anterior mostrará:

    string(6) "defabc"

## Véase también

Memcached::prependByKey, Memcached::append
