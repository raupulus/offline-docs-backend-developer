---
title: Nuevas constantes globales
source_url: https://www.php.net/manual/es/migration83.constants.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration83/constants.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: f037a94fd
order: 1000
---

## Nuevas constantes globales

## cURL

- `CURLINFO_CAPATH` (libcurl \>= 7.84.0)

- `CURLINFO_CAINFO` (libcurl \>= 7.84.0)

- `CURLOPT_MIME_OPTIONS` (libcurl \>= 7.81.0)

- `CURLMIMEOPT_FORMESCAPE` (libcurl \>= 7.81.0)

- `CURLOPT_WS_OPTIONS` (libcurl \>= 7.86.0)

- `CURLWS_RAW_MODE` (libcurl \>= 7.86.0)

- `CURLOPT_SSH_HOSTKEYFUNCTION` (libcurl \>= 7.84.0)

- `CURLOPT_PROTOCOLS_STR` (libcurl \>= 7.85.0)

- `CURLOPT_REDIR_PROTOCOLS_STR` (libcurl \>= 7.85.0)

- `CURLOPT_CA_CACHE_TIMEOUT` (libcurl \>= 7.87.0)

- `CURLOPT_QUICK_EXIT` (libcurl \>= 7.87.0)

- `CURLKHMATCH_OK` (libcurl \>= 7.19.6)

- `CURLKHMATCH_MISMATCH` (libcurl \>= 7.19.6)

- `CURLKHMATCH_MISSING` (libcurl \>= 7.19.6)

- `CURLKHMATCH_LAST` (libcurl \>= 7.19.6)

## Intl

- `MIXED_NUMBERS` (`Spoofchecker`)

- `HIDDEN_OVERLAY` (`Spoofchecker`)

## OpenSSL

- `OPENSSL_CMS_OLDMIMETYPE`

- `PKCS7_NOOLDMIMETYPE`

## PCNTL

- `SIGINFO`

## PDO_ODBC

- `PDO_ODBC_TYPE`

## Posix

- `POSIX_SC_ARG_MAX`

- `POSIX_SC_PAGESIZE`

- `POSIX_SC_NPROCESSORS_CONF`

- `POSIX_SC_NPROCESSORS_ONLN`

- `POSIX_PC_LINK_MAX`

- `POSIX_PC_MAX_CANON`

- `POSIX_PC_MAX_INPUT`

- `POSIX_PC_NAME_MAX`

- `POSIX_PC_PATH_MAX`

- `POSIX_PC_PIPE_BUF`

- `POSIX_PC_CHOWN_RESTRICTED`

- `POSIX_PC_NO_TRUNC`

- `POSIX_PC_ALLOC_SIZE_MIN`

- `POSIX_PC_SYMLINK_MAX`

## Sockets

Les options de socket suivantes sont maintenant définies si elles sont prises en charge :

- `SO_ATTACH_REUSEPORT_CBPF` (Linux)

- `SO_DETACH_BPF` (Linux)

- `SO_DETACH_FILTER` (Linux)

- `TCP_QUICKACK` (Linux)

- `IP_DONTFRAG` (FreeBSD)

- `IP_MTU_DISCOVER` (Linux)

- `IP_PMTUDISC_DO` (Linux)

- `IP_PMTUDISC_DONT` (Linux)

- `IP_PMTUDISC_WANT` (Linux)

- `IP_PMTUDISC_PROBE` (Linux)

- `IP_PMTUDISC_INTERFACE` (Linux)

- `IP_PMTUDISC_OMIT` (Linux)

- `AF_DIVERT` (FreeBSD)

- `SOL_UDPLITE`

- `UDPLITE_RECV_CSCOV`

- `UDPLITE_SEND_CSCOV`

- `SO_RERROR` (NetBSD)

- `SO_ZEROIZE` (OpenBSD)

- `SO_SPLICE` (OpenBSD)

- `TCP_REPAIR` (Linux)

- `SO_REUSEPORT_LB` (FreeBSD)

- `IP_BIND_ADDRESS_NO_PORT` (Linux)

## Zip

- `ZipArchive::ER_DATA_LENGTH` (libzip \>= 1.10)

- `ZipArchive::ER_NOT_ALLOWED` (libzip \>= 1.10)

- `ZipArchive::AFL_RDONLY` (libzip \>= 1.10)

- `ZipArchive::AFL_IS_TORRENTZIP` (libzip \>= 1.10)

- `ZipArchive::AFL_WANT_TORRENTZIP` (libzip \>= 1.10)

- `ZipArchive::AFL_CREATE_OR_KEEP_FILE_FOR_EMPTY_ARCHIVE` (libzip \>= 1.10)

- `ZipArchive::FL_OPEN_FILE_NOW`

- `ZipArchive::LENGTH_TO_END` as default value for `ZipArchive::addFile` and `ZipArchive::replaceFile`

- `ZipArchive::LENGTH_UNCHECKED` (libzip \>= 1.10)
