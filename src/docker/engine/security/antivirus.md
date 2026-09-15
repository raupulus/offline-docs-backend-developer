---
title: Antivirus software and Docker
description: General guidelines for using antivirus software with Docker
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/engine/security/antivirus.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: engine
order: 5550
---

When antivirus software scans files used by Docker, these files may be locked
in a way that causes Docker commands to hang.

One way to reduce these problems is to add the Docker data directory
(`/var/lib/docker` on Linux, `%ProgramData%\docker` on Windows Server, or `$HOME/Library/Containers/com.docker.docker/` on Mac) to the
antivirus's exclusion list. However, this comes with the trade-off that viruses
or malware in Docker images, writable layers of containers, or volumes are not
detected. If you do choose to exclude Docker's data directory from background
virus scanning, you may want to schedule a recurring task that stops Docker,
scans the data directory, and restarts Docker.
