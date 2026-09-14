---
title: Instalación
source_url: https://www.php.net/manual/es/install.fpm.install.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: install/fpm/install.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: install
translation_status: ready
translation_revision: b536040d1
order: 1690
---

## Instalación

## Compilar desde las fuentes

Para activar FPM en la construcción de PHP es necesario añadir la línea `--enable-fpm` a la línea de configuración.

Existen múltiples opciones de configuración para FPM (todas opcionales):

- `--with-fpm-user` - el usuario FPM (por omisión - nobody).

- `--with-fpm-group` - el grupo FPM (por omisión - nobody).

- `--with-fpm-systemd` - Activa la integración de systemd (por omisión - no).

- `--with-fpm-acl` - Utilizar POSIX Access Control Lists (por omisión - no).

- `--with-fpm-apparmor` - Activa la integración de AppArmor (por omisión - no).

- `--with-fpm-selinux` - Activa la integración SELinux (por omisión - no).

## Historial de cambios

| Versión | Descripción                                      |
|---------|--------------------------------------------------|
| 8.2.0   | La opción `--with-fpm-selinux` ha sido añadida.  |
| 8.0.0   | La opción `--with-fpm-apparmor` ha sido añadida. |
