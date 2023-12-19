#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    // Open the current directory.
    FILE *dir = popen("ls -1 *.txt 2>/dev/null", "r");

    if (!dir) {
        perror("Unable to open directory");
        return 1;
    }

    char filename[256];

    // Read the filename of the first text file in the directory.
    if (fgets(filename, sizeof(filename), dir) == NULL) {
        perror("No text files found in the directory");
        return 1;
    }

    // Remove the newline character at the end of the filename.
    filename[strlen(filename) - 1] = '\0';

    // Close the directory.
    pclose(dir);

    // Open the text file for reading.
    FILE *file = fopen(filename, "r");

    if (!file) {
        perror("Unable to open file");
        return 1;
    }

    char line[1024];
    int sum = 0; // Initialize the sum of two-digit numbers

    // Read and process each line in the file.
    while (fgets(line, sizeof(line), file)) {
        // Initialize indices for the start and end of the number.
        int start = 0;
        int end = strlen(line) - 1;

        // Eliminate non-numeric characters from the beginning.
        while (start <= end && !isdigit(line[start])) {
            start++;
        }

        // Eliminate non-numeric characters from the end.
        while (end >= start && !isdigit(line[end])) {
            end--;
        }

        // Check if there's only one digit in the line.
        if (start <= end) {
            char first = line[start];
            char last = line[end];

            // Convert the two-digit number to an integer and add it to the sum.
            int number = (first - '0') * 10 + (last - '0');
            sum += number;
            printf("%d\n", number);
        }
    }

    // Close the file.
    fclose(file);

    // Print the sum of two-digit numbers.
    printf("Sum of two-digit numbers: %d\n", sum);

    return 0;
}
