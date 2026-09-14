---
title: Entradas/Salidas HTTP
source_url: https://www.php.net/manual/es/mbstring.http.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/http-inout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 95bdd6883
order: 45610
---

## Entradas/Salidas HTTP

La conversión automática de las entradas/salidas HTTP puede también convertir datos binarios. Los usuarios deben controlar las conversiones, si los datos binarios deben ser utilizados mediante HTTP.

> [!NOTE]
> Si el atributo `enctype` de la etiqueta `form` vale `multipart/form-data` y la directiva del `php.ini` está posicionada a On, las variables y los nombres de ficheros subidos mediante el método POST serán convertidos con la codificación interna. De lo contrario, la conversión no se realizará.

- Entrada HTTP

  No hay medios para controlar la conversión de caracteres HTTP en entrada, desde un script PHP. Para desactivar esta conversión, debe hacerse desde el fichero `php.ini`.

  Desactiva la conversión HTTP en el `php.ini`

```php
  ;; Desactivar la conversión de entrada HTTP
  mbstring.http_input = pass
  ;; Desactivar la conversión de entrada HTTP
  mbstring.encoding_translation = Off

        
  ```

  Cuando se utiliza PHP como módulo Apache, es posible anular la configuración del `php.ini` para cada Virtual Host en el fichero `httpd.conf` o por directorio con el fichero `.htaccess`. Consúltese la sección de [configuración](#configuration) así como el manual de Apache.

- Salidas HTTP

  Existen varios medios para activar la conversión en salida de script PHP. Uno de ellos utiliza `php.ini`, otro utiliza `ob_start` con la función `mb_output_handler` como función de retrollamada.

Ejemplo de configuración de mbstring en `php.ini`

    ;; Habilitar la conversión de codificación de caracteres en salida para todas las páginas PHP

    ;; Habilitar el búfer de salida
    output_buffering    = On

    ;; Establecer mb_output_handler para habilitar la conversión en salida
    output_handler      = mb_output_handler

Ejemplo de script con mbstring

```php
<?php

// Habilitar la conversión de codificación de caracteres en salida HTTP solo para esta página

// Establecer la codificación de caracteres en salida HTTP a SJIS
mb_http_output('SJIS');

// Iniciar el búfer y especificar "mb_output_handler" como
// función de retrollamada
ob_start('mb_output_handler');

?>

   
```
