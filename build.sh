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
files=$(ls ./build/**/**/*.go)

for file in $files; do 
	go build -o $file 
    rm $file                # Delete original source
done
