---
title: timezone_name_from_abbr
description: Devuelve el nombre de una zona horaria a partir de su abreviatura y del
  desplazamiento UTC
source_url: https://www.php.net/manual/es/function.timezone-name-from-abbr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/datetime/functions/timezone-name-from-abbr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: datetime
translation_status: ready
translation_revision: 3a8c3e77d
order: 11390
---

timezone_name_from_abbr

Devuelve el nombre de una zona horaria a partir de su abreviatura y del desplazamiento UTC

## Descripción

```php
timezone_name_from_abbr(string $abbr, [int $utcOffset], [int $isDST]): string
```php

## Parámetros

`abbr`  
Abreviatura de la zona horaria.

`utcOffset`  
Desplazamiento respecto al GMT en segundos. El valor por omisión es -1 lo que significa que se devuelve la primera zona horaria encontrada que corresponda a `abbr`. De lo contrario, se busca el desplazamiento exacto y solo si no se encuentra, se devuelve la primera zona horaria con cualquier desplazamiento.

`isDST`  
Indicador de hora de verano/hora de invierno. Por omisión -1 que significa que el desplazamiento de hora de verano/hora de invierno no se tiene en cuenta en la búsqueda aunque la zona horaria lo gestione. Si se establece en 1, entonces el `utcOffset` se asume que incluye el desplazamiento de hora de verano /hora de invierno; si es 0 entonces `utcOffset` se asume que representa un desplazamiento que no tiene en cuenta la hora de verano/invierno. Si `abbr` no existe entonces la zona horaria se busca únicamente mediante `utcOffset` y `isDST`.

## Valores devueltos

Devuelve un nombre de zona horaria en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `timezone_name_from_abbr`

```
<?php
echo timezone_name_from_abbr("CET") . "\n";
echo timezone_name_from_abbr("", 3600, 0) . "\n";

    
```php

Resultado del ejemplo anterior es similar a:

    Europe/Berlin
    Europe/Paris

## Véase también

`timezone_abbreviations_list`
