// See https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
// Time to recover some of my ancient rudimentary C skills.
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

// taken from https://stackoverflow.com/questions/3893937/c-array-sorting-tips
int compare(const void *a, const void *b) {
    int int_a = *((int *)a);
    int int_b = *((int *)b);

    if (int_a == int_b)
      return 0;
    else if (int_a < int_b)
      return -1;
    else
      return 1;
  }

// Python for reference
// def minimumAbsoluteDifference(arr):
//     arr.sort()
//     return min([abs(arr[i] - arr[i-1]) for i in range(1, len(arr)) ])

// JS for reference (probably more relevant)
//function minimumAbsoluteDifference(arr) {
//    arr.sort(function (a, b) { return a - b; })
//    var i, rv;
//    for (i = 1; i < arr.length; i++) {
//        if (typeof rv == 'undefined') {
//            rv = Math.abs(arr[i] - arr[i - 1]);
//            // console.log(rv);
//        } else {
//            rv = Math.min(rv, Math.abs(arr[i] - arr[i - 1]));
//            // console.log(rv);
//        }
//    }
//    return rv;
//
//}

int minimumAbsoluteDifference(int arr_count, int* arr) {

  qsort(arr, arr_count, sizeof(int), compare);
   int rv = -9999;
   for (int i = 1; i < arr_count; i++) {
    if (rv == -9999) {
        rv = abs(arr[i] - arr[i-1]);
        } else {
        rv = imin(rv, abs(arr[i] - arr[i-1]));
        }
   }
   return rv;
}

int imin(int a, int b) {
    if (a > b) {
    return a;
    } else {
    return b;
    }
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char* n_endptr;
    char* n_str = readline();
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    char** arr_temp = split_string(readline());

    int* arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        char* arr_item_endptr;
        char* arr_item_str = *(arr_temp + i);
        int arr_item = strtol(arr_item_str, &arr_item_endptr, 10);

        if (arr_item_endptr == arr_item_str || *arr_item_endptr != '\0') { exit(EXIT_FAILURE); }

        *(arr + i) = arr_item;
    }

    int arr_count = n;

    int result = minimumAbsoluteDifference(arr_count, arr);

    fprintf(fptr, "%d\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) {
            break;
        }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') {
            break;
        }

        alloc_length <<= 1;

        data = realloc(data, alloc_length);

        if (!line) {
            break;
        }
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';

        data = realloc(data, data_length);
    } else {
        data = realloc(data, data_length + 1);

        data[data_length] = '\0';
    }

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);

        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}
