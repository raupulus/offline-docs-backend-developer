---
title: fputcsv
description: Formatea una línea en CSV y la escribe en un fichero
source_url: https://www.php.net/manual/es/function.fputcsv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fputcsv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: 898627b9f
order: 23630
---

fputcsv

Formatea una línea en CSV y la escribe en un fichero

## Descripción

```php
fputcsv(resource $stream, array $fields, [string $separator], [string $enclosure], [string $escape], [string $eol]): int
```php

`fputcsv` formatea la línea pasada como `fields` (array) como CSV y la escribe (terminada por un `eol`) en el `stream` especificado.

## Parámetros

`stream`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

`fields`  
Un array de strings.

`eol`  
El parámetro opcional `eol` define una secuencia de fin de línea personalizada.

> [!WARNING]
> Cuando `escape` se define con un valor diferente a una cadena vacía (`""`), puede resultar en un CSV que no sea compatible con [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) o que no pueda sobrevivir a un ciclo de ida y vuelta a través de las funciones CSV de PHP. El valor predeterminado de `escape` es `"\\"`, por lo que se recomienda definirlo explícitamente como cadena vacía. El valor predeterminado cambiará en una futura versión de PHP, no antes de PHP 9.0.

> [!NOTE]
> Si un carácter `enclosure` está contenido en un campo, será escapado duplicándolo, a menos que esté inmediatamente precedido por un `escape`.

## Valores devueltos

Devuelve el tamaño de la cadena escrita o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Se añadió el parámetro opcional `eol`. |
| 7.4.0 | El parámetro `escape` ahora acepta una cadena vacía para desactivar el mecanismo de escape propietario. |

## Ejemplos

Ejemplo con `fputcsv`

```
<?php

$list = [
    ['aaa', 'bbb', 'ccc', 'dddd'],
    ['123', '456', '789'],
    ['"aaa"', '"bbb"']
];

$fp = fopen('file.csv', 'w');

foreach ($list as $fields) {
     fputcsv($fp, $fields, ',', '"', '');
}

fclose($fp);
?>

    
```php

El ejemplo anterior escribirá lo siguiente en `file.csv`:

    aaa,bbb,ccc,dddd
    123,456,789
    """aaa""","""bbb"""

## Véase también

fgetcsv

str_getcsv

SplFileObject::fgetcsv

SplFileObject::fputcsv

SplFileObject::setCsvControl

SplFileObject::getCsvControl
