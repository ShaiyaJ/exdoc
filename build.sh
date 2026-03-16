#!/bin/sh

# Remove build folder if it exists
if [ -d "./build" ]; then
    rm -rf ./build 
fi

# Create build folder
mkdir build 
cp -R ./src ./build         # Coppying ./src to ./build
mv ./build/src/* ./build    # Flattening ./build/src to ./build
rm -rf ./build/src/

# Compiling go files
export GO111MODULE=auto

files=$(ls ./build/**/**/*.go)

for file in $files; do 
    # Build name
    basen=$(basename $file) # /path/name.go -> name.go
    name=${basen%.*}        # name.go -> name
    path=${file%\/*}        # /path/name.go -> /path (without trailing '/')

    gccgo "$file" -o "$path/$name"
    rm $file                # Delete original source
done
