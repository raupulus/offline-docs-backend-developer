---
title: stream_select
description: Supervisa la modificación de uno o varios flujos
source_url: https://www.php.net/manual/es/function.stream-select.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-select.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_revision: a758e79c3
order: 88060
---

stream_select

Supervisa la modificación de uno o varios flujos

## Descripción

```php
stream_select(array $read, array $write, array $except, int $seconds, [int $microseconds]): int
```php

`stream_select` acepta un array de flujos y espera a que alguno de ellos cambie de estado. Esta operación es equivalente a lo que hace la función `socket_select`, salvo que trabaja sobre un flujo.

## Parámetros

`read`  
Los flujos que están listados en el parámetro `read` serán supervisados en lectura, es decir, si hay nuevos bytes disponibles para lectura (para ser precisos, si una lectura no bloqueará, lo que incluye también flujos que están al final de archivo, en cuyo caso una llamada a la función `fread` retornará un string de tamaño 0).

`write`  
Los flujos que están listados en el parámetro `write` serán supervisados en escritura (para ser precisos, si una escritura no bloqueará).

`except`  
Los flujos que están listados en el parámetro `except` serán supervisados para ver si se lanza una excepción.

> [!NOTE]
> Cuando `stream_select` termina, los arrays `read`, `write` y `except` son modificados para indicar qué flujos han cambiado de estado actualmente. Las claves originales del array se preservan.

`seconds`  
Los parámetros `seconds` y `microseconds` forman el *tiempo límite*, `seconds` especifica el número de segundos mientras que `microseconds`, el número de microsegundos. El parámetro `timeout` representa el límite superior del tiempo que `stream_select` debe esperar antes de terminar. Si `seconds` está definido a `0` y `microseconds` vale `0` o `null`, `stream_select` no esperará datos - en su lugar, terminará inmediatamente, indicando el estado actual del flujo.

Si `seconds` vale `null`, `stream_select` puede bloquearse indefinidamente, terminando únicamente cuando un evento en alguno de los flujos supervisados ocurra (o si una señal interrumpe la llamada al sistema).

> [!WARNING]
> Utilizar un valor de `0` permite probar instantáneamente el estado de los flujos, pero debe saberse que no se recomienda utilizar `0` en un bucle, ya que esto hará que el script consuma una gran cantidad de procesador.
>
> Es mucho mejor especificar un valor de algunos segundos, incluso si se debe supervisar y ejecutar diferentes códigos de manera simultánea. Por ejemplo, utilizar un valor de al menos `200000` microsegundos, se reducirá considerablemente el consumo de procesador del script.
>
> No se debe olvidar que el valor de expiración es la duración máxima de espera, si no ocurre nada: `stream_select` retornará un resultado tan pronto como uno de los flujos suministrados esté listo para su uso.

`microseconds`  
Véase la descripción de `seconds`.

## Valores devueltos

En caso de éxito, `stream_select` retorna el número de flujos que han cambiado, lo que puede ser `0`, si el tiempo límite fue alcanzado antes de que los flujos cambien. En caso de error, la función retornará `false` y un aviso será devuelto (esto puede ocurrir si la llamada al sistema es interrumpida por una señal entrante).

## Historial de cambios

| Versión | Descripción                       |
|---------|-----------------------------------|
| 8.1.0   | `microseconds` ahora es nullable. |

## Ejemplos

Ejemplo con `stream_select`

Este ejemplo supervisa si los datos llegan para ser leídos ya sea en `$stream1` o en `$stream2`. Si el tiempo límite es `0`, la función termina inmediatamente:

```
<?php
/* Preparación del array de flujos de lectura */
$read   = array($stream1, $stream2);
$write  = NULL;
$except = NULL;
if (false === ($num_changed_streams = stream_select($read, $write, $except, 0))) {
    /* Manejo de errores */
} elseif ($num_changed_streams > 0) {
    /* Al menos uno de los flujos ha cambiado */
}
?>

    
```php

## Notas

> [!NOTE]
> Debido a una limitación del motor Zend actual, no es posible pasar el valor `null` directamente como parámetro de una función que espera parámetros pasados por referencia. En su lugar, se recomienda utilizar una variable temporal, o una expresión cuyo miembro izquierdo sea una variable temporal. Como esto:
>
> ```
> <?php
> $e = NULL;
> stream_select($r, $w, $e, 0);
> ?>
>
>     
> ```

> [!NOTE]
> Asegúrese de utilizar el operador `===` cuando busque errores. Como `stream_select` puede retornar 0, una comparación realizada con `==` lo evaluaría como `true`:
>
> ```
> <?php
> $e = NULL;
> if (false === stream_select($r, $w, $e, 0)) {
>     echo "stream_select() falló\n";
> }
> ?>
>
>     
> ```

> [!NOTE]
> Si ha escrito o leído en un flujo que es retornado en los arrays de flujos, sea consciente de que estos flujos pueden no haber escrito o leído la totalidad de los datos solicitados. Sea capaz de leer un solo byte.

> [!NOTE]
> Algunos flujos (como `zlib`) no pueden ser seleccionados por esta función.

> [!NOTE]
> Utilizar la función `stream_select` en un puntero de archivo retornado por `proc_open` fallará y retornará `false` en Windows.
>
> `STDIN` desde una consola cambia su estado tan pronto como *cualquier* evento de entrada esté disponible, pero leer desde un flujo puede seguir siendo bloqueante.

## Véase también

stream_set_blocking
