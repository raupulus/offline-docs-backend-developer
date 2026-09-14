---
title: SplFileInfo::openFile
description: Obtiene un objeto SplFileObject para el fichero
source_url: https://www.php.net/manual/es/splfileinfo.openfile.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileinfo/openfile.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_reviewed: false
translation_revision: d51166ca1
order: 84260
---

SplFileInfo::openFile

Obtiene un objeto SplFileObject para el fichero

## Descripción

```php
public SplFileInfo::openFile([string $mode], [bool $useIncludePath], [resource $context]): SplFileObject
```php

Crea un `SplFileObject` `object` de el fichero. Esto es útil porque `SplFileObject` contiene otros métodos para manipular el fichero mientras que `SplFileInfo` sólo es útil para obtener información, por ejemplo si el fichero tiene permisos de escritura.

## Parámetros

`mode`  
El modo para abrir el fichero. Véase la documentación de `fopen` para una descripción de los posibles modos. Por omisión es de sólo lectura.

`useIncludePath`  
Cuando está definido como `true`, el nombre del archivo también es buscado en [include_path](#ini.include-path)

`context`  
Consulte la sección [contexto](#context) de este manual para una descripción de los `contexts`.

## Valores devueltos

El fichero abierto como un `objeto` `SplFileObject`.

## Errores/Excepciones

Lanza una `RuntimeException` si el fichero no se puede abrir (p.ej. permisos insuficientes).

## Historial de cambios

| Versión | Descripción                  |
|---------|------------------------------|
| 8.0.0   | `context` es ahora anulable. |

## Ejemplos

Ejemplo de SplFileInfo::openFile

```
<?php
$fileinfo = new SplFileInfo('/tmp/foo.txt');

if ($fileinfo->isWritable()) {

    $fileobj = $fileinfo->openFile('a');

    $fileobj->fwrite("Añadiendo este texto de prueba");
}
?>

    
```php

## Véase también

`SplFileObject`, `stream_context_create`, `fopen`
