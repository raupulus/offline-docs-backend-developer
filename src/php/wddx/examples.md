---
title: Ejemplos
source_url: https://www.php.net/manual/es/wddx.examples.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wddx/examples.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wddx
translation_status: ready
translation_revision: 99d758bd2
order: 101190
---

## Ejemplos

## Ejemplos WDDX

Todas las funciones que serializan variables utilizan el primer elemento de un array para determinar si el array debe ser serializado en un array o en una estructura. Si el primer elemento tiene una cadena de caracteres como clave, entonces será serializado en una estructura, de lo contrario, en un array.

Serialización de un valor simple con WDDX

```php
<?php
echo wddx_serialize_value("PHP to WDDX packet example", "PHP packet");
?>

   
```

Este ejemplo mostrará:

    <wddxPacket version='1.0'><header comment='PHP packet'/><data>
    <string>PHP to WDDX packet example</string></data></wddxPacket>

Uso de paquetes incrementales con WDDX

```php
<?php
$pi = 3.1415926;
$packet_id = wddx_packet_start("PHP");
wddx_add_vars($packet_id, "pi");

/* Supongamos que $cities proviene de una base de datos */
$cities = array("Austin", "Novato", "Seattle");
wddx_add_vars($packet_id, "cities");

$packet = wddx_packet_end($packet_id);
echo $packet;
?>

   
```

Este ejemplo mostrará:

    <wddxPacket version='1.0'><header comment='PHP'/><data><struct>
    <var name='pi'><number>3.1415926</number></var><var name='cities'>
    <array length='3'><string>Austin</string><string>Novato</string>
    <string>Seattle</string></array></var></struct></data></wddxPacket>

> [!NOTE]
> Los strings deben estar codificados en UTF-8; para manejar otros juegos de caracteres, convierta primero el string utilizando `mb_convert_encoding`, UConverter::transcode, o `iconv`.
