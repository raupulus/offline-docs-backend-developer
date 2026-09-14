---
title: headers_sent
description: Indica si los encabezados HTTP ya han sido enviados
source_url: https://www.php.net/manual/es/function.headers-sent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/headers-sent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: b4989f5c1
order: 56410
---

headers_sent

Indica si los encabezados HTTP ya han sido enviados

## Descripción

```php
headers_sent([string $filename], [int $line]): bool
```php

Verifica si los encabezados HTTP ya han sido enviados.

No es posible enviar más encabezados con la función `header` una vez que el bloque de encabezados ha sido cerrado. Mediante esta función, se puede al menos evitar la visualización de los errores HTTP relacionados. Otra opción consiste en utilizar el [control de salida](#ref.outcontrol).

## Parámetros

`filename`  
Si los argumentos opcionales `filename` y `line` son proporcionados, `headers_sent` va a colocar el nombre del archivo fuente y el número de línea que iniciaron la salida, en las variables `filename` y `line`.

> [!NOTE]
> Si la salida comenzó antes de la ejecución del archivo fuente PHP (por ejemplo debido a un error de inicio), el argumento `nombre del archivo` será definido como una cadena vacía.

`line`  
El número de línea donde ocurrió la salida.

## Valores devueltos

`headers_sent` devuelve `false` si ningún encabezado ha sido enviado, o `true` en caso contrario.

## Ejemplos

Ejemplo con `headers_sent`

```
<?php

// Si ningún encabezado ha sido enviado, enviemos uno
if (!headers_sent()) {
    header('Location: http://www.example.com/');
    exit;
}

// Aquí hay un ejemplo de uso de los argumentos opcionales de archivo y línea.
// Tenga en cuenta que $filename y $linenum son transmitidos para su uso posterior.
// No los asigne antes de utilizarlos.
if (!headers_sent($filename, $linenum)) {
    header('Location: http://www.example.com/');
    exit;

// Probablemente se generará un error aquí
} else {

   echo "Los encabezados ya han sido enviados, desde el archivo $filename en la línea $linenum\n" .
   "Por lo tanto, no es posible redirigirlo automáticamente, así que por favor
   haga clic <a href=\"http://www.example.com\">aquí</a>.\n";
   exit;
}

?>

    
```php

## Notas

> [!NOTE]
> Los encabezados solo serán accesibles y se mostrarán cuando se utilice un SAPI que los soporte.

## Véase también

`ob_start`, `trigger_error`, `headers_list`, `header` para más detalles sobre los aspectos.
