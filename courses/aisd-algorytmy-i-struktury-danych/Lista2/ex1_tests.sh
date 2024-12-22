#!/bin/bash

echo 'gen_rand for n = 8. sort = insert_sort'
programs/gen_rand 8 | programs/insert_sort
echo 'gen_rand for n = 16. sort = insert_sort'
programs/gen_rand 16 | programs/insert_sort
echo 'gen_rand for n = 32. sort = insert_sort'
programs/gen_rand 32 | programs/insert_sort
echo 'gen_desc for n = 8. sort = insert_sort'
programs/gen_desc 8 | programs/insert_sort
echo 'gen_desc for n = 16. sort = insert_sort'
programs/gen_desc 16 | programs/insert_sort
echo 'gen_desc for n = 32. sort = insert_sort'
programs/gen_desc 32 | programs/insert_sort
echo 'gen_asc for n = 8. sort = insert_sort'
programs/gen_asc 8 | programs/insert_sort
echo 'gen_asc for n = 16. sort = insert_sort'
programs/gen_asc 16 | programs/insert_sort
echo 'gen_asc for n = 32. sort = insert_sort'
programs/gen_asc 32 | programs/insert_sort
echo 'gen_rand for n = 8. sort = merge_sort'
programs/gen_rand 8 | programs/merge_sort
echo 'gen_rand for n = 16. sort = merge_sort'
programs/gen_rand 16 | programs/merge_sort
echo 'gen_rand for n = 32. sort = merge_sort'
programs/gen_rand 32 | programs/merge_sort
echo 'gen_desc for n = 8. sort = merge_sort'
programs/gen_desc 8 | programs/merge_sort
echo 'gen_desc for n = 16. sort = merge_sort'
programs/gen_desc 16 | programs/merge_sort
echo 'gen_desc for n = 32. sort = merge_sort'
programs/gen_desc 32 | programs/merge_sort
echo 'gen_asc for n = 8. sort = merge_sort'
programs/gen_asc 8 | programs/merge_sort
echo 'gen_asc for n = 16. sort = merge_sort'
programs/gen_asc 16 | programs/merge_sort
echo 'gen_asc for n = 32. sort = merge_sort'
programs/gen_asc 32 | programs/merge_sort
echo 'gen_rand for n = 8. sort = quick_sort'
programs/gen_rand 8 | programs/quick_sort
echo 'gen_rand for n = 16. sort = quick_sort'
programs/gen_rand 16 | programs/quick_sort
echo 'gen_rand for n = 32. sort = quick_sort'
programs/gen_rand 32 | programs/quick_sort
echo 'gen_desc for n = 8. sort = quick_sort'
programs/gen_desc 8 | programs/quick_sort
echo 'gen_desc for n = 16. sort = quick_sort'
programs/gen_desc 16 | programs/quick_sort
echo 'gen_desc for n = 32. sort = quick_sort'
programs/gen_desc 32 | programs/quick_sort
echo 'gen_asc for n = 8. sort = quick_sort'
programs/gen_asc 8 | programs/quick_sort
echo 'gen_asc for n = 16. sort = quick_sort'
programs/gen_asc 16 | programs/quick_sort
echo 'gen_asc for n = 32. sort = quick_sort'
programs/gen_asc 32 | programs/quick_sort
