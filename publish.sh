#!/bin/sh
colls=$2
if [ -z "$colls" ]; then
  colls=$(ls -d collections/*)
else 
  colls="collections/$colls"
fi
for coll in $colls;do
  echo building $coll
  bundle=$(ansible-galaxy collection build --output-path ./builds/ --force $coll| cut -d' ' -f 6 )

  if echo $bundle | grep -q "TKTK";then
    echo fill in info for "$coll"
  else
    echo 'publishing' $bundle
    ansible-galaxy collection publish "$bundle" --token "$1"
  fi 
done
