---
title: socket_select
description: Ejecuta la llamada al sistema select() sobre un array de sockets con
  un tiempo de expiración
source_url: https://www.php.net/manual/es/function.socket-select.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/sockets/functions/socket-select.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: sockets
translation_status: ready
translation_reviewed: true
translation_revision: 14dc7c473
order: 75780
---

socket_select

Ejecuta la llamada al sistema select() sobre un array de sockets con un tiempo de expiración

## Descripción

```php
socket_select(array $read, array $write, array $except, int $seconds, [int $microseconds]): int
```php

`socket_select` acepta un array de sockets y espera a que cambien de estado. Quienes estén familiarizados con los sockets de BSD reconocerán en estos arrays de sockets los juegos de punteros a ficheros. Tres arrays independientes de sockets son monitorizados.

## Parámetros

`read`  
Los sockets listados en el argumento `read` serán monitorizados en lectura: para saber cuándo están disponibles para lectura (más precisamente, si una lectura no va a bloquear, en particular, un socket ya ha alcanzado un fin de archivo, en cuyo caso `socket_read` devolverá una string de tamaño cero).

`write`  
Los sockets listados en `write` serán monitorizados en escritura: para ver si una escritura no va a bloquear.

`except`  
Los sockets listados en `except` serán monitorizados para sus excepciones.

`seconds`  
Los argumentos `seconds` y `microseconds` juntos forman el argumento `timeout` (duración). El `timeout` es la duración máxima de tiempo antes de que `socket_select` termine. `seconds` puede ser cero, lo que hará que `socket_select` devuelva inmediatamente. Esto es muy útil para hacer polling (sondaje). Si `seconds` es `null` (sin timeout), `socket_select` puede bloquearse indefinidamente.

`microseconds`  

> [!WARNING]
> Al salir de la función, los arrays son modificados para indicar qué sockets han cambiado de estado.

No es necesario pasar todos los arrays a `socket_select`. Pueden ser omitidos, o puede usarse un array vacío, o incluso `null` en su lugar. No olvide que estos arrays son pasados por *referencia* y serán modificados por `socket_select`.

> [!NOTE]
> Debido a una limitación del motor Zend actual, no es posible pasar una constante como `null` directamente como argumento a esta función, que espera una referencia. En su lugar, utilice un array temporal o una expresión donde el miembro izquierdo sea una variable temporal:
>
> <div class="example">
>
> <div class="title">
>
> Pasar `null` a `socket_select`
>
> </div>
>
> ```
> <?php
> $e = NULL;
> socket_select($r, $w, $e, 0);
> ?>
>
>      
> ```
>
> </div>

## Valores devueltos

En caso de éxito, `socket_select` devuelve el número de sockets contenidas en los arrays modificados. Este número puede ser cero si se alcanzó el tiempo máximo de espera. En caso de error, `false` es devuelto. El código de error generado puede ser obtenido llamando a la función `socket_last_error`.

> [!NOTE]
> Asegúrese de usar el operador `===` cuando verifique los errores. Dado que `socket_select` puede devolver 0, la comparación con `false` mediante `==` daría `true`:
>
> <div class="example">
>
> <div class="title">
>
> Analizar el resultado de `socket_select`
>
> </div>
>
> ```
> <?php
> $e = NULL;
> if (false === socket_select($r, $w, $e, 0)) {
>     echo "socket_select() falló. Razón: " .
>         socket_strerror(socket_last_error()) . "\n";
> }
> ?>
>
>      
> ```
>
> </div>

## Ejemplos

Ejemplo con `socket_select`

```
<?php
/* Prepara el array read (sockets monitorizadas en lectura) */
$read   = array($socket1, $socket2);
$write  = NULL;
$except = NULL;
$num_changed_sockets = socket_select($read, $write, $except, 0);

if ($num_changed_sockets === false) {
  /* Manejo de errores */
} else if ($num_changed_sockets > 0) {
  /* Al menos una de las sockets ha sido modificada */
}
?>

    
```php

## Notas

> [!NOTE]
> Tenga cuidado con las implementaciones de sockets, que deben ser manipuladas con delicadeza. Algunas reglas básicas:
>
> - Siempre debe intentarse usar `socket_select` sin timeout. Su programa no debería hacer nada si no hay datos disponibles. El código que depende de un timeout generalmente es poco portable y difícil de depurar.
>
> - Un socket no debe ser añadido a uno de los arrays de argumentos, si no se desea verificar el resultado después de la llamada a `socket_select`. Después del retorno de `socket_select`, todos los sockets en todos los arrays deben ser verificados. Todo socket que esté disponible en escritura o lectura debe ser usado para escribir o leer.
>
> - Si escribe o lee con un socket devuelto en un array, tenga en cuenta que no podrá escribir o leer todas las datos que solicite. Esté preparado para poder leer solo un byte.
>
> - Es común a la mayoría de las implementaciones de sockets que la única excepción interceptada por los sockets en el array `except` sea el caso de datos fuera de límites, recibidos por un socket.

## Véase también

`socket_read`, `socket_write`, `socket_last_error`, `socket_strerror`
