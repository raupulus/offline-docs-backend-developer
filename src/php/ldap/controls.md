---
title: Control LDAP
source_url: https://www.php.net/manual/es/ldap.controls.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ldap/controls.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ldap
translation_status: ready
translation_reviewed: true
translation_revision: b37727aba
order: 42940
---

## Control LDAP

Los controles son objetos especiales que pueden ser enviados con una petición LDAP para modificar el comportamiento del servidor LDAP durante la ejecución de la petición. También pueden existir controles enviados por el servidor con la respuesta para proporcionar más información, generalmente para responder a un objeto de control de la petición.

> [!NOTE]
> No todos los controles son soportados por todos los servidores LDAP. Para saber qué controles son soportados por un servidor, debe interrogarse el DSE raíz leyendo un dn vacío con el filtro (objectClass=\*).
>
> <div class="example">
>
> <div class="title">
>
> Prueba de soporte para el control de resultados paginados
>
> </div>
>
> ```
> <?php
> // $ds es un identificador de enlace válido para un servidor de directorio
> $result = ldap_read($ds, '', '(objectClass=*)', ['supportedControl']);
> if (!in_array(LDAP_CONTROL_PAGEDRESULTS, ldap_get_entries($ds, $result)[0]['supportedcontrol'])) {
>   die("Este servidor no soporta el control de resultados paginados");
> }
> ?>
>
>     
> ```
>
> </div>

Desde PHP 7.3, puede enviarse controles con la petición en todas las funciones de petición utilizando el parámetro `controls`. Cuando existe una versión extendida de una función, debe utilizarse si se desea acceder al objeto de respuesta completo y ser capaz de analizar los controles de respuesta a partir de este utilizando `ldap_parse_result`.

`controls` debe ser un array que contenga un array para cada control a enviar, conteniendo las siguientes claves :

oid (`string`)  
El OID del control. Deben utilizarse las constantes que comienzan por LDAP_CONTROL\_ para esto. Ver [constantes de LDAP](#ldap.constants).

iscritical (`bool`)  
Si un control está marcado como crítico, la petición fallará si el control no es soportado por el servidor, o si falla al ser aplicado. Tenga en cuenta que algunos controles deben siempre estar marcados como críticos como se indica en el RFC que los introduce. Por omisión a `false`.

value (`mixed`)  
Si es aplicable, el valor del control. Lea a continuación para más información.

La mayoría de los valores de control son enviados al servidor en BER-encodados. Puede BER-encodar el valor usted mismo, o puede pasar un array con las claves correctas para que el encodado sea realizado por usted. Los controles soportados para pasar como array son :

- `LDAP_CONTROL_PAGEDRESULTS` Las claves esperadas son \[size\] y \[cookie\]

- `LDAP_CONTROL_ASSERT` La clave esperada es \[assertion\]

- `LDAP_CONTROL_VALUESRETURNFILTER` La clave esperada es filter

- `LDAP_CONTROL_PRE_READ` La clave esperada es attrs

- `LDAP_CONTROL_POST_READ` La clave esperada es attrs

- `LDAP_CONTROL_SORTREQUEST` Espera un array de arrays con las claves attr, \[oid\], \[reverse\].

- `LDAP_CONTROL_VLVREQUEST` Las claves esperadas son before, after, attrvalue\|(offset, count), \[context\]

Los siguientes controles no requieren valor :

- `LDAP_CONTROL_PASSWORDPOLICYREQUEST`

- `LDAP_CONTROL_MANAGEDSAIT`

- `LDAP_CONTROL_DONTUSECOPY`

El control `LDAP_CONTROL_PROXY_AUTHZ` es un caso especial ya que su valor no se espera que esté BER-encodado, por lo que puede utilizarse directamente una cadena para su valor.

Cuando los controles son analizados por `ldap_parse_result`, los valores son transformados en array si son soportados. Esto es soportado para :

- `LDAP_CONTROL_PASSWORDPOLICYRESPONSE` Las claves son expire, grace, \[error\]

- `LDAP_CONTROL_PAGEDRESULTS` Las claves son size, cookie

- `LDAP_CONTROL_PRE_READ` Las claves son dn y los nombres de atributos LDAP

- `LDAP_CONTROL_POST_READ` Las claves son dn y los nombres de atributos LDAP

- `LDAP_CONTROL_SORTRESPONSE` Las claves son errcode, \[attribute\]

- `LDAP_CONTROL_VLVRESPONSE` Las claves son target, count, errcode, context
