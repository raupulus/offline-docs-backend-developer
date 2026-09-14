---
title: eio_poll
description: Puede ser llamada siempre que existan peticiones pendientes que necesitan
  ser finalizadas
source_url: https://www.php.net/manual/es/function.eio-poll.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-poll.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: dfd68fd22
order: 17020
---

eio_poll

Puede ser llamada siempre que existan peticiones pendientes que necesitan ser finalizadas

## Descripción

```php
eio_poll(): int
```php

`eio_poll` se puede usar para implementar un bucle de eventos especial. Para esto, podria usarse `eio_nreqs` para comprobar si existen peticiones no procesadas.

> [!NOTE]
> Aplicable solamente al implementar bucles de eventos del espacio de usuario.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Si cualquier invocación a una petición devuelve un valor distinto de cero, devuelve ese valor. De otro modo devuelve `0`.

## Ejemplos

Ejemplo de `eio_poll`

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
    // Algún IPC específico más o menos
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

eio_nreqs
