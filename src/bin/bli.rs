use std::io::{self};

fn main() -> io::Result<()> {
    let mut filetype = String::new();

    let stdin = io::stdin();
    stdin.read_line(&mut filetype)?;

    match filetype.trim() {
        "html" => println!("<ul>"),
        &_ => {}
    };

    for line in stdin.lines() {
        match filetype.trim() {
            "txt" => println!("- {}", line.unwrap()),
            "80.txt" => println!("- {}", line.unwrap()),
            "79.txt" => println!("- {}", line.unwrap()),
            "50.txt" => println!("- {}", line.unwrap()),
            "40.txt" => println!("- {}", line.unwrap()),
            "md" => println!("- {}", line.unwrap()),
            "html" => println!("<li>{}</li>", line.unwrap()),
            &_ => println!("- {}", line.unwrap())
        };
    }

    match filetype.trim() {
        "html" => println!("</ul>"),
        &_ => {}
    };

    Ok(())
}
