package main

import "fmt"
import "io"
import "os"

func main() {
	// Getting extension
	var ext string
	fmt.Scanln(&ext) // TODO: error handling:

	// Getting cols
	var cols int
	fmt.Scanf("%d", &cols);

	// Getting content
	data, _ := io.ReadAll(os.Stdin)
	content := string(data[:])

	// Outputting formatted cols
	switch ext {
	// TODO: support other filetypes!
	default:
		var current_line_chars int = 0;

		for total_chars := 0; total_chars < len(content); total_chars++ {
			if current_line_chars == cols {
				fmt.Printf("\n")
				current_line_chars = 0
			}

			fmt.Printf("%c", content[total_chars])

			current_line_chars++;
		}
	}
}
