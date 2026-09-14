---
title: eio_open
description: Abre un fichero
source_url: https://www.php.net/manual/es/function.eio-open.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/eio/functions/eio-open.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: eio
translation_status: ready
translation_reviewed: false
translation_revision: dfd68fd22
order: 17010
---

eio_open

Abre un fichero

## Descripción

```php
eio_open(string $path, int $flags, int $mode, int $pri, callable $callback, [mixed $data]): resource
```php

`eio_open` abre un fichero especificado por el argumento `path` con el modo de acceso especificado por el argumento `mode` con los `flags` dados.

## Parámetros

`path`  
Ruta hacia el fichero a abrir.

> [!WARNING]
> Con algunas APIs (i.e. *PHP-FPM*), la llamada puede fallar si no se especifica la ruta completa.

`flags`  
Una constante entre las constantes *EIO_O\_\**, o bien una combinación de estas constantes. Las constantes *EIO_O\_\** tienen el mismo significado que las constantes correspondientes *O\_\** definidas en el archivo de encabezados C `fnctl.h`. Por omisión, vale `EIO_O_RDWR`.

`mode`  
Una constante entre las constantes *EIO_S_I\**, o bien una combinación de estas constantes (vía el operador OR). Las constantes tienen el mismo significado que las constantes correspondientes *S_I\** definidas en el archivo de encabezados C [sys/stat.h](http://pubs.opengroup.org/onlinepubs/9699919799/basedefs/sys_stat.h.html). Requerido si se crea un fichero. De lo contrario, será ignorado.

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
Variables arbitrarias a pasar a la función de devolución de llamada `callback`.

## Valores devueltos

`eio_open` devuelve un descriptor de fichero en el argumento `result` de la función de devolución de llamada `callback` en caso de éxito; de lo contrario, `result` valdrá `-1`.

## Ejemplos

Ejemplo con `eio_open`

```
<?php
$temp_filename = "eio-temp-file.tmp";

/* Será llamado cuando la función eio_close() haya terminado */
function my_close_cb($data, $result) {
 // Cero indica una ejecución con éxito
    var_dump($result == 0);
 @unlink($data);
}

/* Será llamado cuando la función eio_open() haya terminado */
function my_file_opened_callback($data, $result) {
 // $result debe contener el descriptor de fichero
    var_dump($result > 0);

    if ($result > 0) {
  // Cierra el fichero
        eio_close($result, EIO_PRI_DEFAULT, "my_close_cb", $data);
        eio_event_loop();
    }
}

// Crea un nuevo fichero para lectura y escritura
// No permite a grupos y otros hacer nada con este fichero
eio_open($temp_filename, EIO_O_CREAT | EIO_O_RDWR, EIO_S_IRUSR | EIO_S_IWUSR,
  EIO_PRI_DEFAULT, "my_file_opened_callback", $temp_filename);
eio_event_loop();
?>

   
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    bool(true)

## Véase también

eio_mknod
