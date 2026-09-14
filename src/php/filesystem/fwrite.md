---
title: fwrite
description: Escribe en un fichero en modo binario
source_url: https://www.php.net/manual/es/function.fwrite.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fwrite.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: bb6247b68
order: 23720
---

fwrite

Escribe en un fichero en modo binario

## Descripción

```php
fwrite(resource $stream, string $data, [int $length]): int
```php

`fwrite` escribe el contenido de la cadena `data` en el fichero apuntado por `stream`.

## Parámetros

`stream`  
Un puntero al sistema de ficheros de tipo `resource` que típicamente se crea utilizando `fopen`.

`data`  
La cadena a escribir.

`length`  
Si se proporciona la longitud `length`, la escritura se detendrá después de `length` bytes, o al final de la cadena (lo que ocurra primero).

## Valores devueltos

`fwrite` devuelve el número de bytes escritos o `false` si ocurre un error.

## Errores/Excepciones

La función `fwrite` emite una `E_WARNING` si ocurre un error.

## Historial de cambios

| Versión | Descripción                 |
|---------|-----------------------------|
| 8.0.0   | `length` ahora es nullable. |

## Ejemplos

Ejemplo con `fwrite`

```
     
<?php
$filename = 'test.txt';
$somecontent = "Añadiendo cadena al fichero\n";

// Asegurémonos de que el fichero es accesible en escritura
if (is_writable($filename)) {

    // En nuestro ejemplo, abrimos el fichero $filename en modo de añadir
    // El puntero del fichero se coloca al final del fichero
    // es ahí donde $somecontent será colocado
    if (!$fp = fopen($filename, 'a')) {
         echo "No se puede abrir el fichero ($filename)";
         exit;
    }

    // Escribamos algo en nuestro fichero.
    if (fwrite($fp, $somecontent) === FALSE) {
        echo "No se puede escribir en el fichero ($filename)";
        exit;
    }

    echo "La escritura de ($somecontent) en el fichero ($filename) ha tenido éxito";

    fclose($fp);

} else {
    echo "El fichero $filename no es accesible en escritura.";
}
?>

    
```php

## Notas

> [!NOTE]
> La escritura en un flujo puede terminar antes de que la cadena completa sea escrita. El valor devuelto por la función `fwrite` puede ser verificado de la siguiente manera:
>
> ```
> <?php
> function fwrite_stream($fp, $string) {
>     for ($written = 0; $written < strlen($string); $written += $fwrite) {
>         $fwrite = fwrite($fp, substr($string, $written));
>         if ($fwrite === false) {
>             return $fwrite;
>         }
>     }
>     return $written;
> }
> ?>
>
>     
> ```

> [!NOTE]
> En los sistemas que hacen la distinción entre ficheros binarios y ficheros de texto (por ejemplo, Windows), el fichero debe ser abierto con la opción 'b' incluida en el parámetro de modo de `fopen`.

> [!NOTE]
> Si `stream` está abierto en modo añadir (`append`), `fwrite` será atómico (excepto si el tamaño de `data` excede el tamaño del bloque del sistema de ficheros, en algunas plataformas, y siempre que el fichero se encuentre en el sistema de ficheros local). Por lo tanto, no es necesario utilizar la función `flock` en un recurso antes de llamar a la función `fwrite`; todos los datos serán escritos sin interrupción.

> [!NOTE]
> Si se escribe dos veces en el fichero, los datos serán añadidos al final del fichero; esto significa que el siguiente ejemplo no dará el resultado esperado:
>
> ```
> <?php
> $fp = fopen('data.txt', 'w');
> fwrite($fp, '1');
> fwrite($fp, '23');
> fclose($fp);
>
> // el contenido de 'data.txt' es ahora 123 y no 23 !
> ?>
>
>         
> ```

## Véase también

`fread`, `fopen`, `fsockopen`, `popen`, `file_get_contents`, `pack`
