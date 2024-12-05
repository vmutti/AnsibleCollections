#!/bin/sh
colls=$1
if [ -z "$colls" ]; then
  colls=$(ls -d collections/*)
else 
  colls="collections/$colls"
fi
for coll in $colls;do
  echo initializing "$coll"
  if [ ! -f "$coll/README.md" ]; then
    cp skeletons/collection/README.md "$coll"
  fi
  if [ ! -f "$coll/galaxy.yml" ]; then
    cp skeletons/collection/galaxy.yml "$coll"
  fi

  if [ ! -f "$coll/meta/runtime.yml" ]; then
    mkdir -p "$coll/meta"
    cp skeletons/collection/meta/runtime.yml "$coll/meta"
  fi
  if [ -d "$coll/roles" ]; then
    for role in $(ls -d $coll/roles/*);do
      echo "initializing $role" 
      if [ ! -f "$role/meta/runtime.yml" ]; then
        mkdir -p "$role/meta"
        cp skeletons/role/meta/main.yml "$role/meta"
      fi
      if [ ! -f "$role/README.md" ]; then
        cp skeletons/role/README.md "$role"
      fi
    done
  fi
done
