---
title: svn_checkout
description: Extrae una copia de trabajo desde un repositorio
source_url: https://www.php.net/manual/es/function.svn-checkout.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-checkout.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: true
translation_revision: 997700a58
order: 89930
---

svn_checkout

Extrae una copia de trabajo desde un repositorio

## Descripción

```php
svn_checkout(string $repos, string $targetpath, [int $revision], [int $flags]): bool
```php

Extrae una copia de trabajo desde el repositorio `repos` hacia `targetpath` en la revisión `revision`.

## Parámetros

`repos`  
URL del directorio en el repositorio a extraer.

`targetpath`  
Ruta local del directorio en el cual se realiza la extracción

> [!NOTE]
> Los caminos relativos pueden ser resueltos si el directorio de trabajo actual es uno de los que contienen el binario PHP. Para utilizar el directorio de trabajo, utilice la función `realpath`, o la instrucción dirname(\_\_FILE\_\_).

`revision`  
Número de revisión del repositorio a extraer. Por omisión, es HEAD, la revisión más reciente.

`flags`  
Cualquier combinación de `SVN_NON_RECURSIVE` y `SVN_IGNORE_EXTERNALS`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo de uso

Este ejemplo muestra cómo extraer un directorio desde un repositorio hacia un directorio llamado `"calc"`:

```
<?php
svn_checkout('http://www.example.com/svnroot/calc/trunk', dirname(__FILE__) . '/calc');
?>

   
```php

El uso de `dirname(__FILE__)` es necesario para convertir la ruta relativa del directorio calc en una ruta absoluta. Si calc existe, asimismo se puede utilizar `realpath` para obtener una ruta absoluta.

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.

## Véase también

svn_add

svn_commit

svn_status

svn_update

Documentación SVN sobre el comando

"svn checkout"
