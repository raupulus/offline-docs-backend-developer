---
title: Instalado como módulo de Apache
source_url: https://www.php.net/manual/es/security.apache.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: security/apache.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: security
translation_status: ready
translation_revision: ab6785b01
order: 109890
---

## Instalado como módulo de Apache

Cuando PHP es usado como un módulo de Apache, hereda los permisos del usuario de Apache (generalmente los del usuario "nobody"). Este hecho representa varios impactos sobre la seguridad y las autorizaciones. Por ejemplo, si se está usando PHP para acceder a una base de datos, a menos que tal base de datos disponga de un control de acceso propio, se tendrá que hacer que la base de datos sea asequible por el usuario "nobody". Esto quiere decir que un script malicioso podría tener acceso y modificar la base de datos, incluso sin un nombre de usuario y contraseña. Es completamente posible que una araña web (bot) pudiera toparse con la página web de administración de una base de datos, y eliminar todo de la base de datos. Una protección ante este tipo de situaciones es mediante el uso del mecanismo de autorización de Apache, o con modelos de acceso de diseño propio usando LDAP, archivos `.htaccess`, etc. e incluir ese código como parte de los scripts PHP.

Con frecuencia, una vez la seguridad se ha establecido en un punto en donde el usuario de PHP (en este caso, el usuario de apache) tiene asociada muy poco riesgo, se descubre que PHP se encuentra ahora imposibilitado de escribir archivos en los directorios de los usuarios. O quizás se le haya desprovisto de la capacidad de acceder o modificar bases de datos. Se ha prevenido que pudiera escribir tanto archivos buenos como malos, o que pudiera realizar transacciones buenas o malas en la base de datos.

Un error de seguridad cometido con frecuencia en este punto es darle permisos de administrador (root) a apache, o incrementar las habilidades del usuario de apache de alguna otra forma.

Incrementar los permisos del usuario de Apache hasta el nivel de administrador es extremadamente peligroso y puede comprometer al sistema entero, así que el uso de entornos sudo, chroot, o cualquier otro mecanismo que sea ejecutado como root no debería ser considerado como una opción por aquellos que no son profesionales en seguridad.

Existen otras soluciones más simples. Mediante el uso de [open_basedir](#ini.open-basedir) se puede controlar y restringir qué directorios pueden ser usados por PHP. También se pueden definir áreas solo-Apache, para restringir todas las actividades basadas en web a archivos que no son de usuarios o del sistema.
