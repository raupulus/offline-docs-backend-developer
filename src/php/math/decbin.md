---
title: decbin
description: Convierte de decimal a binario
source_url: https://www.php.net/manual/es/function.decbin.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/math/functions/decbin.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: math
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 44600
---

decbin

Convierte de decimal a binario

## Descripción

```php
decbin(int $num): string
```php

Devuelve un string que contiene la representación binaria del entero `num` proporcionado como argumento.

## Parámetros

`num`  
Valor decimal a convertir

<table>
<caption>Intervalo de entrada en máquinas de 32-bit</caption>
<thead>
<tr>
<th>Parámetro <code>num</code> positivo</th>
<th>Parámetro <code>num</code> negativo</th>
<th>Valor devuelto</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td></td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td></td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td></td>
<td>10</td>
</tr>
<tr>
<td colspan="3">... progresión normal ...</td>
</tr>
<tr>
<td>2147483646</td>
<td></td>
<td>1111111111111111111111111111110</td>
</tr>
<tr>
<td>2147483647 (mayor entero firmado)</td>
<td></td>
<td>1111111111111111111111111111111 (31 unos)</td>
</tr>
<tr>
<td>2147483648</td>
<td>-2147483648</td>
<td>10000000000000000000000000000000</td>
</tr>
<tr>
<td colspan="3">... progresión normal ...</td>
</tr>
<tr>
<td>4294967294</td>
<td>-2</td>
<td>11111111111111111111111111111110</td>
</tr>
<tr>
<td>4294967295 (mayor entero no firmado)</td>
<td>-1</td>
<td>11111111111111111111111111111111 (32 unos)</td>
</tr>
</tbody>
</table>

<table>
<caption>Intervalo de entrada en máquinas de 64-bit</caption>
<thead>
<tr>
<th>Parámetro <code>num</code> positivo</th>
<th>Parámetro <code>num</code> negativo</th>
<th>Valor devuelto</th>
</tr>
</thead>
<tbody>
<tr>
<td>0</td>
<td></td>
<td>0</td>
</tr>
<tr>
<td>1</td>
<td></td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td></td>
<td>10</td>
</tr>
<tr>
<td colspan="3">... progresión normal ...</td>
</tr>
<tr>
<td>9223372036854775806</td>
<td></td>
<td>111111111111111111111111111111111111111111111111111111111111110</td>
</tr>
<tr>
<td>9223372036854775807 (mayor entero firmado)</td>
<td></td>
<td>111111111111111111111111111111111111111111111111111111111111111 (63 unos)</td>
</tr>
<tr>
<td></td>
<td>-9223372036854775808</td>
<td>1000000000000000000000000000000000000000000000000000000000000000</td>
</tr>
<tr>
<td colspan="3">... progresión normal ...</td>
</tr>
<tr>
<td></td>
<td>-2</td>
<td>1111111111111111111111111111111111111111111111111111111111111110</td>
</tr>
<tr>
<td></td>
<td>-1</td>
<td>1111111111111111111111111111111111111111111111111111111111111111 (64 unos)</td>
</tr>
</tbody>
</table>

## Valores devueltos

Una representación binaria de `num`.

## Ejemplos

Ejemplo con `decbin`

```
<?php
echo decbin(12) . "\n";
echo decbin(26);
?>

    
```php

El ejemplo anterior mostrará:

    1100
    11010

## Véase también

`bindec`, `decoct`, `dechex`, `base_convert`, `printf`, utilizando `%b`, `%032b` o `%064b` como formato, `sprintf`, utilizando `%b`, `%032b` o `%064b` como formato
