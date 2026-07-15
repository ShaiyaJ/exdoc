use regex::{Captures, Regex};
use std::{io, io::prelude::*, process::Command};

const RAW_RE: &str = concat!(
    r"(?:^#|[^\\]#)",           // Match the # at the start of the input or a # without a \ before it
    r"(?<suppress_ext>!){0,1}", // Match 1 !
    r"(?<recursive>\*){0,1}",   // Match 1 * 
    r"[\n ]*",                  // Allow for any amount of whitespace or newlines until the command
    r"\((?<command>.*)\)",      // Match the command
    r"[\n ]*",                  // Allow for any amount of whitespace or newlines until the content
    r"<(?<content>[\s\S]*)>");  // Match any content inbetween <>

fn process_text(text: &str, re: &Regex) -> String {
    Regex::replace_all(re, text, |caps: &Captures| -> String {
        let suppress_ext = caps.name("suppress_ext").is_some();
        let recursive = caps.name("recursive").is_some();
        let command = caps.name("command").expect("Couldn't determine command").as_str();
        let content = caps.name("content").expect("Couldn't determine content").as_str();

        let command_result = Command::new(command)
            .output()
            .expect("Command failed")
            .stdout;

        let command_result_str = String::from_utf8(command_result)
            .expect("Non UTF-8 compliant command output");

        if recursive {
            return process_text(&command_result_str, re);
        }

        return command_result_str;
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
    
    print!("{}", process_text(string_data, &exdoc_re));

    Ok(())
}
