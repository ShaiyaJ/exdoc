import "fmt"
import "strings"
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
	
	lines := strings.Split(content, "\n")

	// Outputting formatted cols
	for i, line := range lines {
		for (len(line) != 0) {
			s := line[:cols]
			line = line[cols:]

			fmt.Println(s)
		}
	}
}
