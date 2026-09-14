---
title: yaz_scan
description: Prepara para un escaneo YAZ
source_url: https://www.php.net/manual/es/function.yaz-scan.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-scan.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_reviewed: false
translation_revision: 96c9d88ba
order: 107920
---

yaz_scan

Prepara para un escaneo YAZ

## Descripción

```php
yaz_scan(resource $id, string $type, string $startterm, [array $flags]): void
```php

Esta función prepara para una solicitud "Z39.50 Scan Request" en la conexión YAZ especificada.

Para transferir realmente la "Scan Request" del servidor y recibir la "Scan Response", debe llamarse `yaz_wait`. Después de la finalización de la llamada a `yaz_wait`, llamar a `yaz_error` y `yaz_scan_result` para gestionar la respuesta.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`type`  
Actualmente sólo está soportado el tipo `rpn` .

`startterm`  
Punto de partida del escaneo.

La forma en la que el punto de partida es especificado, viene dado por el parámetro `type`.

La sintaxis de este parámetro es parecido al de la consulta RPN tal y como se describe en `yaz_search`. Consiste en cero o más especificaciones del operador `@attr`, seguido de exactamente un token.

`flags`  
Este parámetro opcional describe información adicional para controlar el comportamiento de la solicitud de escaneo. Tres índices se leen actualmente del array de marcas: `number` (número de términos solicitados), `position` (posición preferida del término) y `stepSize` (tamaño preferido del paso).

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

función PHP que escanea títulos

```
<?php
function scan_titles($id, $startterm)
{
  yaz_scan($id, "rpn", "@attr 1=4 " . $startterm);
  yaz_wait();
  $errno = yaz_errno($id);
  if ($errno == 0) {
    $ar = yaz_scan_result($id, $options);
    echo 'Scan ok; ';
    foreach ($options as $key => $val) {
      echo "$key = $val ";
    }
    echo '<br /><table>';
    while (list($key, list($k, $term, $tcount)) = each($ar)) {
      if (empty($k)) continue;
      echo "<tr><td>$term</td><td>$tcount</td></tr>";
    }
    echo '</table>';
  } else {
    echo "Error de escaneo. Error: " . yaz_error($id) . "<br />";
  }
}
?>

    
```php
