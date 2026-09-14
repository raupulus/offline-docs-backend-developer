---
title: fgetcsv
description: Obtiene una línea desde un puntero de archivo y la analiza para campos
  CSV
source_url: https://www.php.net/manual/es/function.fgetcsv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fgetcsv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 330a38c4d
order: 23430
---

fgetcsv

Obtiene una línea desde un puntero de archivo y la analiza para campos CSV

## Descripción

```php
fgetcsv(resource $stream, [int $length], [string $separator], [string $enclosure], [string $escape]): array
```php

Similar a `fgets` pero `fgetcsv` analiza la línea que lee y busca los campos CSV, que devuelve en un array que los contiene.

> [!NOTE]
> Los parámetros de configuración local son tenidos en cuenta por esta función. Por ejemplo, los datos codificados en ciertos juegos de caracteres de un byte pueden ser analizados incorrectamente si `LC_CTYPE` es `en_US.UTF-8`.

## Parámetros

`stream`  
Un puntero válido a un archivo abierto con `fopen`, `popen` o `fsockopen`.

`length`  
Debe ser mayor que la línea más larga (en términos de caracteres) a leer en el archivo (incluyendo el carácter de fin de línea). En caso contrario la línea será dividida en fragmentos de `length` caracteres, a menos que la división ocurra dentro de un encierro.

Omitir este parámetro (o establecerlo a 0, o `null` en PHP 8.0.0 o versiones posteriores) hace que la longitud máxima de la línea no esté limitada, lo cual es ligeramente más lento.

`separator`  
El parámetro `separator` define el separador de campo. Debe tratarse de un carácter de un solo byte.

`enclosure`  
El parámetro `enclosure` define el carácter de encierro de los campos. Debe tratarse de un carácter de un solo byte.

`escape`  
El parámetro `escape` define el carácter de escape. Debe tratarse de un carácter de un solo byte o una cadena vacía. La cadena vacía (`""`) desactiva el mecanismo de escape propietario.

> [!WARNING]
> En el flujo de entrada, el carácter `enclosure` siempre puede ser escapado duplicándolo dentro de una cadena entrecomillada, lo que resulta en un único carácter `enclosure` en el resultado analizado. El carácter `escape` funciona de manera diferente: si una secuencia de caracteres `escape` y `enclosure` aparece en la entrada, ambos caracteres estarán presentes en el resultado analizado. Así, para los parámetros por defecto, una línea CSV como `"a""b","c\"d"` tendrá los campos analizados como `a"b` y `c\"d`, respectivamente.

> [!WARNING]
> A partir de PHP 8.4.0, el uso del valor por omisión de `escape` está deprecado. Debe ser proporcionado explícitamente ya sea por posición o mediante el uso de los [argumentos nombrados](#functions.named-arguments).

> [!WARNING]
> Cuando `escape` se define con un valor diferente a una cadena vacía (`""`), puede resultar en un CSV que no sea compatible con [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) o que no pueda sobrevivir a un ciclo de ida y vuelta a través de las funciones CSV de PHP. El valor predeterminado de `escape` es `"\\"`, por lo que se recomienda definirlo explícitamente como cadena vacía. El valor predeterminado cambiará en una futura versión de PHP, no antes de PHP 9.0.

## Valores devueltos

Devuelve un array indexado que contiene los campos leídos en caso de éxito, o `false` si ocurre un error.

> [!NOTE]
> Una línea vacía en un archivo CSV será devuelta en forma de un array que contiene el valor `null` y no será tratada como un error.

> [!NOTE]
> Si PHP no reconoce correctamente los finales de línea al leer ficheros que han sido creados o leídos en un Macintosh, la activación de la opción de configuración [auto_detect_line_endings](#ini.auto-detect-line-endings) puede resolver el problema.

## Errores/Excepciones

Genera una ValueError si `separator` o `enclosure` no tiene una longitud de un byte.

Genera una ValueError si `escape` no tiene una longitud de un byte o es una cadena vacía.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Confiar en el valor por omisión de `escape` está ahora deprecado. |
| 8.3.0 | Una cadena vacía es devuelta en lugar de una cadena que contiene un solo byte nulo para el último campo si este contiene únicamente un delimitador no terminado. |
| 8.0.0 | `length` ahora es nullable. |
| 7.4.0 | El parámetro `escape` ahora acepta una cadena vacía para desactivar el mecanismo de escape propietario. |

## Ejemplos

Lee y muestra el contenido de un archivo CSV

```
<?php
$row = 1;
if (($handle = fopen("test.csv", "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
        $num = count($data);
        echo "<p> $num campos en la línea $row: <br /></p>\n";
        $row++;
        for ($c=0; $c < $num; $c++) {
            echo $data[$c] . "<br />\n";
        }
    }
    fclose($handle);
}
?>

    
```php

## Véase también

fputcsv

str_getcsv

SplFileObject::fgetcsv

SplFileObject::fputcsv

SplFileObject::setCsvControl

SplFileObject::getCsvControl

explode

file

pack
