package main 

import "fmt"

func main() {
    // Getting extension
    var ext string
    fmt.Scanln(&ext) // TODO: error handling:

    // Getting content
    var content string
    fmt.Scanf("%s", &content) // TODO: error handling

    // Outputting value based on ext
    switch ext {
        case ".md":		fmt.Print("```", content, "```")
        case ".html":	fmt.Print("<strong>", content, "</strong>")
        default:
			for index, element := range strings.Split(content, '\n') {
				fmt.Print("    ", element);
			}
	}
}
