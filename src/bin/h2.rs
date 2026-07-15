use std::io::{self, prelude::*};

fn main() -> io::Result<()> {
    let mut filetype = String::new();
    let mut content: Vec<u8> = Vec::new();

    let mut stdin = io::stdin();
    stdin.read_line(&mut filetype)?;
    stdin.read_to_end(&mut content)?;

    unsafe { print!("{}", match filetype.trim() {
        "txt" => format!("{:~^80}", str::from_utf8_unchecked(&content)),
        "80.txt" => format!("{:~^80}", str::from_utf8_unchecked(&content)),
        "79.txt" => format!("{:~^79}", str::from_utf8_unchecked(&content)),
        "50.txt" => format!("{:~^50}", str::from_utf8_unchecked(&content)),
        "40.txt" => format!("{:~^40}", str::from_utf8_unchecked(&content)),
        "md" => format!("## {}", str::from_utf8_unchecked(&content)),
        "html" => format!("<h2>{}</h2>", str::from_utf8_unchecked(&content)),
        &_ => format!("~~~~~ {} ~~~~~", str::from_utf8_unchecked(&content))
    }); }

    Ok(())
}
