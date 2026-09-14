---
title: com_print_typeinfo
description: Muestra una definición de clase PHP para una interfaz distribuible
source_url: https://www.php.net/manual/es/function.com-print-typeinfo.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/com/functions/com-print-typeinfo.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: com
translation_status: ready
translation_reviewed: false
translation_revision: 20216b916
order: 7730
---

com_print_typeinfo

Muestra una definición de clase PHP para una interfaz distribuible

## Descripción

```php
com_print_typeinfo(variant $variant, [string $dispatch_interface], [bool $display_sink]): bool
```php

Ayuda a generar un esqueleto de clase para usarlo como sumidero de eventos. Asimismo, puede ser utilizado para generar una copia de seguridad de cualquier objeto COM, siempre que soporte suficientes interfaces de introspección y se conozca el nombre de la interfaz que se desea mostrar.

## Parámetros

`variant`  
`variant` debe ser una instancia de un objeto COM o el nombre de una biblioteca de tipos (que debe ser resuelto de acuerdo con las reglas definidas en la función `com_load_typelib`).

`dispatch_interface`  
El nombre de una interfaz descendiente `IDispatch` que se desea mostrar.

`display_sink`  
Si se establece a `true`, se mostrará la interfaz de sumidero correspondiente en su lugar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

`com_event_sink`, `com_load_typelib`
