---
title: Ejemplos
source_url: https://www.php.net/manual/es/outcontrol.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: e2f2172bf
order: 59710
---

## Ejemplos

## Uso básico

Ejemplo de bufferización de salida

```php
<?php

ob_start();
echo "Bonjour\n";

setcookie("cookiename", "cookiedata");

ob_end_flush();

?>

    
```

En el ejemplo anterior, la instrucción `echo` se almacena en un buffer hasta la llamada a la función `ob_end_flush`. Al mismo tiempo, la llamada a `setcookie` ha tenido éxito en la creación de un cookie, sin generar errores. (Normalmente, los encabezados deben enviarse al navegador antes de los datos).

## Uso de la reescritura de salida

Desde PHP 7.1.0, `output_add_rewrite_var`, `output_reset_rewrite_vars` utiliza un buffer de salida dedicado. Es decir, no utiliza un buffer de salida [trans sid](#ini.session.use-trans-sid).

Ejemplo de reescritura de salida

```php
<?php
// Este código funciona con PHP 7.1.0, 7.0.10, 5.6.25 y superior.

// HTTP_HOST es el host objetivo por defecto. Definir manualmente para que el ejemplo de código funcione.
$_SERVER['HTTP_HOST'] = 'php.net';

// La reescritura de salida solo puede reescribir los form. Añadir a=href.
// Las etiquetas pueden especificarse como tag_name=url_attr, por ejemplo img=src, iframe=src
// No se permiten espacios entre los argumentos.
// La etiqueta form es una etiqueta especial que añade un campo oculto.
ini_set('url_rewriter.tags','a=href,form=');
var_dump(ini_get('url_rewriter.tags'));

// Esto se añade a la URL y al formulario
output_add_rewrite_var('test', 'value');
?>
<a href="//php.net/index.php?bug=1234">bug1234</a>
<form action="https://php.net/?bug=1234&edit=1" method="post">
 <input type="text" name="title" />
</form>

    
```

El ejemplo anterior mostrará:

    <a href="//php.net/?bug=1234&test=value">bug1234</a>
    <form action="https://php.net/?bug=1234&edit=1" method="post"><input type="hidden" name="test" value="value" />
     <input type="text" name="title" />
    </form>

Desde PHP 7.1.0, las funciones de reescritura de salida tienen sus propios parámetros INI, [url_rewriter.tags](#ini.url-rewriter.tags) y [url_rewriter.hosts](#ini.url-rewriter.hosts).
