---
title: SplFileObject::fgetcsv
description: Recupera una línea del archivo y la analiza como datos CSV
source_url: https://www.php.net/manual/es/splfileobject.fgetcsv.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fgetcsv.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: 0a3648a71
order: 84360
---

SplFileObject::fgetcsv

Recupera una línea del archivo y la analiza como datos CSV

## Descripción

```php
public SplFileObject::fgetcsv([string $separator], [string $enclosure], [string $escape]): array
```php

Recupera una línea del archivo y la analiza como datos CSV y devuelve un array que contiene todos los campos leídos.

## Parámetros

`separator`  
El delimitador de campo (un solo carácter de un byte). Por omisión, `,` o el valor definido por una llamada previa a SplFileObject::setCsvControl.

`enclosure`  
El carácter utilizado para encerrar el valor de un campo (un carácter de un solo byte). Por omisión, será una comilla doble o bien el valor definido utilizando el método SplFileObject::setCsvControl.

`escape`  
El carácter de escape de campo (un solo carácter de un byte). Por omisión, `"` o el valor definido por una llamada previa a SplFileObject::setCsvControl. Un `string` vacío (`""`) desactiva el mecanismo de escape propietario.

> [!WARNING]
> A partir de PHP 8.4.0, depender del valor por omisión de `escape` está deprecado. Debe ser proporcionado explícitamente ya sea por posición, ya sea mediante el uso de los [argumentos nombrados](#functions.named-arguments), o mediante una llamada a SplFileObject::setCsvControl.

> [!WARNING]
> Cuando `escape` se define con un valor diferente a una cadena vacía (`""`), puede resultar en un CSV que no sea compatible con [RFC 4180](https://datatracker.ietf.org/doc/html/rfc4180) o que no pueda sobrevivir a un ciclo de ida y vuelta a través de las funciones CSV de PHP. El valor predeterminado de `escape` es `"\\"`, por lo que se recomienda definirlo explícitamente como cadena vacía. El valor predeterminado cambiará en una futura versión de PHP, no antes de PHP 9.0.

## Valores devueltos

Devuelve un array indexado que contiene todos los campos leídos, o `false` si ocurre un error.

> [!NOTE]
> Una línea vacía de un archivo CSV será devuelta en forma de un array contenido un solo campo `null` a menos que se utilice `SplFileObject::SKIP_EMPTY | SplFileObject::DROP_NEW_LINE`, en cuyo caso, las líneas vacías serán ignoradas.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 7.4.0 | El parámetro `escape` ahora acepta una cadena de caracteres vacía para desactivar el mecanismo de escape propietario. |

## Ejemplos

Ejemplo con SplFileObject::fgetcsv

```
<?php
$file = new SplFileObject("data.csv");
while (!$file->eof()) {
    var_dump($file->fgetcsv());
}
?>

    
```php

Ejemplo con `SplFileObject::READ_CSV`

```
<?php
$file = new SplFileObject("animals.csv");
$file->setFlags(SplFileObject::READ_CSV);
foreach ($file as $row) {
    list($animal, $class, $legs) = $row;
    printf("Un %s es un %s con %d patas\n", $animal, $class, $legs);
}
?>

    
```php

Contenido de animals.csv

```
crocodile,reptile,4
dauphin,mammifère,0
canard,oiseau,2
koala,mammifère,4
saumon,poisson,0

    
```php

Resultado del ejemplo anterior es similar a:

    Un crocodile es un reptile con 4 patas
    Un dauphin es un mammifère con 0 patas
    Un canard es un oiseau con 2 patas
    Un koala es un mammifère con 4 patas
    Un saumon es un poisson con 0 patas

## Véase también

SplFileObject::fputcsv

SplFileObject::setCsvControl

SplFileObject::getCsvControl

SplFileObject::setFlags

SplFileObject::READ_CSV

SplFileObject::current

fputcsv

fgetcsv

str_getcsv
