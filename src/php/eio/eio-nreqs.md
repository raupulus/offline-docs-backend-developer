---
title: eio_nreqs
description: Devuelve el número de peticiones a ser procesadas
source_url: https://www.php.net/manual/es/function.eio-nreqs.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-nreqs.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16990
---

eio_nreqs

Devuelve el número de peticiones a ser procesadas

## Descripción

```php
eio_nreqs(): int
```php

`eio_nreqs` se podría llamar en un bucle personalizado al llamar a `eio_poll`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

`eio_nreqs` devuelve el número de peticiones a ser procesadas.

## Ejemplos

Ejepmlo de `eio_nreqs`

```
<?php
function res_cb($datos, $resultado) {
    var_dump($datos);
    var_dump($resultado);
}

eio_nop(EIO_PRI_DEFAULT, "res_cb", "1");
eio_nop(EIO_PRI_DEFAULT, "res_cb", "2");
eio_nop(EIO_PRI_DEFAULT, "res_cb", "3");

while (eio_nreqs()) {
    eio_poll();
}
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(1) "1"
    int(0)
    string(1) "3"
    int(0)
    string(1) "2"
    int(0)

## Véase también

eio_poll

eio_nready
