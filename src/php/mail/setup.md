---
title: Instalación/Configuración
source_url: https://www.php.net/manual/es/mail.setup.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mail/setup.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mail
translation_status: ready
translation_reviewed: true
translation_revision: 48ce43fe7
order: 44280
---

## Instalación/Configuración

## Requisitos

Para que las funciones Mail estén disponibles, es necesario que PHP tenga acceso al binario `sendmail` en el servidor durante la compilación. Si se utiliza otro programa de correo, como qmail o postfix, asegúrese de utilizar las API correctas. PHP comenzará a buscar sendmail en el `PATH`, y luego, en los siguientes directorios: `/usr/bin:/usr/sbin:/usr/etc:/etc:/usr/ucblib:/usr/lib`. Se recomienda encarecidamente tener sendmail disponible en el `PATH`. Además, el usuario que compile PHP debe tener los permisos necesarios para acceder al ejecutable sendmail.
