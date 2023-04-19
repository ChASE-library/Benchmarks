#!/bin/sh

if test -f "$2"; then

Init=$(sqlite3 $2 <<EOF
SELECT
    AVG(end-start)*2
FROM NVTX_EVENTS
WHERE text='ChaseMpiProperties(Block-Block2): Init'  OR text='ChaseMpiDLAMultiGPU: Init'
EOF)

RND=$(sqlite3 $2 <<EOF
SELECT
    AVG(end-start)
FROM NVTX_EVENTS
WHERE text='initVecs'
EOF)

echo "$3,$4 $5,Init,${RND},${Init}"

fi
