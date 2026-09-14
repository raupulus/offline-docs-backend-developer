---
title: eio_cancel
description: Cancelar una petición
source_url: https://www.php.net/manual/es/function.eio-cancel.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-cancel.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 16690
---

eio_cancel

Cancelar una petición

## Descripción

```php
eio_cancel(resource $req): void
```php

`eio_cancel` cancela una petición especificada por `req`

## Parámetros

`req`  
El recurso de petición

`pri`  
La prioridad de la petición: `EIO_PRI_DEFAULT`, `EIO_PRI_MIN`, `EIO_PRI_MAX`, o `null`. Si `null` es pasado, el parámetro `pri`, internamente, es definido a `EIO_PRI_DEFAULT`.

`callback`  
La función de retrollamada `callback` es llamada cuando la petición está terminada. Debe corresponder al siguiente prototipo:

```
void callback(mixed $data, int $result[, resource $req]);
```php

`data`  
representa los datos personalizados pasados a la petición.

`result`  
representa el valor resultante específico de la petición; básicamente, el valor retornado por la llamada al sistema correspondiente.

`req`  
es el recurso opcional de la petición que puede ser utilizado con funciones como `eio_get_last_error`.

`data`  
Variable arbitraria pasada a `callback`.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de `eio_cancel`

```
<?php
 /* Es llamada cuando eio_nop() finaliza */
 function mi_llamada_retorno_nop($datos, $resultado) {
  echo "mi_nop ", $datos, "\n";
 }

// Esta llamada a eio_nop() será cancelada
$petición = eio_nop(EIO_PRI_DEFAULT, "mi_llamada_retorno_nop", "1");
var_dump($petición);
eio_cancel($petición);

// Esta vez eio_nop() será procesada
eio_nop(EIO_PRI_DEFAULT, "mi_llamada_retorno_nop", "2");

// Procesar las peticiones
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    resource(4) of type (EIO Request Descriptor)
    mi_nop 2

## Véase también

eio_grp_cancel
