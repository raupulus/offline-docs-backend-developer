---
title: number_format
description: Formatea un número para su visualización
source_url: https://www.php.net/manual/es/function.number-format.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/strings/functions/number-format.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: strings
translation_status: ready
translation_reviewed: true
translation_revision: 45042fef6
order: 88940
---

number_format

Formatea un número para su visualización

## Descripción

```php
number_format(float $num, [int $decimals], [string $decimal_separator], [string $thousands_separator]): string
```php

Formatea un número con los miles agrupados y opcionalmente con cifras decimales utilizando la regla de redondeo al más cercano.

## Parámetros

`num`  
El número a formatear.

`decimals`  
Define el número de cifras decimales. Si es `0`, el `decimal_separator` es omitido del valor de retorno. A partir de PHP 8.3.0, cuando el valor es negativo, `num` es redondeado a `decimals` cifras significativas antes del punto decimal. Antes de PHP 8.3.0, los valores negativos eran ignorados y tratados de la misma manera que `0`.

`decimal_separator`  
Define el separador para el punto decimal.

`thousands_separator`  
Define el separador de miles.

## Valores devueltos

Una versión formateada del número `num`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Se añadió el manejo de valores negativos para `decimals`. |
| 8.0.0 | Antes de esta versión, `number_format` aceptaba uno, dos o cuatro argumentos (pero no tres). |
| 7.2.0 | `number_format` fue modificado para no permitir devolver `-0`, anteriormente `-0` podía ser devuelto para casos donde `num` valía `-0.01`. |

Un valor negativo para `decimals`

A partir de PHP 8.3.0, un valor negativo para `decimals` es utilizado para redondear el número de cifras significativas antes del punto decimal.

```
<?php
$number = "1234.5678";
var_dump(number_format($number, -1));
var_dump(number_format($number, -2));
var_dump(number_format($number, -3));
?>

   
```php

El ejemplo anterior mostrará:

    string(5) "1 230"
    string(5) "1 200"
    string(5) "1 000"

## Ejemplos

Ejemplo con `number_format`

En notación francesa, se utilizan generalmente dos cifras después de la coma, una coma como separador decimal y un espacio como separador de miles. El siguiente ejemplo muestra cómo formatear un número de diferentes maneras:

```
<?php

$number = 1234.56;

// Notación inglesa (por omisión)
echo number_format($number), PHP_EOL;
// 1,235

// Notación francesa
echo number_format($number, 2, ',', ' '), PHP_EOL;
// 1 234,56

$number = 1234.5678;

// Notación inglesa sin separador de miles
echo number_format($number, 2, '.', ''), PHP_EOL;
// 1234.57

?>

    
```php

## Véase también

`money_format`, `sprintf`, `printf`, `sscanf`
