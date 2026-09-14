---
title: ZipArchive::addGlob
description: Añadir ficheros de un directorio mediante un patrón glob
source_url: https://www.php.net/manual/es/ziparchive.addglob.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/zip/ziparchive/addglob.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: zip
translation_status: ready
translation_reviewed: false
translation_revision: 963af75fa
order: 108170
---

ZipArchive::addGlob

Añadir ficheros de un directorio mediante un patrón glob

## Descripción

```php
public ZipArchive::addGlob(string $pattern, [int $flags], [array $options]): array
```php

Añade ficheros de un directorio que corresponde con el patrón global `pattern`.

> [!NOTE]
> Para una portabilidad máxima, se recomienda siempre utilizar barras oblicuas (`/`) como separador de directorio en los nombres de archivos zip.

## Parámetros

`pattern`  
Un patrón `glob`contra el cual se hará la correspondencia con los ficheros.

`flags`  
Una máscara de un bit de marcas `glob()`.

`options`  
Un array asociativo de opciones. Las opciones disponibles son:

- `"add_path"`

  Prefijo a indicar cuando se traduce la ruta de acceso del fichero dentro del archivo. Esta traducción se aplica después de cualquier operación de eliminación definida por las opciones `"remove_path"` o `"remove_all_path"`.

- `"remove_path"`

  Prefijo para eliminar la ruta de acceso de los ficheros antes de añadirlos al archivo.

- `"remove_all_path"`

  `true` para utilizar únicamente el nombre del fichero y añadirlo a la raíz del archivo.

- `"flags"`

  Máscara de bits compuesta por `ZipArchive::FL_OVERWRITE`, `ZipArchive::FL_ENC_GUESS`, `ZipArchive::FL_ENC_UTF_8`, `ZipArchive::FL_ENC_CP437`, `ZipArchive::FL_OPEN_FILE_NOW`. El comportamiento de estas constantes se describe en la página de [constantes ZIP](#zip.constants).

- `"comp_method"`

  Método de compresión, una de las constantes `ZipArchive::CM_*`, ver la página de [constantes ZIP](#zip.constants).

- `"comp_flags"`

  Nivel de compresión.

- `"enc_method"`

  Método de cifrado, una de las constantes `ZipArchive::EM_*`, ver la página de [constantes ZIP](#zip.constants).

- `"enc_password"`

  Contraseña utilizada para el cifrado.

## Valores devueltos

Un `array` de archivos añadidos en caso de éxito o `false` si ocurre un error

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0, PECL zip 1.18.0 | Se añadió `"flags"` en `options`. |
| 8.0.0, PECL zip 1.18.1 | Se añadieron `"comp_method"`, `"comp_flags"`, `"enc_method"` y `"enc_password"` en `options`. |
| 8.3.0, PECL zip 1.22.1 | Se añadió `ZipArchive::FL_OPEN_FILE_NOW`. |

## Ejemplos

Ejemplo con ZipArchive::addGlob

Añadir todos los ficheros de scripts y texto php del directorio de trabajo actual

```
<?php
$zip = new ZipArchive();
$ret = $zip->open('application.zip', ZipArchive::CREATE | ZipArchive::OVERWRITE);
if ($ret !== TRUE) {
    printf('Erróneo con el código %d', $ret);
} else {
    $options = array('add_path' => 'sources/', 'remove_all_path' => TRUE);
    $zip->addGlob('*.{php,txt}', GLOB_BRACE, $options);
    $zip->close();
}
?>

   
```php

## Véase también

ZipArchive::addFile, ZipArchive::addPattern
