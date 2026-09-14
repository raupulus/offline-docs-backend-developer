---
title: stream_filter_register
description: Registra un filtro de flujo
source_url: https://www.php.net/manual/es/function.stream-filter-register.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-filter-register.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 87930
---

stream_filter_register

Registra un filtro de flujo

## Descripción

```php
stream_filter_register(string $filter_name, string $class): bool
```php

`stream_filter_register` permite implementar un filtro de flujo personalizado, para ser utilizado con las funciones de acceso a datos externos (como `fopen`, `fread`, etc.).

## Parámetros

`filter_name`  
El nombre del filtro a registrar.

`class`  
Para crear una clase de filtro, se debe definir una clase que extienda la clase `php_user_filter`. Al realizar operaciones de lectura y escritura en el flujo al que esté adjunto el filtro, PHP pasará los datos a través del filtro (y de todos los otros filtros adjuntos), de manera que los datos sean modificados según lo deseado. Se deben implementar los métodos tal como se describe en `php_user_filter`, de lo contrario se producirán comportamientos indefinidos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

`stream_filter_register` debe devolver siempre `false` si el parámetro `filter_name` ya está definido.

## Ejemplos

Filtro de letras mayúsculas en el flujo `foo-bar.txt`

El ejemplo siguiente implementa un filtro llamado `strtoupper`, en el flujo `foo-bar.txt`, que convierte a mayúsculas todas las letras escritas/leídas desde este flujo.

```
<?php

/* Definición de la clase */
class strtoupper_filter extends php_user_filter {
  function filter($in, $out, &$consumed, $closing)
  {
    while ($bucket = stream_bucket_make_writeable($in)) {
      $bucket->data = strtoupper($bucket->data);
      $consumed += $bucket->datalen;
      stream_bucket_append($out, $bucket);
    }
    return PSFS_PASS_ON;
  }
}

/* Registro de nuestro filtro con PHP */
stream_filter_register("strtoupper", "strtoupper_filter")
    or die("Error al registrar el filtro");

$fp = fopen("foo-bar.txt", "w");

/* Adjuntar el filtro registrado al flujo que acabamos de abrir */
stream_filter_append($fp, "strtoupper");

fwrite($fp, "Línea1\n");
fwrite($fp, "Palabra - 2\n");
fwrite($fp, "Fácil como 123\n");

fclose($fp);

/* Lectura del contenido */
readfile("foo-bar.txt");

?>

    
```php

El ejemplo anterior mostrará:

    LÍNEA1
    PALABRA - 2
    FÁCIL COMO 123

Registro de una clase de filtro genérica para coincidir con múltiples nombres de filtros

```
<?php

/* Definición de la clase */
class string_filter extends php_user_filter {
  var $mode;

  function filter($in, $out, &$consumed, $closing)
  {
    while ($bucket = stream_bucket_make_writeable($in)) {
      if ($this->mode == 1) {
        $bucket->data = strtoupper($bucket->data);
      } elseif ($this->mode == 0) {
        $bucket->data = strtolower($bucket->data);
      }

      $consumed += $bucket->datalen;
      stream_bucket_append($out, $bucket);
    }
    return PSFS_PASS_ON;
  }

  function onCreate()
  {
    if ($this->filtername == 'str.toupper') {
      $this->mode = 1;
    } elseif ($this->filtername == 'str.tolower') {
      $this->mode = 0;
    } else {
      /* Se solicitan algunos otros filtros str.*, manejo del error con PHP */
      return false;
    }

    return true;
  }
}

/* Registro de nuestro filtro con PHP */
stream_filter_register("str.*", "string_filter")
    or die("Error al registrar el filtro");

$fp = fopen("foo-bar.txt", "w");

/* Adjuntar el filtro registrado al flujo que acabamos de abrir
    Podemos alternativamente pasar a str.tolower aquí */
stream_filter_append($fp, "str.toupper");

fwrite($fp, "Línea1\n");
fwrite($fp, "Palabra - 2\n");
fwrite($fp, "Fácil como 123\n");

fclose($fp);

/* Lectura del contenido */
readfile("foo-bar.txt");

?>

    
```php

El ejemplo anterior mostrará:

    LÍNEA1
    PALABRA - 2
    FÁCIL COMO 123

## Véase también

`stream_wrapper_register`, `stream_filter_append`, `stream_filter_prepend`
