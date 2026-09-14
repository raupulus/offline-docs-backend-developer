---
title: dio_seek
description: Salta a una posición del descriptor de fichero desde donde proceda
source_url: https://www.php.net/manual/es/function.dio-seek.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-seek.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_revision: 96c9d88ba
order: 11890
---

dio_seek

Salta a una posición del descriptor de fichero desde donde proceda

## Descripción

```php
dio_seek(resource $fd, int $pos, [int $whence]): int
```php

`dio_seek` se usa para cambiar la posición del fichero del descriptor de fichero proporcionado.

## Parámetros

`fd`  
Descriptor de fichero devuelto por `dio_open`.

`pos`  
Nueva posición.

`whence`  
Indica cómo interpretar la posición `pos`:

- `SEEK_SET` (por omisión) - indica que `pos` se contabiliza a partir del comienzo del fichero.

- `SEEK_CUR` - indica que `pos` se contabiliza a partir de la posición actual del fichero. Este valor puede ser positivo o negativo.

- `SEEK_END` - Indica que `pos` contabiliza caracteres a partir del final del fichero. Un valor negativo especifica una posición perteneciente al contenido del fichero; un valor positivo especifica una posición que supera el final. Si éste fuera el caso, y se escribieran datos, se rellenaría el fichero con ceros hasta alcanzar la posición que proceda.

## Valores devueltos

## Ejemplos

Posicionamiento de un fichero

```
<?php

$fd = dio_open('/dev/ttyS0', O_RDWR);

dio_seek($fd, 10, SEEK_SET);
// la posición está a 10 caracteres del comienzo

dio_seek($fd, -2, SEEK_CUR);
// la posición está a 8 caracteres del comienzo

dio_seek($fd, -5, SEEK_END);
// la posición está a 5 caracteres del final

dio_seek($fd, 10, SEEK_END);
// la posición supera ahora 10 caracteres del final del fichero.
// Los 10 caracteres intermedios entre el final y la posición actual
// se rellenan con ceros.

dio_close($fd);
?>

    
```php
