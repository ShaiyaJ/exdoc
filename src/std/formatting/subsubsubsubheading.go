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
		fmt.Print("##### ", content)
	case ".html":
		fmt.Print("<h5>", content, "</h5>")
	case ".ansi":
		fmt.Print("- \033[1m", content, "\033[22m -")
	default:
		fmt.Print("- ", content, " -")
	}
}
