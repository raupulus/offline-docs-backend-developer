---
title: 'Soporte de FAN (Fast Application Notification : Notificación Rápida de Aplicación)
  OCI8'
source_url: https://www.php.net/manual/es/oci8.fan.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/oci8/fan.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: oci8
translation_status: ready
translation_reviewed: false
translation_revision: f4c44b869
order: 57170
---

## Soporte de FAN (Fast Application Notification : Notificación Rápida de Aplicación) OCI8

El soporte de FAN proporciona un cambio de conexión rápido, una funcionalidad de alta disponibilidad para la base de datos Oracle. Permite a los scripts PHP OCI8 ser notificados cuando una máquina de base de datos o una instancia de base de datos se vuelve no disponible. Sin FAN, OCI8 puede bloquearse en caso de alcanzar el tiempo límite TCP, y se devuelve un error, lo cual puede tomar varios minutos. La activación de FAN en OCI8 permite a las aplicaciones detectar los errores y reconectarse a una instancia de conexión disponible sin que el servidor Web necesite conocerlo.

El soporte de FAN está disponible cuando las bibliotecas clientes Oracle vinculadas a PHP y la base de datos Oracle son de la versión 10gR2 o superiores.

FAN beneficia a los usuarios de la tecnología de clúster Oracle (RAC) ya que las conexiones sobrevivientes a las instancias de base de datos pueden realizarse inmediatamente. Los usuarios de Oracle Data Guard con un broker, verán los eventos FAN generados cuando una base de datos pasa a estar en línea. Las bases de datos que no forman parte de un clúster enviarán eventos FAN cuando la base de datos se reinicie.

Para las conexiones activas, cuando una máquina o una instancia de base de datos se vuelve indisponible, se devolverá un error de conexión por la función de la extensión OCI8 llamada. Durante la reconexión de un script PHP subyacente, se establecerá una conexión a una instancia de base de datos sobreviviente. La extensión OCI8 también, de forma transparente, limpiará todas las conexiones inactivas afectadas por una máquina de base de datos o una instancia en fallo, así, las llamadas de conexión PHP establecerán una nueva conexión sin que el script lo sepa, evitando así cualquier interrupción del servicio.

Cuando [oci8.events](#ini.oci8.events) vale `On`, se sugiere definir [oci8.ping_interval](#ini.oci8.ping-interval) a -1 para desactivar el ping, sabiendo que la activación de los eventos FAN proporciona un gestor de conexiones proactivo de las conexiones inactivas que se han vuelto inválidas por una interrupción del servicio.

Para activar el soporte FAN en PHP OCI8, compile PHP OCI8 con las bibliotecas Oracle 10gR2 o superiores, luego, siga estos pasos:

- Con los privilegios de administrador de la base de datos, utilice un programa como SQL\*Plus para activar el servicio de base de datos para publicar los eventos FAN; por ejemplo:

          SQL> execute dbms_service.modify_service(
                         SERVICE_NAME        => 'sales',
                         AQ_HA_NOTIFICATIONS => TRUE);

- Edite el archivo php.ini y añada:

          oci8.events = On

- Si la aplicación no gestiona aún las condiciones de error OCI8, modifíquela para detectar los fallos. Esto puede requerir la reconexión y la re-ejecución de las consultas.

- Ejecute la aplicación, conéctese a la base de datos Oracle 10gR2 o superiores.
