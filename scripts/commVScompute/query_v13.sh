#!/bin/sh

if test -f "$2"; then

QR=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='QR'
EOF)

cholQR_nb=$(sqlite3 $2 <<EOF
SELECT COUNT(text)/${1}
FROM NVTX_EVENTS
WHERE text='ChaseMpiDLA: potrf'
EOF)

QR_allreduce=$(sqlite3 $2 <<EOF
SELECT
	AVG(CASE WHEN RN <=${1}*${cholQR_nb} then end-start END)*${cholQR_nb}
FROM(
SELECT
	ROW_NUMBER() over () RN,
	end,
	start
FROM NVTX_EVENTS
WHERE text='allreduce'
 )
EOF)

echo "$3,$4 $5,QR,$(bc <<< "($QR-${QR_allreduce})"),${QR_allreduce}"

RR=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='RR'
EOF)

RR_bcast=$(sqlite3 $2 <<EOF
SELECT
	AVG(CASE WHEN RN <=${1}*2 then end-start END)*2
FROM(	
SELECT
	ROW_NUMBER() over () RN,
	end,
	start
FROM NVTX_EVENTS
WHERE text='MPI_Ibcast'  OR text='MPI_Wait'
 )
EOF)

RR_allreduce=$(sqlite3 $2 <<EOF
SELECT
    AVG(CASE WHEN RN >${1}*2 AND RN <=${1}*4 then end-start END)*2
FROM(
SELECT
    ROW_NUMBER() over () RN,
    end,
    start
FROM NVTX_EVENTS
WHERE text='allreduce'
 )
EOF)

echo "$3,$4 $5,RR,$(bc <<< "($RR-${RR_allreduce}-$RR_bcast)"),$(bc <<< "($RR_bcast+${RR_allreduce})")"

Resid=$(sqlite3 $2 <<EOF
SELECT AVG(end-start)
FROM NVTX_EVENTS
WHERE text='Resid'
EOF)

Resid_bcast=$(sqlite3 $2 <<EOF
SELECT
    AVG(CASE WHEN RN >${1}*2 then end-start END)*2
FROM(
SELECT
    ROW_NUMBER() over () RN,
    end,
    start
FROM NVTX_EVENTS
WHERE text='MPI_Ibcast'  OR text='MPI_Wait'
 )
EOF)

Resid_allreduce=$(sqlite3 $2 <<EOF
SELECT
    AVG(CASE WHEN RN >${1}*4 then end-start END)*2
FROM(
SELECT
    ROW_NUMBER() over () RN,
    end,
    start
FROM NVTX_EVENTS
WHERE text='allreduce'
 )
EOF)

echo "$3,$4 $5,Resid,$(bc <<< "($Resid-${Resid_allreduce}-$Resid_bcast)"),$(bc <<< "($Resid_bcast+${Resid_allreduce})")"


Init=$(sqlite3 $2 <<EOF
SELECT
	AVG(end-start)*4
FROM NVTX_EVENTS
WHERE text='ChaseMpiProperties(Block-Block2): Init'  OR text='ChaseMpiDLAMultiGPU: Init' OR text='ChaseMpiDLA: Init' OR text='ChaseMpiDLA: initVecs'
EOF)

RND=$(sqlite3 $2 <<EOF
SELECT
    AVG(end-start)
FROM NVTX_EVENTS
WHERE text='InitRndVecs'
EOF)

fi
