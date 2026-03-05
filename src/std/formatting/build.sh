#!/bin/sh

files=$(ls *.go)
for file in $files; do 
	go build -o bin/ $file
done
