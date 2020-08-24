#!/bin/sh

NAME="Are You out of Your Vulcan mind!"
echo $NAME
NAME="Leonard Mccoy"
echo $NAME
echo $$

echo

#!/bin/sh

$./test.sh Are You out of Your Vulcan mind

echo "File Name: $0"
echo "First Parameter : $1"Are
echo "Second Parameter : $2"You
echo "Third Parameter : $3"out
echo "Forth Parameter : $4"of
echo "Fifth parameter : $5"Your
echo "Sixt Parameter : $6"Vulcan
echo "Seventh Parameter : $7"mind
echo "Quoted Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters : $#"

echo

#!/bin/sh
NAME="a+b"
echo $NAME
NAME="ab"

echo

#!/bin/sh

$./test.sh

NAME[0]="Are"
NAME[1]="You"
NAME[2]="out"
NAME[3]="of"
NAME[4]="Your"
NAME[5]="Vulcan"
NAME[6]="mind"
echo "First Method: ${NAME[*]}"
echo "Second Method: ${NAME[@]}"


echo


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

echo


