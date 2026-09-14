---
title: mkdir
description: Crea un directorio
source_url: https://www.php.net/manual/es/function.mkdir.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/mkdir.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_revision: 6b48028ae
order: 23870
---

mkdir

Crea un directorio

## Descripción

```php
mkdir(string $directory, [int $permissions], [bool $recursive], [resource $context]): bool
```php

Intenta crear el directorio especificado por `directory`.

## Parámetros

`directory`  
La ruta del directorio.

> [!TIP]
> Puede utilizar una URL como nombre de archivo con esta función, si el [gestor fopen](#ini.allow-url-fopen) ha sido activado. Véase `fopen` para más detalles sobre cómo especificar el nombre del archivo. Consulte [???](#wrappers) para más información sobre las capacidades de los diferentes gestores, las notas sobre su uso, así como la información sobre las variables predefinidas que proporcionan.

`permissions`  
El modo predeterminado es 0777, lo que significa el acceso más amplio posible. Para más información sobre los modos, lea los detalles en la página de `chmod`.

> [!NOTE]
> `permissions` es ignorado en Windows.

Observe que probablemente se quiera especificar el modo como un número octal, lo que significa que debería de haber un cero inicial. El modo es modificado también por la actual máscara de usuario, la cual se puede cambiar usando `umask`.

`recursive`  
Si el valor es `true`, entonces cualquier directorio padre del directorio especificado en el parámetro `directory` también será creado, con los mismos permisos.

`context`  
Un [contexto de flujo](#stream.contexts) de tipo `resource`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!NOTE]
> Si el directorio a crear ya existe, se considerará un error y se devolverá `false`. Utilice `is_dir` o `file_exists` para comprobar si el directorio ya existe antes de intentar crearlo.

## Errores/Excepciones

Emite un error de nivel `E_WARNING` si el directorio ya existe.

Emite un error de nivel `E_WARNING` si los permisos relevantes impiden crear el directorio.

## Ejemplos

Ejemplo de `mkdir`

```
<?php
mkdir("/ruta/a/mi/directorio", 0700);
?>

    
```php

`mkdir` usando el parámetro `recursive`

```
<?php
// Estructura de la carpeta deseada
$estructura = './nivel1/nivel2/nivel3/';

// Para crear una estructura anidada se debe especificar
// el parámetro $recursive en mkdir().

if(!mkdir($estructura, 0777, true)) {
    die('Fallo al crear las carpetas...');
}

// ...
?>

    
```php

## Véase también

`is_dir`, `rmdir`, `umask`
