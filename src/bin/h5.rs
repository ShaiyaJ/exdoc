use std::io::{self, prelude::*};

fn main() -> io::Result<()> {
    let mut filetype = String::new();
    let mut content: Vec<u8> = Vec::new();

    let mut stdin = io::stdin();
    stdin.read_line(&mut filetype)?;
    stdin.read_to_end(&mut content)?;

    unsafe { print!("{}", match filetype.trim() {
        "txt" => format!("=== {}", str::from_utf8_unchecked(&content)),
        "80.txt" => format!("=== {}", str::from_utf8_unchecked(&content)),
        "79.txt" => format!("=== {}", str::from_utf8_unchecked(&content)),
        "50.txt" => format!("=== {}", str::from_utf8_unchecked(&content)),
        "40.txt" => format!("=== {}", str::from_utf8_unchecked(&content)),
        "md" => format!("##### {}", str::from_utf8_unchecked(&content)),
        "html" => format!("<h5>{}</h5>", str::from_utf8_unchecked(&content)),
        &_ => format!("__{}__", str::from_utf8_unchecked(&content))
    }); }

    Ok(())
}
