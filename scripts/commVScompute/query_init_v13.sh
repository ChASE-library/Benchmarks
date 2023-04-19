#!/bin/sh

if test -f "$2"; then

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

echo "$3,$4 $5,Init,${RND},${Init}"

fi
