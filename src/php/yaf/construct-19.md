---
title: Yaf_View_Simple::__construct
description: El constructor de Yaf_View_Simple
source_url: https://www.php.net/manual/es/yaf-view-simple.construct.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaf/yaf_view_simple/construct.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaf
translation_status: ready
translation_revision: b37bddfde
order: 107260
---

Yaf_View_Simple::\_\_construct

El constructor de Yaf_View_Simple

## Descripción

```php
final public Yaf_View_Simple::__construct(string $template_dir, [array $options])
```php

## Parámetros

`template_dir`  
El directorio base de las plantillas, por omisión es APPLICATOIN . "/views" para Yaf.

`options`  
Opciones para el motor, a partir de Yaf 2.1.13, se pueden usar etiquetas cortas "\<?=\$var?\>" en las plantillas (sin tener en cuenta "short_open_tag"), por lo que viene una opción llamada "short_tag", se puede desactivar para prevenir el uso de short_tag en las plantillas.

## Ejemplos

Ejemplo de Yaf_View_Simple::\_\_construct

```
<?php
   define ("TEMPLATE_DIRECTORY", APPLICATOIN_PATH . '/views');
   $view = new Yaf_View_Simple(TEMPLATE_DIRECTORY, array(
                           'short_tag' => false //no se permite el uso de etiquetas cortas en las plantillas
   ));
?>

   
```php
