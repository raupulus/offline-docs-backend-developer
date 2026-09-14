---
title: fgetss
description: Obtiene un línea desde un puntero a un archivo y elimina las etiquetas
  HTML
source_url: https://www.php.net/manual/es/function.fgetss.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fgetss.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: false
translation_revision: cb3e68d99
order: 23450
---

fgetss

Obtiene un línea desde un puntero a un archivo y elimina las etiquetas HTML

> [!WARNING]
> Esta función está *OBSOLETA* a partir de PHP 7.3.0, y ha sido *ELIMINADA* a partir de PHP 8.0.0. Depender de esta función está altamente desaconsejado.

## Descripción

```php
fgetss(resource $handle, [int $length], [string $allowable_tags]): string
```php

Idéntica a `fgets`, excepto que `fgetss` intenta eliminar cualesquiera bytes NULL, etiquetas HTML y PHP del texto que lee.

## Parámetros

`handle`  
El puntero de fichero debe ser válido y apuntar a un archivo abierto con éxito por `fopen` o `fsockopen` (y no cerrado aún por `fclose`).

`length`  
Longitud de la información que va a ser recuperada.

`allowable_tags`  
Puede usar el tercer parámetro opcional para especificar las etiquetas que no deberían ser eliminadas. Consulte `strip_tags` para obtener más información sobre `allowable_tags`.

## Valores devueltos

Devuelve una cadena de hasta `length` - 1 bytes leídos desde el archivo apuntado por `handle`, con todo el código HTML y PHP eliminado.

Si se produjo un error devuelve `false`.

## Ejemplos

Leer un archivo PHP línea a línea

```
<?php
$cadena = <<<EOD
<html><body>
 <p>¡Bienvenido! Hoy es el <?php echo(date('jS')); ?> de <?= date('F'); ?>.</p>
</body></html>
Texto fuera del bloque HTML.
EOD;
file_put_contents('ejemplo.php', $cadena);

$gestor = @fopen("ejemplo.php", "r");
if ($gestor) {
    while (!feof($gestor)) {
        $buffer = fgetss($gestor, 4096);
        echo $buffer;
    }
    fclose($gestor);
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

     ¡Bienvenido! Hoy es el  de .

    Texto fuera del bloque HTML.

## Notas

> [!NOTE]
> Si PHP no reconoce correctamente los finales de línea al leer ficheros que han sido creados o leídos en un Macintosh, la activación de la opción de configuración [auto_detect_line_endings](#ini.auto-detect-line-endings) puede resolver el problema.

## Véase también

`fgets`, `fopen`, `popen`, `fsockopen`, `strip_tags`
