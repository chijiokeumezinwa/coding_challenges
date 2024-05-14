#!/bin/bash

function countbytes() {
    output=$(wc -c $1)
    echo "${output}"
}

function countlines(){
    output=$(wc -l $1)
    echo "${output}"
}

function countwords(){
    output=$(wc -w $1)
    echo "${output}"
}

function countmulti(){
    output=$(wc -m $1)
    echo "${output}"
}


# if [-p /dev/stdin ]; then
#     echo "Data was piped into this script!"
#     while IFS = read line; do
#         echo "Line: ${line}"
#     done

# else
#     echo "No input found on stdin"
#     while getopts c:l:w:m: flag
#     do
#         case "${flag}" in
#             c) countbytes ${OPTARG};;
#             l) countlines ${OPTARG};;
#             w) countwords ${OPTARG};;
#             m) countmulti ${OPTARG};;
#         esac
#     done
# fi

while getopts c:l:w:m: flag
do
    case "${flag}" in
        c) countbytes ${OPTARG};;
        l) countlines ${OPTARG};;
        w) countwords ${OPTARG};;
        m) countmulti ${OPTARG};;
        *) 
            echo "weird argument";;
    esac
done



