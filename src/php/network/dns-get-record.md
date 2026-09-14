---
title: dns_get_record
description: Lee los datos DNS asociados a un host
source_url: https://www.php.net/manual/es/function.dns-get-record.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/dns-get-record.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: false
translation_revision: 525aa5f19
order: 56260
---

dns_get_record

Lee los datos DNS asociados a un host

## Descripción

```php
dns_get_record(string $hostname, [int $type], [array $authoritative_name_servers], [array $additional_records], [bool $raw]): array
```php

Lee los datos DNS asociados al host `hostname`.

## Parámetros

`hostname`  
`hostname` debe ser un nombre de host DNS válido, como `www.example.com`. Las resoluciones inversas pueden realizarse con la notación `in-addr.arpa`, pero la función `gethostbyaddr` es más eficiente para realizar resoluciones inversas.

> [!NOTE]
> En términos de estándares DNS, las direcciones de correo electrónico se proporcionan en el formato `usuario.host` (por ejemplo: `webmaster.example.com` en lugar del formato `webmaster@example.com`). No se debe olvidar verificar esta dirección y modificarla si es necesario antes de pasarla a la función `mail`.

`type`  
Por omisión, `dns_get_record` buscará todos los recursos asociados a `hostname`. Para limitar la consulta, se debe utilizar una de las constantes `DNS_*`.

`authoritative_name_servers`  
Pasado por referencia, y, si se proporciona, recibirá los registros de recursos para los *Authoritative Name Servers*.

`additional_records`  
Pasado por referencia, y, si se proporciona, recibirá todos los *registros adicionales*.

`raw`  
El `type` será interpretado como un ID de tipo DNS sin tratar (no se pueden utilizar las constantes `DNS_*`). El valor de retorno contendrá una clave `data`, que debe ser analizada manualmente.

## Valores devueltos

dns_get_record retorna un array de arrays asociativos, o `false` si ocurre un error. Cada array contiene *como mínimo* los índices siguientes:

| Atributo | Significado |
|----|----|
| host | El registro del espacio de nombres DNS que es descrito por los otros datos. |
| class | `dns_get_record` solo retorna la clase de registro Internet y, como tal, este índice siempre valdrá `IN`. |
| type | String que contiene el tipo de registro. Los atributos adicionales también estarán disponibles en el array según el valor de este tipo. Consulte la tabla a continuación. |
| ttl | `"Time To Live"`: duración antes de la expiración del registro. Este valor es *diferente* de la duración original antes de la expiración, sino que es este valor menos la duración desde la última consulta al servidor DNS responsable. |

Atributos básicos DNS

