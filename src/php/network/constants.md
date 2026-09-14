---
title: Constantes predefinidas
source_url: https://www.php.net/manual/es/network.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/network/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: network
translation_status: ready
translation_reviewed: true
translation_revision: 35ca7f108
order: 56210
---

## Constantes predefinidas

Las constantes listadas aquí están siempre disponibles en PHP.

`LOG_CONS` (`int`)  
Si ocurre un error al enviar los datos al registro del sistema, escribir directamente en la consola del sistema.

`LOG_NDELAY` (`int`)  
Abrir inmediatamente la conexión al registro.

`LOG_ODELAY` (`int`)  
Retrasar la apertura de la conexión hasta el registro del primer mensaje. Este es el comportamiento por omisión.

`LOG_NOWAIT` (`int`)  

`LOG_PERROR` (`int`)  
Registrar también los mensajes en `STDERR`.

`LOG_PID` (`int`)  
Incluir el ID de proceso (PID) con cada mensaje de registro.

<!-- -->

`LOG_AUTH` (`int`)  
Para los mensajes de seguridad o autorización.

> [!NOTE]
> Utilizar `LOG_AUTHPRIV` en su lugar cuando esté disponible.

`LOG_AUTHPRIV` (`int`)  
Para los mensajes de seguridad o autorización privados.

`LOG_CRON` (`int`)  
Para los mensajes del demonio de planificación. Por ejemplo, `cron` o `at`.

`LOG_DAEMON` (`int`)  
Para los mensajes de los demonios del sistema.

`LOG_KERN` (`int`)  
Para los mensajes del núcleo.

`LOG_LOCAL0` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL1` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL2` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL3` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL4` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL5` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL6` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LOCAL7` (`int`)  
Reservado para uso local.

> [!WARNING]
> No disponible en Windows.

`LOG_LPR` (`int`)  
Para los mensajes provenientes del subsistema de la impresora en línea.

`LOG_MAIL` (`int`)  
Para los mensajes provenientes del subsistema de mensajería.

`LOG_NEWS` (`int`)  
Para los mensajes provenientes del subsistema de noticias USENET.

`LOG_SYSLOG` (`int`)  
Para los mensajes generados internamente por `syslogd`.

`LOG_USER` (`int`)  
Para los mensajes genéricos a nivel de usuario.

`LOG_UUCP` (`int`)  
Para los mensajes provenientes del subsistema UUCP.

<!-- -->

`LOG_EMERG` (`int`)  
Urgencia, el sistema es inutilizable. Esto corresponde a una condición de pánico. Normalmente se difunde a todos los procesos.

`LOG_ALERT` (`int`)  
Alerta, se requiere una acción inmediata. Por ejemplo, una base de datos del sistema corrupta.

`LOG_CRIT` (`int`)  
Crítico, se requiere una acción. Por ejemplo, un error de hardware.

`LOG_ERR` (`int`)  
Mensajes de error.

`LOG_WARNING` (`int`)  
Mensajes de advertencia.

`LOG_NOTICE` (`int`)  
Mensajes de notificación, correspondientes a condiciones que no son errores, pero que pueden requerir un tratamiento especial.

`LOG_INFO` (`int`)  
Mensajes informativos.

`LOG_DEBUG` (`int`)  
Mensajes de depuración que contienen información generalmente útil solo durante la depuración de un programa.

<!-- -->

`DNS_ANY` (`int`)  
Todo registro de recurso. En la mayoría de los sistemas, esto devuelve todos los registros de recursos, sin embargo, debido a las particularidades de rendimiento de `libresolv` entre plataformas, esto no está garantizado.

El más lento `DNS_ALL` recolectará todos los registros de manera más fiable.

`DNS_ALL` (`int`)  
Consulta iterativa al servidor de nombres para cada tipo de registro disponible.

`DNS_A` (`int`)  
Registro de dirección IPv4.

`DNS_AAAA` (`int`)  
Recurso de dirección IPv6.

`DNS_A6` (`int`)  
Definido en las primeras especificaciones IPv6, pero degradado a histórico por [RFC 6563](https://datatracker.ietf.org/doc/html/rfc6563).

`DNS_CAA` (`int`)  
Recurso de autorización de autoridad de certificación. Disponible a partir de PHP 7.0.16 y 7.1.2.

> [!WARNING]
> No disponible en Windows.

`DNS_CNAME` (`int`)  
Recurso de alias (Nombre canónico).

`DNS_HINFO` (`int`)  
Recurso de información del host. Para más explicaciones y significados de estos valores, consulte la página de IANA sobre [Nombres de sistemas operativos](http://www.iana.org/assignments/operating-system-names).

`DNS_MX` (`int`)  
Recurso de intercambiador de correo.

`DNS_NAPTR` (`int`)  
Puntero de autoridad de nombre.

`DNS_NS` (`int`)  
Recurso del servidor de nombres autoritario.

`DNS_PTR` (`int`)  
Recurso de puntero.

`DNS_SOA` (`int`)  
Recurso de inicio de autoridad.

`DNS_SRV` (`int`)  
Localizador de servicio.

`DNS_TXT` (`int`)  
Recurso de texto.
