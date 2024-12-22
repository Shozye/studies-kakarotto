#!/bin/bash

echo 'gen_rand for n = 8. sort = dual_pivot_quick_sort'
programs/gen_rand 8 | programs/dual_pivot_quick_sort
echo 'gen_rand for n = 16. sort = dual_pivot_quick_sort'
programs/gen_rand 16 | programs/dual_pivot_quick_sort
echo 'gen_rand for n = 32. sort = dual_pivot_quick_sort'
programs/gen_rand 32 | programs/dual_pivot_quick_sort
echo 'gen_desc for n = 8. sort = dual_pivot_quick_sort'
programs/gen_desc 8 | programs/dual_pivot_quick_sort
echo 'gen_desc for n = 16. sort = dual_pivot_quick_sort'
programs/gen_desc 16 | programs/dual_pivot_quick_sort
echo 'gen_desc for n = 32. sort = dual_pivot_quick_sort'
programs/gen_desc 32 | programs/dual_pivot_quick_sort
echo 'gen_asc for n = 8. sort = dual_pivot_quick_sort'
programs/gen_asc 8 | programs/dual_pivot_quick_sort
echo 'gen_asc for n = 16. sort = dual_pivot_quick_sort'
programs/gen_asc 16 | programs/dual_pivot_quick_sort
echo 'gen_asc for n = 32. sort = dual_pivot_quick_sort'
programs/gen_asc 32 | programs/dual_pivot_quick_sort
