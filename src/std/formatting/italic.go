package main

import "fmt"
import "io"
import "os"

func main() {
	// Getting extension
	var ext string
	fmt.Scanln(&ext) // TODO: error handling:

	// Getting content
	data, _ := io.ReadAll(os.Stdin)
	content := string(data[:])

	// Outputting value based on ext
	switch ext {
	case ".md":
		fmt.Print("*", content, "*")
	case ".html":
		fmt.Print("<em>", content, "</em>")
	case ".ansi":
		fmt.Print("\033[3m", content, "\033[23m")
	default:
		fmt.Print("*", content, "*")
	}
}
