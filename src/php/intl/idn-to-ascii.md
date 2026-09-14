---
title: idn_to_ascii
description: Convierte un nombre de dominio al formato IDNA ASCII
source_url: https://www.php.net/manual/es/function.idn-to-ascii.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/idn/idn-to-ascii.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1be57c2d7
order: 39920
---

idn_to_ascii

Convierte un nombre de dominio al formato IDNA ASCII

## Descripción

Estilo procedimental

```php
idn_to_ascii(string $domain, [int $flags], [int $variant], [array $idna_info]): string
```php

Esta función convierte un nombre de dominio Unicode a un formato ASCII compatible con IDNA, en minúsculas.

## Parámetros

`domain`  
El dominio a convertir, que debe estar codificado en UTF-8.

`flags`  
Opciones de conversión - combinación de constantes IDNA\_\*. (excepto las constantes IDNA_ERROR\_\*).

`variant`  
Puede ser `INTL_IDNA_VARIANT_2003` (obsoleto a partir de PHP 7.2.0) para IDNA 2003, o `INTL_IDNA_VARIANT_UTS46` (solo disponible a partir de ICU 4.6) para UTS \#46.

`idna_info`  
Este parámetro solo puede ser utilizado si la constante `INTL_IDNA_VARIANT_UTS46` ha sido utilizada en el parámetro `variant`. En este caso, será un array con la clave `'result'` conteniendo el resultado de la transformación, la clave `'isTransitionalDifferent'` conteniendo un booleano indicando si se ha utilizado el mecanismo transicional UTS \#46 que ha alterado o no el resultado, y la clave `'errors'` conteniendo un `int` representando un conjunto de bits de las constantes de error IDNA_ERROR\_\*.

## Valores devueltos

El nombre de dominio codificado en formato ASCII-compatible. o `false` si ocurre un error

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.4.0 | Ahora lanza un ValueError si el parámetro `domain` está vacío. |
| 8.4.0 | Ahora lanza un ValueError si el parámetro `variant` no es `INTL_IDNA_VARIANT_UTS46`. |
| 7.4.0 | El valor por defecto del parámetro `variant` es ahora `INTL_IDNA_VARIANT_UTS46` en lugar de la constante `INTL_IDNA_VARIANT_2003` depreciada. |
| 7.2.0 | `INTL_IDNA_VARIANT_2003` ha sido depreciado; utilizar `INTL_IDNA_VARIANT_UTS46` en su lugar. |

## Ejemplos

Ejemplo con `idn_to_ascii`

```
<?php

echo idn_to_ascii('täst.de');
?>

   
```php

El ejemplo anterior mostrará:

    xn--tst-qla.de

Los nombres de dominio completamente ASCII son simplemente convertidos a minúsculas

```
<?php

var_dump(idn_to_ascii('Example.com'));

?>

    
```php

El ejemplo anterior mostrará:

    string(11) "example.com"

      

## Véase también

`idn_to_utf8`
