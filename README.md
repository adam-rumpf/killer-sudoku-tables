# Killer Sudoku Tables

Programs for generating tables of integer partitions for use in solving Killer Sudoku puzzles.

## Introduction

[Killer Sudoku](https://en.wikipedia.org/wiki/Killer_sudoku) (a.k.a. Sumdoku) is a popular Sudoku variant wherein some collections of cells are circled by cages, with the sum of the digits in the cage being given as a clue. Solving Killer Sudoku puzzles often relies on quickly [partitioning an integer](https://en.wikipedia.org/wiki/Integer_partition) (the cage sum) into a sum of a specific number of integers (the number of cells in the cage). Experts simply have common integer partitions memorized, so these scripts are meant for generating tables for quick reference.

## Contents

This repo includes a Python file for generating relevant partitions along with a text file listing relevant results. The file defines some functions that can be used for generating specific types of partitions or partitions falling within specific ranges, while the text file is simply a table containing a range of specific results. Since this is meant for Sudoku puzzles, only sums containing digits 1-9 are included. Lists containing no repeat digits are highlighted since these represent the only valid partitions for cages lying entirely within a single row, column, or 3x3 box.
