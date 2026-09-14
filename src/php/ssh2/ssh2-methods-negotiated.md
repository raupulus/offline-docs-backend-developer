---
title: ssh2_methods_negotiated
description: Devuelve una lista de métodos negociados
source_url: https://www.php.net/manual/es/function.ssh2-methods-negotiated.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ssh2/functions/ssh2-methods-negotiated.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ssh2
translation_status: ready
translation_reviewed: false
translation_revision: 12f0e7220
order: 86540
---

ssh2_methods_negotiated

Devuelve una lista de métodos negociados

## Descripción

```php
ssh2_methods_negotiated(resource $session): array
```php

Devuelve una lista de métodos negociados.

## Parámetros

`session`  
Un identificador de conexión SSH, obtenido desde la función `ssh2_connect`.

## Valores devueltos

## Ejemplos

Determina qué métodos han sido negociados

```
<?php
$connection = ssh2_connect('shell.example.com', 22);
$methods = ssh2_methods_negotiated($connection);

echo "Clave de cifrado negociada utilizando: {$methods['kex']}\n";
echo "Identificación del servidor utilizando {$methods['hostkey']}";
echo "Huella: " . ssh2_fingerprint($connection) . "\n";

echo "Métodos de transmisión de paquetes cliente a servidor:\n";
echo "\tCrypt: {$methods['client_to_server']['crypt']}\n";
echo "\tComp: {$methods['client_to_server']['comp']}\n";
echo "\tMAC: {$methods['client_to_server']['mac']}\n";

echo "Métodos de transmisión de paquetes servidor a cliente:\n";
echo "\tCrypt: {$methods['server_to_client']['crypt']}\n";
echo "\tComp: {$methods['server_to_client']['comp']}\n";
echo "\tMAC: {$methods['server_to_client']['mac']}\n";

?>

   
```php

## Véase también

ssh2_connect
