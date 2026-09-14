---
title: xdiff_file_rabdiff
description: Hacer una diferencia binaria de dos archivos utilizando el algoritmo
  polinomial de huella digital (fingerprinting) de Rabin
source_url: https://www.php.net/manual/es/function.xdiff-file-rabdiff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xdiff/functions/xdiff-file-rabdiff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xdiff
translation_status: ready
translation_reviewed: false
translation_revision: 14af302c9
order: 102170
---

xdiff_file_rabdiff

Hacer una diferencia binaria de dos archivos utilizando el algoritmo polinomial de huella digital (fingerprinting) de Rabin

## Descripción

```php
xdiff_file_rabdiff(string $old_file, string $new_file, string $dest): bool
```php

Hace una diferencia binaria de dos archivos y almacena el resultado en un archivo de revisión. La diferencia entre esta función y `xdiff_file_bdiff` es el diferente algoritmo que se utiliza que debería traducirse en una ejecución más rápida y un diff producido menor. Esta función trabaja con archivos de texto y binarios. El archivo parche resultante puede ser posteriormente aplicado utilizando `xdiff_file_bpatch`/`xdiff_string_bpatch`.

Para obtener más información sobre las diferencias entre el algoritmo utilizado por favor vea el sitio web [libxdiff](http://www.xmailserver.org/xdiff-lib.html)

## Parámetros

`old_file`  
Ruta a el primer archivo. Este archivo actúa como "viejo" archivo.

`new_file`  
Ruta a el segundo archivo. Este archivo actúa como "nuevo" archivo.

`dest`  
Ruta de el archivo parche resultante. El archivo resultante contiene diferencias entre los archivos "viejo" y "nuevo". Este será en formato binario y no legible por humanos.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de `xdiff_file_rabdiff`

El siguiente código hace una diferencia binaria de dos archivos.

```
<?php
$old_version = 'my_script_1.0.tgz';
$new_version = 'my_script_1.1.tgz';

xdiff_file_rabdiff($old_version, $new_version, 'my_script.bdiff');
?>

    
```php

## Notas

> [!NOTE]
> Ambos archivos serán cargados en memoria así que asegúrese que el valor de memory_limit es lo suficientemente alto.

## Véase también

`xdiff_file_bpatch`
