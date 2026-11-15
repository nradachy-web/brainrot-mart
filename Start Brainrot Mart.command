#!/bin/bash
cd "$(dirname "$0")"
if lsof -i :4181 >/dev/null 2>&1; then
  open "http://127.0.0.1:4181"
  exit 0
fi
node server.js > server.log 2>&1 &
sleep 1
open "http://127.0.0.1:4181"
