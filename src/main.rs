use regex::{Captures, Regex};
use std::{io, io::prelude::*, process::Command, process::Stdio};

const RAW_RE: &str = concat!(
    r"(?:^#|[^\\]#)",           // Match the # at the start of the input or a # without a \ before it
    r"(?<suppress_ext>!){0,1}", // Match 1 !
    r"(?<recursive>\*){0,1}",   // Match 1 * 
    r"[\n ]*",                  // Allow for any amount of whitespace or newlines until the command
    r"\((?<command>.*)\)",      // Match the command
    r"[\n ]*",                  // Allow for any amount of whitespace or newlines until the content
    r"<(?<content>[\s\S]*)>");  // Match any content inbetween <>

fn process_text(text: &str, re: &Regex, ext: &str) -> String {
    Regex::replace_all(re, text, |caps: &Captures| -> String {
        let suppress_ext = caps.name("suppress_ext").is_some();
        let recursive = caps.name("recursive").is_some();
        let command = caps.name("command").expect("Couldn't determine command").as_str();
        let content = caps.name("content").expect("Couldn't determine content").as_str();

        // Opening handler      TODO: windows platform is unsupported
        let mut command_handler = Command::new("sh")
                                          .arg("-c")
                                          .arg(command)
                                          .stdin(Stdio::piped())
                                          .stdout(Stdio::piped())
                                          .spawn()
                                          .expect("Failed to start command process");

        // Writing content to the program
        let mut command_input = String::new();

        if !suppress_ext {
            command_input.push_str(ext);
            command_input.push_str("\n");
        }

        command_input.push_str(content);

        let command_input_bytes = command_input.into_bytes();

        command_handler.stdin.take().expect("Failed to open command stdin")
                             .write_all(&command_input_bytes).expect("Failed to write to command stdin");

        // Running command
        let command_output = command_handler.wait_with_output().expect("Failed to open command stdout").stdout;

        let result = String::from_utf8(command_output)
            .expect("Non UTF-8 compliant command output");

        // Handling recursive blocks
        if recursive {
            return process_text(&result, re, ext);
        }

        return result;
    }).to_string()
}

fn main() -> io::Result<()> {
    // Get string data from stdin
    let mut data: Vec<u8> = vec!();
    let _ = io::stdin().read_to_end(&mut data);
    
    let string_data = str::from_utf8(&data)
                        .expect("Non UTF-8 compliant input");

    // Apply regex replace on it
    let exdoc_re = Regex::new(RAW_RE).unwrap();
    
    // Outputting resulting text
    print!("{}", process_text(string_data, &exdoc_re, "txt"));

    Ok(())
}
