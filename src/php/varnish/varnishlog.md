---
title: La clase VarnishLog
source_url: https://www.php.net/manual/es/class.varnishlog.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/varnish/varnishlog.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: varnish
translation_status: ready
translation_revision: 4d17b7b49
order: 101140
---

## Introducción

## Sinopsis de la clase

VarnishLog

VarnishLog

Constantes

const

int

VarnishLog::TAG_Debug

0

const

int

VarnishLog::TAG_Error

1

const

int

VarnishLog::TAG_CLI

2

const

int

VarnishLog::TAG_StatSess

3

const

int

VarnishLog::TAG_ReqEnd

4

const

int

VarnishLog::TAG_SessionOpen

5

const

int

VarnishLog::TAG_SessionClose

6

const

int

VarnishLog::TAG_BackendOpen

7

const

int

VarnishLog::TAG_BackendXID

8

const

int

VarnishLog::TAG_BackendReuse

9

const

int

VarnishLog::TAG_BackendClose

10

const

int

VarnishLog::TAG_HttpGarbage

11

const

int

VarnishLog::TAG_Backend

12

const

int

VarnishLog::TAG_Length

13

const

int

VarnishLog::TAG_FetchError

14

const

int

VarnishLog::TAG_RxRequest

15

const

int

VarnishLog::TAG_RxResponse

16

const

int

VarnishLog::TAG_RxStatus

17

const

int

VarnishLog::TAG_RxURL

18

const

int

VarnishLog::TAG_RxProtocol

19

const

int

VarnishLog::TAG_RxHeader

20

const

int

VarnishLog::TAG_TxRequest

21

const

int

VarnishLog::TAG_TxResponse

22

const

int

VarnishLog::TAG_TxStatus

23

const

int

VarnishLog::TAG_TxURL

24

const

int

VarnishLog::TAG_TxProtocol

25

const

int

VarnishLog::TAG_TxHeader

26

const

int

VarnishLog::TAG_ObjRequest

27

const

int

VarnishLog::TAG_ObjResponse

28

const

int

VarnishLog::TAG_ObjStatus

29

const

int

VarnishLog::TAG_ObjURL

30

const

int

VarnishLog::TAG_ObjProtocol

31

const

int

VarnishLog::TAG_ObjHeader

32

const

int

VarnishLog::TAG_LostHeader

33

const

int

VarnishLog::TAG_TTL

34

const

int

VarnishLog::TAG_Fetch_Body

35

const

int

VarnishLog::TAG_VCL_acl

36

const

int

VarnishLog::TAG_VCL_call

37

const

int

VarnishLog::TAG_VCL_trace

38

const

int

VarnishLog::TAG_VCL_return

39

const

int

VarnishLog::TAG_VCL_error

40

const

int

VarnishLog::TAG_ReqStart

41

const

int

VarnishLog::TAG_Hit

42

const

int

VarnishLog::TAG_HitPass

43

const

int

VarnishLog::TAG_ExpBan

44

const

int

VarnishLog::TAG_ExpKill

45

const

int

VarnishLog::TAG_WorkThread

46

const

int

VarnishLog::TAG_ESI_xmlerror

47

const

int

VarnishLog::TAG_Hash

48

const

int

VarnishLog::TAG_Backend_health

49

const

int

VarnishLog::TAG_VCL_Log

50

const

int

VarnishLog::TAG_Gzip

51

Métodos

## Constantes predefinidas

`VarnishLog::TAG_Debug`  

`VarnishLog::TAG_Error`  

`VarnishLog::TAG_CLI`  

`VarnishLog::TAG_StatSess`  

`VarnishLog::TAG_ReqEnd`  

`VarnishLog::TAG_SessionOpen`  

`VarnishLog::TAG_SessionClose`  

`VarnishLog::TAG_BackendOpen`  

`VarnishLog::TAG_BackendXID`  

`VarnishLog::TAG_BackendReuse`  

`VarnishLog::TAG_BackendClose`  

`VarnishLog::TAG_HttpGarbage`  

`VarnishLog::TAG_Backend`  

`VarnishLog::TAG_Length`  

`VarnishLog::TAG_FetchError`  

`VarnishLog::TAG_RxRequest`  

`VarnishLog::TAG_RxResponse`  

`VarnishLog::TAG_RxStatus`  

`VarnishLog::TAG_RxURL`  

`VarnishLog::TAG_RxProtocol`  

`VarnishLog::TAG_RxHeader`  

`VarnishLog::TAG_TxRequest`  

`VarnishLog::TAG_TxResponse`  

`VarnishLog::TAG_TxStatus`  

`VarnishLog::TAG_TxURL`  

`VarnishLog::TAG_TxProtocol`  

`VarnishLog::TAG_TxHeader`  

`VarnishLog::TAG_ObjRequest`  

`VarnishLog::TAG_ObjResponse`  

`VarnishLog::TAG_ObjStatus`  

`VarnishLog::TAG_ObjURL`  

`VarnishLog::TAG_ObjProtocol`  

`VarnishLog::TAG_ObjHeader`  

`VarnishLog::TAG_LostHeader`  

`VarnishLog::TAG_TTL`  

`VarnishLog::TAG_Fetch_Body`  

`VarnishLog::TAG_VCL_acl`  

`VarnishLog::TAG_VCL_call`  

`VarnishLog::TAG_VCL_trace`  

`VarnishLog::TAG_VCL_return`  

`VarnishLog::TAG_VCL_error`  

`VarnishLog::TAG_ReqStart`  

`VarnishLog::TAG_Hit`  

`VarnishLog::TAG_HitPass`  

`VarnishLog::TAG_ExpBan`  

`VarnishLog::TAG_ExpKill`  

`VarnishLog::TAG_WorkThread`  

`VarnishLog::TAG_ESI_xmlerror`  

`VarnishLog::TAG_Hash`  

`VarnishLog::TAG_Backend_health`  

`VarnishLog::TAG_VCL_Log`  

`VarnishLog::TAG_Gzip`
