#!/bin/bash

echo Number given: $1
c=$1
#
a=0; b=0; #b0=0; b1=0; b2=0; b3=0; b4=0; b5=0; b6=0; b7=0;

a=$(($1/2)); b=$(($1%2)); b0=$b
echo $a $b $b0
a=$(($a/2)); b=$(($a%2)); b1=$b
echo $aa $b $b1
aa=$(($a/2)); b=$(($a%2)); b2=$b
echo $a $b $b2
#

echo "c mainīgā vērtība pirms cikla:" $c
while [ "sc" != 0 ]
do
 c=$(($c/2))
 echo "c mainīgā vērtība ciklā:" $c
done
echo "c mainīgā vērtība pēc cikla:" $c


#!/bin/sh

a=0
while [ "$a" -lt 10 ]    # this is loop1
do
   b="$a"
   while [ "$b" -ge 0 ]  # this is loop2
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done
