#! /bin/bash

sudo mkdir books
cd books

wget https://www.gutenberg.org/files/57654/57654-0.txt
wget https://www.gutenberg.org/cache/epub/22045/pg22045.txt
wget https://www.gutenberg.org/files/61339/61339-0.txt
wget https://www.gutenberg.org/cache/epub/29640/pg29640.txt
wget https://www.gutenberg.org/cache/epub/54430/pg54430.txt

hdfs dfs -put /home/cloudera/books* /user/cloudera
hdfs dfs -ls books
