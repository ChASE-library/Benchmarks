#!/bin/sh

if test -f "$2"; then

QR=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='QR'
EOF)

QR_geqrf=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='ChaseMpiDLA: gegqr'
EOF)

echo "$3,$4 $5,QR,${QR_geqrf},$(bc <<< "($QR-${QR_geqrf})")"

RR=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='RR'
EOF)

RR_POSTApplication=$(sqlite3 $2 <<EOF
SELECT
	AVG(CASE WHEN RN<=102*$1 AND RN > 101*$1 then end-start END)
FROM(
    SELECT
    ROW_NUMBER() over () RN,
    end,
    start
	FROM NVTX_EVENTS
    WHERE text='ChaseMpiDLA: postApplication'
)
EOF)

RR_Allreduce=$(sqlite3 $2 <<EOF
SELECT
    AVG(CASE WHEN RN<=121*$1 AND RN > 120*$1 then end-start END)
FROM(
    SELECT
    ROW_NUMBER() over () RN,
    end,
    start
    FROM NVTX_EVENTS
    WHERE text='ChaseMpiDLA: allreduce'
)
EOF)

echo "$3,$4 $5,RR,$(bc <<< "($RR-${RR_POSTApplication}-${RR_Allreduce})"),$(bc <<< "(${RR_POSTApplication}+${RR_Allreduce})")"

Resid=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='Resid'
EOF)

#echo ${Resid}

Resid_POSTApplication=$(sqlite3 $2 <<EOF
SELECT
    AVG(CASE WHEN RN==103 then end-start END)
FROM(
    SELECT
    ROW_NUMBER() over () RN,
    end,
    start
    FROM NVTX_EVENTS
    WHERE text='ChaseMpiDLA: postApplication'
)
EOF)

Resid_Allreduce=$(sqlite3 $2 <<EOF
SELECT
    AVG(CASE WHEN RN<=122*$1 AND RN > 121*$1 then end-start END)
FROM(
    SELECT
    ROW_NUMBER() over () RN,
    end,
    start
    FROM NVTX_EVENTS
    WHERE text='ChaseMpiDLA: allreduce'
)
EOF)

echo "$3,$4 $5,Resid,$(bc <<< "($Resid-${Resid_POSTApplication}-${Resid_Allreduce})"),$(bc <<< "(${Resid_POSTApplication}+${Resid_Allreduce})")"

Init=$(sqlite3 $2 <<EOF
SELECT
    AVG(end-start)*2
FROM NVTX_EVENTS
WHERE text='ChaseMpiProperties(Block-Block2): Init'  OR text='ChaseMpiDLAMultiGPU: Init'
EOF)
#echo ${Init}

Init=$(sqlite3 $2 <<EOF
SELECT
    AVG(end-start)
FROM NVTX_EVENTS
WHERE text='initVecs'
EOF)
#echo ${Init}
fi
