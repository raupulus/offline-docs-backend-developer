---
title: syslog
description: Genera un mensaje en el historial del sistema
source_url: https://www.php.net/manual/es/function.syslog.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/functions/syslog.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 35ca7f108
order: 56580
---

syslog

Genera un mensaje en el historial del sistema

## Descripción

```php
syslog(int $priority, string $message): true
```php

`syslog` genera un mensaje que será registrado en el historial por el sistema.

Para más información sobre cómo configurar un gestor de historial, consúltese el manual Unix, página 5 `syslog.conf(5)`. Otra información sobre los sistemas de historial y sus opciones también está disponible en el manual `syslog(3)` de las máquinas Unix.

## Parámetros

`priority`  
Una de las `LOG_EMERG`, `LOG_ALERT`, `LOG_CRIT`, `LOG_ERR`, `LOG_WARNING`, `LOG_NOTICE`, `LOG_INFO`, `LOG_DEBUG` constantes.

`message`  
El mensaje a enviar.

## Valores devueltos

Retorna siempre `true`.

## Ejemplos

Ejemplo con `syslog`

```
<?php
// apertura de syslog, adición del PID y envío simultáneo del
// mensaje a la salida estándar y a un mecanismo
// específico
openlog("myScriptLog", LOG_PID | LOG_PERROR, LOG_LOCAL0);

// algunas líneas de código

if (authorized_client()) {
    // hacer algo
} else {
    // cliente no autorizado!
    // registro del intento
    $access = date("Y/m/d H:i:s");
    syslog(LOG_WARNING, "Cliente no autorizado: $access {$_SERVER['REMOTE_ADDR']} ({$_SERVER['HTTP_USER_AGENT']})");
}

closelog();
?>

    
```php

## Notas

En Windows, el historial es gestionado por el registro de eventos.

> [!NOTE]
> El uso de `LOG_LOCAL0` a `LOG_LOCAL7` para el argumento `facility` de la función `openlog` no está disponible en Windows.

## Véase también

`openlog`, `closelog`, Parámetro INI [syslog.filter](#ini.syslog.filter) (a partir de PHP 7.3)