| Tipo | Valor adicional |
|----|----|
| `A` | `ip`: una dirección IPv4, en formato numérico. |
| `MX` | `pri`: prioridad del servidor de correo. Los números bajos indican una prioridad alta. `target`: FQDN del servidor de correo. Ver también `dns_get_mx`. |
| `CNAME` | `target`: FQDN del nombre del espacio DNS que sirve como alias para este registro. |
| `NS` | `target`: FQDN del nombre del servidor que es responsable de este nombre de dominio. |
| `PTR` | `target`: nombre de dominio al que apunta este registro. |
| `TXT` | `txt`: string asociado arbitrariamente a este registro. |
| `HINFO` | `cpu`: número IANA que designa el procesador de la máquina referenciada por este registro. `os`: número IANA que designa el sistema operativo de la máquina referenciada por este registro. Ver [`Operating System Names`](http://www.iana.org/assignments/operating-system-names) para conocer el significado de estos valores. |
| `CAA` | `flags`: Un campo de bits de un octeto: actualmente solo el bit 0 está definido, significando 'critical' (crítico); los otros bits están reservados y deben ser ignorados. `tag`: El nombre del tag CAA (string alfanumérico ASCII). `value`: El valor del tag CAA (string binario, puede utilizar subformatos). Para más información ver: [RFC 6844](https://datatracker.ietf.org/doc/html/rfc6844) |
| `SOA` | `mname`: FQDN de la fuente de este registro. `rname`: dirección de correo electrónico del contacto administrativo de este dominio. `serial`: número de serie del nombre de dominio. `refresh`: intervalo de actualización (en segundos) que los servidores de nombres secundarios deben utilizar para almacenar en caché este nombre de dominio. `retry`: duración (en segundos) de espera después de una actualización fallida, antes de hacer un segundo intento. `expire`: duración máxima (en segundos) de conservación de una copia de los datos de zona sin poder hacer una actualización. `minimum-ttl`: duración mínima (en segundos) durante la cual un cliente conserva datos de zona antes de que envíe una nueva consulta. Esta configuración puede ser anulada por otros registros. |
| `AAAA` | `ipv6`: dirección IPv6 |
| `A6` | `masklen`: longitud (en octetos) a heredar desde el objetivo especificado por `chain`. `ipv6`: dirección para que este registro específico se fusione con `chain`. `chain`: el registro padre a fusionar con los datos `ipv6`. |
| `SRV` | `pri`: (prioridad) las prioridades más bajas deben ser utilizadas primero. `weight`: clasificación para elegir aleatoriamente entre los servidores `targets`. `target` y `port`: nombre de host y puerto donde el servicio está disponible. Para más información, ver: [RFC 2782](https://datatracker.ietf.org/doc/html/rfc2782) |
| `NAPTR` | `order` y `pref`: equivalente a `pri` y `weight` arriba. `flags`, `services`, `regex`, y `replacement`: parámetros como se definen en la [RFC 2915](https://datatracker.ietf.org/doc/html/rfc2915). |

Otros índices disponibles según el tipo DNS

## Historial de cambios

| Versión       | Descripción                                   |
|---------------|-----------------------------------------------|
| 7.0.16, 7.1.2 | Se agregó soporte para registros de tipo CAA. |

## Ejemplos

Ejemplo con `dns_get_record`

```
<?php
$result = dns_get_record("php.net");
print_r($result);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [host] => php.net
                [type] => MX
                [pri] => 5
                [target] => pair2.php.net
                [class] => IN
                [ttl] => 6765
            )

        [1] => Array
            (
                [host] => php.net
                [type] => A
                [ip] => 64.246.30.37
                [class] => IN
                [ttl] => 8125
            )

    )

Ejemplo con `dns_get_record` y DNS_ANY

Como es muy común buscar la IP de un servidor, una vez que el campo MX ha sido resuelto, `dns_get_record` retornará también un array en el parámetro `additional_records` que contendrá los registros asociados. `authoritative_name_servers` también es retornado conteniendo una lista de los servidores de autoridad.

```
<?php
/* Solicita todos ("ANY") los registros para php.net,
   luego crea los arrays $authns y $addtl
   conteniendo una lista de nombres de servidores, y todos
   los registros que van con ellos
   */
$result = dns_get_record("php.net", DNS_ANY, $authns, $addtl);
echo "Result = ";
print_r($result);
echo "Auth NS = ";
print_r($authns);
echo "Additional = ";
print_r($addtl);
?>

    
```php

Resultado del ejemplo anterior es similar a:

    Result = Array
    (
        [0] => Array
            (
                [host] => php.net
                [type] => MX
                [pri] => 5
                [target] => pair2.php.net
                [class] => IN
                [ttl] => 6765
            )

        [1] => Array
            (
                [host] => php.net
                [type] => A
                [ip] => 64.246.30.37
                [class] => IN
                [ttl] => 8125
            )

    )
    Auth NS = Array
    (
        [0] => Array
            (
                [host] => php.net
                [type] => NS
                [target] => remote1.easydns.com
                [class] => IN
                [ttl] => 10722
            )

        [1] => Array
            (
                [host] => php.net
                [type] => NS
                [target] => remote2.easydns.com
                [class] => IN
                [ttl] => 10722
            )

        [2] => Array
            (
                [host] => php.net
                [type] => NS
                [target] => ns1.easydns.com
                [class] => IN
                [ttl] => 10722
            )

        [3] => Array
            (
                [host] => php.net
                [type] => NS
                [target] => ns2.easydns.com
                [class] => IN
                [ttl] => 10722
            )

    )
    Additional = Array
    (
        [0] => Array
            (
                [host] => pair2.php.net
                [type] => A
                [ip] => 216.92.131.5
                [class] => IN
                [ttl] => 6766
            )

        [1] => Array
            (
                [host] => remote1.easydns.com
                [type] => A
                [ip] => 64.39.29.212
                [class] => IN
                [ttl] => 100384
            )

        [2] => Array
            (
                [host] => remote2.easydns.com
                [type] => A
                [ip] => 212.100.224.80
                [class] => IN
                [ttl] => 81241
            )

        [3] => Array
            (
                [host] => ns1.easydns.com
                [type] => A
                [ip] => 216.220.40.243
                [class] => IN
                [ttl] => 81241
            )

        [4] => Array
            (
                [host] => ns2.easydns.com
                [type] => A
                [ip] => 216.220.40.244
                [class] => IN
                [ttl] => 81241
            )

    )

## Véase también

`dns_get_mx`, `dns_check_record`
