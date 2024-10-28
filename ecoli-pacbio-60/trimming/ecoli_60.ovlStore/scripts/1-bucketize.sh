#!/bin/sh


#  Path to Canu.

bin="/Users/pfb2024/canu-2.2/bin"

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which java`
echo "  " `java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_CLIENT_UA=
export CANU_OBJECT_STORE_CLIENT_DA=
export CANU_OBJECT_STORE_NAMESPACE=
export CANU_OBJECT_STORE_PROJECT=




#  Discover the job ID to run, from either a grid environment variable and a
#  command line offset, or directly from the command line.
#
if [ x$CANU_LOCAL_JOB_ID = x -o x$CANU_LOCAL_JOB_ID = xundefined -o x$CANU_LOCAL_JOB_ID = x0 ]; then
  baseid=$1
  offset=0
else
  baseid=$CANU_LOCAL_JOB_ID
  offset=$1
fi
if [ x$offset = x ]; then
  offset=0
fi
if [ x$baseid = x ]; then
  echo Error: I need CANU_LOCAL_JOB_ID set, or a job index on the command line.
  exit
fi
jobid=`expr -- $baseid + $offset`
if [ x$baseid = x0 ]; then
  echo Error: jobid 0 is invalid\; I need CANU_LOCAL_JOB_ID set, or a job index on the command line.
  exit
fi
if [ x$CANU_LOCAL_JOB_ID = x ]; then
  echo Running job $jobid based on command line options.
else
  echo Running job $jobid based on CANU_LOCAL_JOB_ID=$CANU_LOCAL_JOB_ID and offset=$offset.
fi

echo ""
echo "Attempting to increase maximum allowed processes and open files."
max=`ulimit -Hu`
bef=`ulimit -Su`
if [ $bef -lt $max ] ; then
  ulimit -Su $max
  aft=`ulimit -Su`
  echo "  Changed max processes per user from $bef to $aft (max $max)."
else
  echo "  Max processes per user limited to $bef, no increase possible."
fi

max=`ulimit -Hn`
bef=`ulimit -Sn`
if [ $bef -lt $max ] ; then
  ulimit -Sn $max
  aft=`ulimit -Sn`
  echo "  Changed max open files from $bef to $aft (max $max)."
else
  echo "  Max open files limited to $bef, no increase possible."
fi

echo ""


#  This script should be executed from trimming/ecoli_60.ovlStore.BUILDING/, but the binary needs
#  to run from trimming/ (all the paths in the config are relative to there).

cd ..

jobname=`printf %04d $jobid`

if [ -e ./ecoli_60.ovlStore.BUILDING/bucket$jobname ] ; then
  echo "Bucketizing job finished; directory './ecoli_60.ovlStore.BUILDING/bucket$jobname' exists."
  exit
fi



#
#  Bucketize!
#

$bin/ovStoreBucketizer \
  -O  ./ecoli_60.ovlStore.BUILDING \
  -S ../ecoli_60.seqStore \
  -C  ./ecoli_60.ovlStore.config \
  -f \
  -b $jobid 
