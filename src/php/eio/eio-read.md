---
title: eio_read
description: Leer de un descriptor de fichero en un índice dado
source_url: https://www.php.net/manual/es/function.eio-read.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-read.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_revision: 4e5389401
order: 17030
---

eio_read

Leer de un descriptor de fichero en un índice dado

## Descripción

```php
eio_read(mixed $fd, int $length, int $offset, int $pri, callable $callback, [mixed $data]): resource
```php

`eio_read` lee hasta `length` bytes desde el descriptor de fichero `fd` empezando en `offset`. Los bytes leídos son almacenados en el argumento `result` de `callback`.

## Parámetros

`fd`  
Un flujo, un recurso Socket, o un descriptor numérico de fichero.

`length`  
El número máximo de bytes a leer.

`offset`  
El índice dentro del fichero.

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

`eio_read` almacena los bytes leídos en el argumento `result` de la función `callback`.

## Ejemplos

Ejemplo de `eio_read`

```
<?php
// Abrir un fichero temporal y escribir algunos bytes en él
$nombre_fichero_temp = "eio-temp-file.tmp";
$fp = fopen($nombre_fichero_temp, "w");
fwrite($fp, "1234567890");
fclose($fp);

/* Es llamada cuando eio_read() termina */
function mi_llamada_retorno_read($datos, $resultado) {
    global $nombre_fichero_temp;

 // Imprimir los bytes leídos
    var_dump($resultado);

 // Cerrar el fichero
    eio_close($datos);
    eio_event_loop();

 // Eliminar el fichero temporal
    @unlink($nombre_fichero_temp);
}

/* Es llamada cuanco eio_open() termina */
function mi_llamada_retorno_fichero abierto($datos, $resultado) {
 // $resultado debería contener el descriptor del fichero
    if ($resultado > 0) {
  // Leer 5 bytes empezando desde el tercero
        eio_read($resultado, 5, 2, EIO_PRI_DEFAULT, "mi_llamada_retorno_read", $resultado);
        eio_event_loop();
    } else {
  // eio_open() falló
        unlink($datos);
    }
}

// Abrir el fichero para leer y escribir
eio_open($nombre_fichero_temp, EIO_O_RDWR, NULL,
    EIO_PRI_DEFAULT, "mi_llamada_retorno_fichero abierto", $nombre_fichero_temp);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    string(5) "34567"

## Véase también

eio_open

eio_write

eio_close

eio_event_loop
