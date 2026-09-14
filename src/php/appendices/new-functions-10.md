---
title: Nuevas funciones
source_url: https://www.php.net/manual/es/migration84.new-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration84/new-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: true
translation_revision: 30b0c5117
order: 1140
---

## Nuevas funciones

## Núcleo

request_parse_body

## BCMath

bcceil

bcdivmod

bcfloor

bcround

## Fecha

DateTime::createFromTimestamp

DateTime::getMicrosecond

DateTime::setMicrosecond

DateTimeImmutable::createFromTimestamp

DateTimeImmutable::getMicrosecond

DateTimeImmutable::setMicrosecond

## DOM

DOMNode::compareDocumentPosition

DOMXPath::registerPhpFunctionNS

DOMXPath::quote

## Hash

HashContext::\_\_debugInfo

## Intl

IntlTimeZone::getIanaID

intltz_get_iana_id

IntlDateFormatter::parseToCalendar

Spoofchecker::setAllowedChars

grapheme_str_split

## MBString

mb_trim

mb_ltrim

mb_rtrim

mb_ucfirst

mb_lcfirst

## Opcache

opcache_jit_blacklist

## PCNTL

pcntl_getcpu

pcntl_getcpuaffinity

pcntl_getqos_class

pcntl_setns

pcntl_setqos_class

pcntl_waitid

## PDO_PGSQL

Pdo\Pgsql::setNoticeCallback

## PGSQL

pg_change_password

pg_jit

pg_put_copy_data

pg_put_copy_end

pg_result_memory_size

pg_set_chunked_rows_size

pg_socket_poll

## Reflection

Los métodos siguientes están relacionados con la nueva funcionalidad de objetos perezosos: ReflectionClass::newLazyGhost, ReflectionClass::newLazyProxy, ReflectionClass::resetAsLazyGhost, ReflectionClass::resetAsLazyProxy, ReflectionClass::isUninitializedLazyObject, ReflectionClass::initializeLazyObject, ReflectionClass::markLazyObjectAsInitialized, ReflectionClass::getLazyInitializer, ReflectionProperty::skipLazyInitialization, ReflectionProperty::setRawValueWithoutLazyInitialization

ReflectionClassConstant::isDeprecated

ReflectionGenerator::isClosed

ReflectionProperty::isDynamic

## Sodium

sodium_crypto_aead_aegis128l\_

\*

sodium_crypto_aead_aegis256l\_

\*

## SPL

SplObjectStorage::seek

## SOAP

SoapServer::\_\_getLastResponse

## Estándar

http_get_last_response_headers

http_clear_last_response_headers

fpow

array_all

array_any

array_find

array_find_key

## Tidy

tidyNode::getNextSibling

tidyNode::getPreviousSibling

## XMLReader

XMLReader::fromStream

XMLReader::fromUri

XMLReader::fromString

## XMLWriter

XMLWriter::toStream

XMLWriter::toUri

XMLWriter::toMemory

## XSL

XSLTProcessor::registerPhpFunctionNS
