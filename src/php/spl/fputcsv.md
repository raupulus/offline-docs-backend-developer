---
title: SplFileObject::fputcsv
description: Escribe un array en forma de línea CSV
source_url: https://www.php.net/manual/es/splfileobject.fputcsv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fputcsv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 73007ad98
order: 84410
---

SplFileObject::fputcsv

Escribe un array en forma de línea CSV

## Descripción

```php
public SplFileObject::fputcsv(array $fields, [string $separator], [string $enclosure], [string $escape], [string $eol]): int
```php

Escribe un array `fields` en forma de línea CSV.

## Parámetros

`fields`  
Un array de valores.

`eol`  
El parámetro opcional `eol` define una secuencia de fin de línea personalizada.

> [!WARNING]
> Cuando `escape` se define con un valor diferente a una cadena vacía (`""`), puede resultar en un CSV que no sea compatible con [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) o que no pueda sobrevivir a un ciclo de ida y vuelta a través de las funciones CSV de PHP. El valor predeterminado de `escape` es `"\\"`, por lo que se recomienda definirlo explícitamente como cadena vacía. El valor predeterminado cambiará en una futura versión de PHP, no antes de PHP 9.0.

> [!NOTE]
> Si un carácter `enclosure` está contenido en un campo, será escapado duplicándolo, a menos que esté inmediatamente precedido por un `escape`.

## Valores devueltos

Devuelve la longitud de la cadena escrita o `false` si ocurre un error.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | Se añadió el parámetro opcional `eol`. |
| 7.4.0 | El parámetro `escape` ahora acepta una cadena vacía para desactivar el mecanismo de escape propietario. |

## Ejemplos

Ejemplo con SplFileObject::fputcsv

```
<?php

$list = array (
    array('aaa', 'bbb', 'ccc', 'dddd'),
    array('123', '456', '789'),
    array('"aaa"', '"bbb"')
);

$file = new SplFileObject('file.csv', 'w');

foreach ($list as $fields) {
    $file->fputcsv($fields);
}

?>

    
```php

El siguiente ejemplo escribirá la línea siguiente en el fichero `file.csv`:

    aaa,bbb,ccc,dddd
    123,456,789
    """aaa""","""bbb"""

## Véase también

SplFileObject::fgetcsv

SplFileObject::setCsvControl

SplFileObject::getCsvControl

fputcsv

fgetcsv

str_getcsv
