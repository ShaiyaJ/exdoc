use regex;
use fmt;
use strings;
use io;
use os;

fn btoi(b: bool) int = { // TODO: don't do this.
    if (b) 
        return 1;
    return 0;
};

// Runs the result of a matched block (excluding #s)
fn process_block(raw: str) str = {
    const raw_utf8 = strings::toutf8(raw);

    const suppress_filetype = (raw_utf8[0] == '!' ^^ raw_utf8[1] == '!');
    const recursive = (raw_utf8[0] == '*' ^^ raw_utf8[1] == '*');

    const raw = strings::sub(raw, btoi(suppress_filetype): size + btoi(recursive): size); // Trimming off !/*
    const raw = strings::ltrim(raw); // Trimming off whitespace

    const file = "";        // TODO: get file (headache because valid UNIX paths can contain " and ' and \ ...
    const content = "";     // TODO: get content

    return "";              // TODO: run the command {file} with {content} as the stdin
};

// Applies a regex pattern to a string and replaces string content with process_block
// Expects that the regex was to match a valid exdoc block in capture group 1 - result must be free'd
fn apply_pattern(target: str, pattern: str) str = {
    const re = regex::compile(pattern)!;
    defer regex::finish(&re);

    const results = regex::findall(&re, target);
    defer regex::result_freeall(results);

    let copy = strings::dup(target);

    for (let result .. results) {
        copy = strings::replace(copy, result[1].content, process_block(result[1].content));
    };

    return copy;
};

// Processes an entire document, matching all exdoc blocks
fn process_document(target: str) str = {
    const doubles = apply_pattern(target, `##([\s\S]*?)##`);
    defer free(doubles);

    const singles = apply_pattern(doubles, `#(.*?)#`);
    return singles;
};

export fn main() void = {
    const input_content = match (io::drain(os::stdin)) {
    case let bytes: []u8 =>
        yield bytes;
    case =>
        fmt::fatalf("Error reading stdin.");
    };

    const input_content = match (strings::fromutf8(input_content)) {
    case let content: str =>
        yield content;
    case =>
        fmt::fatalf("Malformed string data in given content.");
    };

    fmt::println( process_document(input_content) )!;
};
