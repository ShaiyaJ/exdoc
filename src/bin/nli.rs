use std::io::{self};

fn main() -> io::Result<()> {
    let mut filetype = String::new();

    let stdin = io::stdin();
    stdin.read_line(&mut filetype)?;

    match filetype.trim() {
        "html" => println!("<ol>"),
        &_ => {}
    };

    for (i, line) in stdin.lines().enumerate() {
        match filetype.trim() {
            "txt" => println!("{}. {}", i+1, line.unwrap()),
            "80.txt" => println!("{}. {}", i+1, line.unwrap()),
            "79.txt" => println!("{}. {}", i+1, line.unwrap()),
            "50.txt" => println!("{}. {}", i+1, line.unwrap()),
            "40.txt" => println!("{}. {}", i+1, line.unwrap()),
            "md" => println!("{}. {}", i+1, line.unwrap()),
            "html" => println!("<li>{}</li>", line.unwrap()),
            &_ => println!("{}. {}", i+1, line.unwrap())
        };
    }

    match filetype.trim() {
        "html" => println!("</ol>"),
        &_ => {}
    };

    Ok(())
}
