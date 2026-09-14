---
title: imap_get_quota
description: Lee los cuotas de los buzones de correo así como las estadísticas sobre
  cada uno de ellos
source_url: https://www.php.net/manual/es/function.imap-get-quota.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-get-quota.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 34892f827
order: 38150
---

imap_get_quota

Lee los cuotas de los buzones de correo así como las estadísticas sobre cada uno de ellos

## Descripción

```php
imap_get_quota(IMAP\Connection $imap, string $quota_root): array
```php

Lee los cuotas de los buzones de correo así como las estadísticas sobre cada uno de ellos.

Para una versión de usuario, no administrador, de esta función, refiérase a la función `imap_get_quotaroot`.

## Parámetros

`imap`  
Una instancia de `IMAP\Connection`.

`quota_root`  
`quota_root` debe ser de la forma : "`user.nom`", donde "nom" es el nombre del buzón de correo que se desea analizar.

## Valores devueltos

Devuelve un array que contiene los valores de cuota y actuales del buzón de correo `quota_root`. La cuota representa el tamaño máximo del buzón de correo. El valor actual es el espacio actualmente utilizado por el buzón de correo. `imap_get_quota` devolverá `false` en caso de fallo.

Desde PHP 4.3, la función refleja más fielmente las funcionalidades dictadas por la [RFC2087](https://datatracker.ietf.org/doc/html/rfc2087). El array devuelto ha cambiado para soportar un número ilimitado de recursos devueltos (i.e. mensajes o subcarpetas) con cada recurso nombrado que es identificado por una clave. Cada clave contiene entonces otro array con el uso y la cuota. El ejemplo a continuación muestra cómo utilizarlo.

Por razones de compatibilidad, el método de acceso original sigue estando disponible, pero se recomienda abandonarlo.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.1.0 | El parámetro `imap` ahora espera una instancia de `IMAP\Connection` ; anteriormente, se esperaba un `resource` `imap` válido. |

## Ejemplos

Ejemplo con `imap_get_quota`

```
<?php
$mbox = imap_open("{imap.example.org}", "mailadmin", "password", OP_HALFOPEN)
      or die("Imposible conectarse : " . imap_last_error());

$quota_value = imap_get_quota($mbox, "user.kalowsky");
if (is_array($quota_value)) {
    echo "Nivel de uso : " . $quota_value['usage'];
    echo "Cuota : " . $quota_value['limit'];
}

imap_close($mbox);
?>

    
```php

Ejemplo con `imap_get_quota` 4.3 o superior

```
<?php
$mbox = imap_open("{imap.example.org}", "mailadmin", "password", OP_HALFOPEN)
      or die("Imposible conectarse : " . imap_last_error());

$quota_values = imap_get_quota($mbox, "user.kalowsky");
if (is_array($quota_values)) {
   $storage = $quota_values['STORAGE'];
   echo "Uso actual de la capacidad de almacenamiento : " .  $storage['usage'];
   echo "Cuota actual de almacenamiento  : " .  $storage['limit'];

   $message = $quota_values['MESSAGE'];
   echo "Nivel de uso de MESSAGE  : " .  $message['usage'];
   echo "Cuota de MESSAGE : " .  $message['limit'];

   /* ...  */
}

imap_close($mbox);
?>

    
```php

## Notas

`imap_get_quota` funciona actualmente solo con las bibliotecas c-client2000.

El `imap` dado debe estar abierto como administrador de correo, de lo contrario esta función falla.

## Véase también

`imap_open`, `imap_set_quota`, `imap_get_quotaroot`
