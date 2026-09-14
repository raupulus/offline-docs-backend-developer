---
title: fseek
description: Modifica la posición del puntero de archivo
source_url: https://www.php.net/manual/es/function.fseek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/filesystem/functions/fseek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: filesystem
translation_status: ready
translation_reviewed: true
translation_revision: cc735f9ff
order: 23670
---

fseek

Modifica la posición del puntero de archivo

## Descripción

```php
fseek(resource $stream, int $offset, [int $whence]): int
```php

Modifica el cursor de posición en el archivo `stream`. La nueva posición, medida en bytes, desde el inicio del archivo, se obtiene sumando la distancia `offset` a la posición `whence`.

En general, es posible desplazarse más allá del final del flujo (eof); si se escriben datos en este caso, el espacio entre el final del flujo y la posición actual será rellenado con bytes nulos. Sin embargo, algunos flujos no soportan este comportamiento, en particular cuando el espacio de almacenamiento subyacente es de tamaño fijo.

## Parámetros

`stream`  
Un puntero al sistema de ficheros de tipo `resource` que típicamente se crea utilizando `fopen`.

`offset`  
La posición.

Para desplazarse a una posición antes del final del archivo, debe pasarse un valor negativo en el `offset` y el parámetro `whence` debe establecerse en `SEEK_END`.

`whence`  
Los valores posibles para `whence` son : `SEEK_SET` - Establecer la posición igual a `offset` bytes desde el inicio del archivo., `SEEK_CUR` - Establecer la posición en el lugar actual más `offset` bytes., `SEEK_END` - Establecer la posición al final del archivo más `offset` bytes.

## Valores devueltos

En caso de éxito, devuelve `0`; de lo contrario, devuelve `-1`.

> [!WARNING]
> Esta función ha sido creada para imitar la función del mismo nombre en lenguaje C. Tenga en cuenta los valores de retorno, ya que difieren de lo que podría esperarse en PHP.

## Ejemplos

Ejemplo con `fseek`

```
<?php

$fp = fopen('somefile.txt', 'r');

// lee algunos datos
$data = fgets($fp, 4096);

// vuelve al inicio del archivo
// equivalente a rewind($fp);
fseek($fp, 0);

?>

    
```php

## Notas

> [!NOTE]
> Si abre el archivo con el modo `a` o `a+`, todos los datos que escriba en el archivo siempre serán añadidos, sin importar la posición en el archivo.

> [!NOTE]
> No todos los flujos soportan el desplazamiento. Para aquellos que no lo soportan, el desplazamiento hacia adelante se realizará leyendo y liberando los bytes; otras formas de desplazamiento fallarán.

## Véase también

`ftell`, `rewind`
