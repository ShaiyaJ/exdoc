use regex;
use fmt;
use strings;
use io;
use os;

const SUPPRESS_CAPTURE_GROUP = 1;
const RECURSIVE_CAPTURE_GROUP = 2;
const FILENAME_CAPTURE_GROUP = 3;
const CONTENT_CAPTURE_GROUP = 4;

fn exdoc_re_generator() regex::regex = {
    match (regex::compile(`#`                 // Match any #
                          `[(!)`              // Match a potential !
                          `(\*)]*`            // Match a potential *
                          ` *`                // Zero or more spaces between # and the filename
                          `(.*)`              // The file name
                          `[\n ]*`            // Zero or more spaces/newlines between the filename and the content
                          `<(.+|>)[^\\]>`)) { // Any characters inside <>
    case let err: regex::error =>
        fmt::fatalf(regex::strerror(err));
    case let other: regex::regex =>
        return other;
    };
};

// Runs the result of a matched block
fn process_block(raw: regex::result) str = {
    const suppress_filetype = len(raw[SUPPRESS_CAPTURE_GROUP].content) != 0;
    const recursive = len(raw[RECURSIVE_CAPTURE_GROUP].content) != 0;
    const file = raw[FILENAME_CAPTURE_GROUP];
    const content = raw[CONTENT_CAPTURE_GROUP];

    return "";              // TODO: run the command {file} with {content} as the stdin
};

// Processes an entire document, matching all exdoc blocks
fn process_document(target: str) str = {
    const exdoc_re = exdoc_re_generator();
    defer regex::finish(&exdoc_re);

    const results = regex::findall(&exdoc_re, target);
    defer regex::result_freeall(results);

    fmt::println(len(results))!;

    let copy = strings::dup(target);

    for (let result .. results) {
        fmt::println(result[0].content)!;
        fmt::println(result[SUPPRESS_CAPTURE_GROUP].content)!;
        fmt::println(result[FILENAME_CAPTURE_GROUP].content)!;
        fmt::println(result[CONTENT_CAPTURE_GROUP].content)!;

        copy = strings::replace(copy, result[0].content, process_block(result));
    };

    return copy;
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

@test fn exdoc_re_test() void = {
    const exdoc_re = exdoc_re_generator();
    defer regex::finish(&exdoc_re);

    const fails = [
        "#this is a test",
        "This is a test",
        "# this <is a test\\>",
//        "\\# this <is a test>",
    ];

    const passes = [
        "#this <is a test>",
        "#this<is a test>",
        "# this<is a test>",
        "# this <is a test>",
        "# this <\nis a test>",
        "# this <\nis a test\n>",
        "# this \n<\nis a test\n>",
        "\\## this <is a test>",
        "#!*this <is a test>",
        "#*!this <is a test>",
        "# this < >"
        "# this <>"
    ];

    for (let s .. fails)
        assert(!regex::test(&exdoc_re, s), fmt::asprintf("Wrong match at \"{}\"", s));

    for (let s .. passes)
        assert(regex::test(&exdoc_re, s), fmt::asprintf("Didn't match at \"{}\"", s));
};
