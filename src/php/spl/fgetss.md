---
title: SplFileObject::fgetss
description: Obtiene la línea de el fichero y elimina etiquetas HTML
source_url: https://www.php.net/manual/es/splfileobject.fgetss.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/spl/splfileobject/fgetss.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: spl
translation_status: ready
translation_revision: d51166ca1
order: 84380
---

SplFileObject::fgetss

Obtiene la línea de el fichero y elimina etiquetas HTML

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.3.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
public SplFileObject::fgetss([string $allowable_tags]): string
```php

Idéntico a SplFileObject::fgets, excepto que SplFileObject::fgetss intenta eliminar las etiquetas HTML y PHP de el texto que se lee. La función mantiene el estado de análisis sintáctico de llamada a llamada, y como tal no es equivalente a la llamada `strip_tags` sobre el valor de retorno de SplFileObject::fgets.

## Parámetros

`allowable_tags`  
Parámetro opcional para especificar etiquetas que no deben ser eliminadas.

## Valores devueltos

Devuelve un string conteniendo la siguiente línea de el fichero con el código HTML y PHP eliminado, o `false` en caso de error.

## Ejemplos

Ejemplo de SplFileObject::fgetss

```
<?php
$str = <<<EOD
<html><body>
 <p>Bienvenid@! Hoy es el <?php echo(date('jS')); ?> de <?= date('F'); ?>.</p>
</body></html>
Texto fuera del bloque HTML.
EOD;
file_put_contents("ejemplo.php", $str);

$fichero = new SplFileObject("ejemplo.php");
while (!$fichero->eof()) {
    echo $fichero->fgetss();
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Bienvenid@! Hoy es el  de .

    Texto fuera del bloque HTML.

## Véase también

`fgetss`, SplFileObject::fgets, SplFileObject::fgetc, SplFileObject::current, El filtro [string.strip_tags](#filters.string.strip_tags)
