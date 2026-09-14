---
title: SplFileObject::setCsvControl
description: Define las opciones CSV
source_url: https://www.php.net/manual/es/splfileobject.setcsvcontrol.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/setcsvcontrol.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: true
translation_revision: 4a0ce5d81
order: 84590
---

SplFileObject::setCsvControl

Define las opciones CSV

## Descripción

```php
public SplFileObject::setCsvControl([string $separator], [string $enclosure], [string $escape]): void
```php

Define el delimitador, el carácter de escape y el carácter utilizado para encerrar los campos CSV analizados.

## Parámetros

> [!WARNING]
> Cuando `escape` se define con un valor diferente a una cadena vacía (`""`), puede resultar en un CSV que no sea compatible con [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) o que no pueda sobrevivir a un ciclo de ida y vuelta a través de las funciones CSV de PHP. El valor predeterminado de `escape` es `"\\"`, por lo que se recomienda definirlo explícitamente como cadena vacía. El valor predeterminado cambiará en una futura versión de PHP, no antes de PHP 9.0.

## Valores devueltos

No se retorna ningún valor.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | El argumento `escape` acepta ahora una cadena de caracteres vacía para desactivar el mecanismo de escape propietario. |

## Ejemplos

Ejemplo con SplFileObject::setCsvControl

```
<?php
$file = new SplFileObject("data.csv");
$file->setFlags(SplFileObject::READ_CSV);
$file->setCsvControl('|');
foreach ($file as $row) {
    list ($fruit, $quantity) = $row;
    // Operación sobre los datos
}
?>

    
```php

Contenido de data.csv

```
<?php
apples|20
bananas|14
cherries|87
?>

    
```php

## Véase también

SplFileObject::getCsvControl

SplFileObject::fgetcsv

SplFileObject::fputcsv

fputcsv

fgetcsv

str_getcsv
