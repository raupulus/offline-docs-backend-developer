---
title: libxml_use_internal_errors
description: Se desactiva el reporte de errores de libxml y se almacenan para su lectura
  posterior
source_url: https://www.php.net/manual/es/function.libxml-use-internal-errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/libxml/functions/libxml-use-internal-errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: libxml
translation_status: ready
translation_reviewed: true
translation_revision: f90df97fa
order: 43720
---

libxml_use_internal_errors

Se desactiva el reporte de errores de libxml y se almacenan para su lectura posterior

## Descripción

```php
libxml_use_internal_errors([bool $use_errors]): bool
```php

`libxml_use_internal_errors` permite desactivar el gestor de errores estándar de libxml y activar el propio gestor de errores.

## Parámetros

`use_errors`  
Activa (`true`) el gestor de errores del usuario o lo desactiva (`false`). La desactivación borrará también todos los errores de libxml existentes.

## Valores devueltos

`libxml_use_internal_errors` devuelve el valor previamente configurado para `use_errors`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `use_errors` ahora es nullable. Anteriormente, su valor por omisión era `false`. |

## Ejemplos

Ejemplo con `libxml_use_internal_errors`

Este ejemplo muestra el uso básico de los errores de libxml, y el valor devuelto por esta función.

```
<?php

// activa la gestión de errores personalizada
var_dump(libxml_use_internal_errors(true));

// Carga del documento
$doc = new DOMDocument;

if (!$doc->load('file.xml')) {
    foreach (libxml_get_errors() as $error) {
        // gestionar los errores aquí
    }

    libxml_clear_errors();
}

?>

    
```php

El ejemplo anterior mostrará:

    bool(false)

## Véase también

`libxml_clear_errors`, `libxml_get_errors`
