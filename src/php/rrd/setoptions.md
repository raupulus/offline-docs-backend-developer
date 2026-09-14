---
title: RRDGraph::setOptions
description: Establece las opciones para la exportación gráfica rrd
source_url: https://www.php.net/manual/es/rrdgraph.setoptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/rrd/rrdgraph/setoptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: rrd
translation_status: ready
translation_reviewed: false
translation_revision: 0f2a5f5dd
order: 72770
---

RRDGraph::setOptions

Establece las opciones para la exportación gráfica rrd

## Descripción

```php
public RRDGraph::setOptions(array $options): void
```php

## Parámetros

`options`  
Lista de las opciones para la generación de imágenes a partir del archivo de base de datos RRD. Esta puede ser una lista de cadenas o lista de cadenas con claves para una mejor legibilidad. Consulte las páginas del manual rrd graph para conocer la lista de opciones disponibles.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ejemplo de RRDGraph::setOptions

```
<?php
$graphObj->setOptions(array(
    "--start" => "920804400",
    "--end" => 920808000,
    "--vertical-label" => "m/s",
    "DEF:myspeed=$rrdFile:speed:AVERAGE",
    "CDEF:realspeed=myspeed,1000,*",
    "LINE2:realspeed#FF0000"
));
?>

    
```php

Establecer varias opciones de color

```
<?php
$graphObj->setOptions(array(
    "--start" => "920804400",
    "--end" => 920808000,
    "--vertical-label" => "m/s",
    "--color=BACK#00000000",
    "--color=GRID#00000000",
    "--color=MGRID#00000000",
    "DEF:myspeed=$rrdFile:speed:AVERAGE",
    "CDEF:realspeed=myspeed,1000,*",
    "LINE2:realspeed#FF0000"
));
?>

   
```php

No emplee la sintaxis de valor de clave para la misma opción rrd. Es más legible, pero no fucniona.

```
<?php
$graphObj->setOptions(array(
    "--color" => "BACK#00000000",
    "--color" => "GRID#00000000",
    "--color" => "MGRID#00000000"
));
?>

   
```php

En PHP es lo mismo que

```
<?php
$graphObj->setOptions(array(
    "--color" => "MGRID#00000000"
));
?>

   
```php
