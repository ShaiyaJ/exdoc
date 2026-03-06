package main

import "fmt"
import "strings"
import "io"
import "os"

func main() {
	// Getting extension
	var ext string
	fmt.Scanln(&ext) // TODO: error handling:

	// Getting content
	data, _ := io.ReadAll(os.Stdin)
	content := string(data[:])

	lines := strings.Split(content, "\n")

	// Outputting value based on ext
	switch ext {
	case ".md":
		fmt.Print("```", content, "```")
	case ".html":
		fmt.Print("<strong>", content, "</strong>")
	default:
		for _, line := range lines {
			fmt.Print("    ", line, "\n")
		}
	}
}
