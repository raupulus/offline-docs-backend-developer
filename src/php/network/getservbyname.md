---
title: getservbyname
description: Devuelve el número de puerto asociado a un servicio de Internet y un
  protocolo
source_url: https://www.php.net/manual/es/function.getservbyname.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/getservbyname.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 0c9c2dd66
order: 56350
---

getservbyname

Devuelve el número de puerto asociado a un servicio de Internet y un protocolo

## Descripción

```php
getservbyname(string $service, string $protocol): int
```php

`getservbyname` devuelve el número de puerto asociado al servicio `service` y al protocolo `protocol`, como en `/etc/services`.

## Parámetros

`service`  
El nombre del servicio de Internet, en forma de `string`.

`protocol`  
`protocol` puede ser `"tcp"` o `"udp"` (en minúsculas).

## Valores devueltos

Devuelve el número del puerto, o `false` si `service` o `protocol` no se encuentra.

## Ejemplos

Ejemplo con `getservbyname`

```
<?php
$services = array('http', 'ftp', 'ssh', 'telnet', 'imap',
'smtp', 'nicname', 'gopher', 'finger', 'pop3', 'www');

foreach ($services as $service) {
    $port = getservbyname($service, 'tcp');
    echo $service . ": " . $port . "<br />\n";
}
?>

    
```php

## Véase también

`getservbyport`, <http://www.iana.org/assignments/port-numbers> para una lista completa de los números de puerto.
