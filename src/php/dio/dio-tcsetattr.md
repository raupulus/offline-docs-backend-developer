---
title: dio_tcsetattr
description: Establece los atributos de terminal y la velocidad de transmisión para
  un puerto serie
source_url: https://www.php.net/manual/es/function.dio-tcsetattr.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dio/functions/dio-tcsetattr.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dio
translation_status: ready
translation_reviewed: false
translation_revision: ee1ce6a0e
order: 11910
---

dio_tcsetattr

Establece los atributos de terminal y la velocidad de transmisión para un puerto serie

## Descripción

```php
dio_tcsetattr(resource $fd, array $options): bool
```php

`dio_tcsetattr` establece los atributos de terminal y la velocidad de transmisión del `fd` abierto.

## Parámetros

`fd`  
El descriptor de fichero devuelto por `dio_open`.

`options`  
Las opciones disponibles actualmente son:

- 'baud' - velocidad de transmisión del puerto - puede ser 38400,19200,9600,4800,2400,1800, 1200,600,300,200,150,134,110,75 o 50, el valor por omisión es 9600.

- 'bits' - bits de datos - puede ser 8,7,6 o 5. El valor por omisión es 8.

- 'stop' - bits de parada - puede ser 1 o 2. El valor por omisión es 1.

- 'parity' - puede ser 0,1 o 2. El valor por omisión es 0.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Establecer la velocidad de transmisión en un puerto serie

```
<?php

$fd = dio_open('/dev/ttyS0', O_RDWR | O_NOCTTY | O_NONBLOCK);

dio_fcntl($fd, F_SETFL, O_SYNC);

dio_tcsetattr($fd, array(
    'baud' => 9600,
    'bits' => 8,
    'stop'  => 1,
    'parity' => 0
));

while (true) {
    $data = dio_read($fd, 256);
    if ($data !== null && $data !== '') {
        echo $data;
    }
}

?>

   
```php

## Notas

> [!NOTE]
> Esta función no está implementada en las plataformas Windows.
