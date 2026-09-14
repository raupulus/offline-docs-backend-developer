---
title: LuaSandbox::getProfilerFunctionReport
description: Recupera los datos del perfilador
source_url: https://www.php.net/manual/es/luasandbox.getprofilerfunctionreport.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/luasandbox/luasandbox/getprofilerfunctionreport.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: luasandbox
translation_status: ready
translation_reviewed: false
translation_revision: 9c40251a8
order: 43970
---

LuaSandbox::getProfilerFunctionReport

Recupera los datos del perfilador

## Descripción

```php
public LuaSandbox::getProfilerFunctionReport([int $units]): array
```php

Para una instancia de perfilado previamente iniciada por LuaSandbox::enableProfiler, recupera un informe del costo de cada función.

La medición del costo se determina por el argumento `$units`:

`LuaSandbox::SAMPLES`  
Medición en número de muestras.

`LuaSandbox::SECONDS`  
Medición en segundos de tiempo CPU.

`LuaSandbox::PERCENT`  
Medición en porcentaje de tiempo CPU.

## Parámetros

`units`  
La unidad de medida constante.

## Valores devueltos

Devuelve las mediciones del perfilador, ordenadas en orden descendente, en forma de un array asociativo. Las claves son los nombres de las funciones Lua (con el fichero fuente y la línea definidos entre corchetes angulares), los valores son las mediciones en `int` o `float`.

> [!NOTE]
> En Windows, esta función siempre devuelve cero. En los sistemas operativos que no soportan `CLOCK_THREAD_CPUTIME_ID`, como FreeBSD y Mac OS X, esta función devolverá el tiempo transcurrido en el reloj, no el tiempo CPU.

## Ejemplos

Perfilado de código Lua

```
<?php

// crear un nuevo LuaSandbox
$sandbox = new LuaSandbox();

// Inicia el perfilador
$sandbox->enableProfiler( 0.01 );

// ... Ejecute código Lua aquí ...

// Recupera los datos del perfilador
$data = $sandbox->getProfilerFunctionReport();

?>

   
```php
