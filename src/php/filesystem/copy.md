---
title: copy
description: Copia un fichero
source_url: https://www.php.net/manual/es/function.copy.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/copy.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: ea62fb831
order: 23320
---

copy

Copia un fichero

## Descripción

```php
copy(string $from, string $to, [resource $context]): bool
```php

Realiza una copia del fichero `from` hacia el fichero `to`.

Si se desea mover un fichero, utilice la función `rename`.

## Parámetros

`from`  
Ruta hacia el fichero origen.

`to`  
La ruta de destino. Si `to` es una URL, la copia puede fallar si este protocolo no soporta la sobrescritura de ficheros existentes.

> [!WARNING]
> Si el fichero de destino `to` ya existe, será sobrescrito.

`context`  
Un recurso de contexto válido, creado por la función `stream_context_create`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `copy`

```
<?php
$file = 'example.txt';
$newfile = 'example.txt.bak';

if (!copy($file, $newfile)) {
    echo "La copia $file del fichero ha fallado...\n";
}
?>

    
```php

## Véase también

`move_uploaded_file`, `rename`, La sección del manual relativa a la [gestión de subidas de ficheros](#features.file-upload)
