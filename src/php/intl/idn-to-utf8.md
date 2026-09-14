---
title: idn_to_utf8
description: Convierte el nombre de dominio IDNA ASCII a Unicode
source_url: https://www.php.net/manual/es/function.idn-to-utf8.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/idn/idn-to-utf8.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1be57c2d7
order: 39930
---

idn_to_utf8

Convierte el nombre de dominio IDNA ASCII a Unicode

## Descripción

Estilo procedimental

```php
idn_to_utf8(string $domain, [int $flags], [int $variant], [array $idna_info]): string
```php

Esta función convierte el nombre de dominio en formato IDNA ASCII-compatible a Unicode, codificado en UTF-8.

## Parámetros

`domain`  
Dominio a convertir desde el formato IDNA ASCII-compatible.

`flags`  
Opciones de conversión - una combinación de las constantes IDNA\_\* (excepto las constantes IDNA_ERROR\_\*).

`variant`  
Puede ser `INTL_IDNA_VARIANT_2003` (obsoleto a partir de PHP 7.2.0) para IDNA 2003, o `INTL_IDNA_VARIANT_UTS46` (solo disponible a partir de ICU 4.6) para UTS \#46.

`idna_info`  
Este parámetro solo puede ser utilizado si la constante `INTL_IDNA_VARIANT_UTS46` ha sido utilizada como parámetro para `variant`. En este caso, este parámetro será rellenado por un array donde la clave `'result'` contendrá el resultado de la transformación, la clave `'isTransitionalDifferent'` contendrá un booleano indicando si el uso del mecanismo transicional UTS \#46 ha alterado o no el resultado, y la clave `'errors'` contendrá un `int` representando un juego de bits de constantes IDNA_ERROR\_\*.

## Valores devueltos

Nombre de dominio en Unicode, codificado UTF-8. o `false` si ocurre un error

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora lanza un ValueError si el parámetro `domain` está vacío. |
| 8.4.0 | Ahora lanza un ValueError si el parámetro `variant` no es `INTL_IDNA_VARIANT_UTS46`. |
| 7.4.0 | El valor por defecto del parámetro `variant` es ahora `INTL_IDNA_VARIANT_UTS46` en lugar de la constante `INTL_IDNA_VARIANT_2003` deprecada. |
| 7.2.0 | `INTL_IDNA_VARIANT_2003` ha sido deprecado; utilizar `INTL_IDNA_VARIANT_UTS46` en su lugar. |

## Ejemplos

Ejemplo con `idn_to_utf8`

```
<?php

echo idn_to_utf8('xn--tst-qla.de');

?>

   
```php

El ejemplo anterior mostrará:

    täst.de

      

## Véase también

`idn_to_ascii`
