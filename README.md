# JP2pdf

JP2pdf is a simple Python tool designed to convert JP2/JPEG 2000 image files into PDF format. This tool handles both individual JP2 files and batch processing of multiple JP2 files within a directory, making it versatile for various workflow needs.

## Understanding JP2 and This Tool's Purpose

JPEG 2000 (JP2) is an image compression standard that offers superior quality compared to traditional JPEG, but it's not as widely supported by standard PDF viewers and document management systems. This tool bridges that gap by converting JP2 images into universally readable PDF documents while preserving image quality.

## Key Features

This tool offers several practical advantages for handling JP2 files:

**Flexible Input Processing**: You can convert either a single JP2 file or process an entire directory containing multiple JP2 files in one operation. This flexibility makes it suitable for both quick individual conversions and large batch processing tasks.

**High-Quality Direct Conversion**: The tool performs direct JP2-to-PDF conversion using PyMuPDF, which maintains the original image quality without unnecessary compression or quality loss that might occur with intermediate format conversions.

**Intuitive Command-Line Interface**: The tool uses straightforward command-line syntax that follows common patterns, making it easy to integrate into existing workflows or automation scripts.

**Comprehensive Logging**: Detailed output messages help you track the conversion process, identify any issues with specific files, and understand exactly what the tool is doing at each step.

## Installation Process

Before using JP2pdf, you need to ensure your system has the necessary dependencies. The tool relies on specific Python packages that handle image processing and PDF creation.

**Step 1: Install Required Dependencies**
```bash
pip install -r requirements.txt
```

This command installs PyMuPDF (imported as `fitz` in Python), which is the core library that handles both JP2 image reading and PDF creation. PyMuPDF is particularly well-suited for this task because it can directly work with JP2 files without requiring intermediate conversion steps.

**Understanding the Requirements**: The primary dependency is PyMuPDF, a Python binding for the MuPDF library. This choice is significant because MuPDF has native support for JPEG 2000 images, ensuring efficient and high-quality conversions.

## Usage Guide

The tool's design philosophy centers on simplicity while providing the flexibility you need for different scenarios. Here's how to use it effectively:

### Basic Conversion Scenarios

**Converting a Single JP2 File**:
```bash
python jp2pdf.py path/to/image.jp2
```

When you run this command, the tool automatically creates a PDF file with the same base name as your JP2 file, but with a `.pdf` extension. For example, if your input file is `document.jp2`, the output will be `document.jp2.pdf`.

**Processing an Entire Directory**:
```bash
python jp2pdf.py path/to/directory
```

This approach is particularly useful when you have multiple JP2 files that logically belong together, such as scanned pages of a document. The tool will find all JP2 files in the specified directory, sort them alphabetically by filename, and combine them into a single PDF document. The output PDF will be named after the directory.

**Specifying Custom Output Location**:
```bash
python jp2pdf.py path/to/image.jp2 -o output.pdf
```

The `-o` or `--output` option gives you control over where and how the resulting PDF is named. This is especially useful when integrating the tool into automated workflows or when you need the output file to follow specific naming conventions.

### Understanding Command-Line Parameters

**Required Parameter**:
- `input_path`: This can be either a path to a single JP2 file or a directory containing JP2 files. The tool automatically detects which type of input you've provided and adjusts its behavior accordingly.

**Optional Parameters**:
- `-o, --output`: Specifies the path and filename for the output PDF. If you don't provide this option, the tool generates a sensible default name based on your input.

### How the Tool Processes Your Files

When you run JP2pdf, it follows a systematic approach to ensure reliable conversion:

**Input Validation**: The tool first checks whether your specified path exists and, if it's a file, whether it has the correct `.jp2` extension. This early validation helps catch common mistakes before processing begins.

**File Discovery**: For directory inputs, the tool searches for all files with the `.jp2` extension and sorts them alphabetically. This sorting ensures that pages appear in a predictable order in the final PDF.

**Conversion Process**: Each JP2 file is opened using PyMuPDF's native JPEG 2000 support, converted to a PDF page, and then combined into the final document. The tool processes files one at a time and provides status updates for each file.

**Error Handling**: If a particular JP2 file cannot be processed (due to corruption, unusual formatting, or other issues), the tool logs the error and continues with the remaining files rather than stopping the entire process.

## System Requirements

Understanding the technical requirements helps ensure smooth operation:

**Python Version**: The tool requires Python 3.6 or later. This requirement stems from the use of modern Python features like f-string formatting and the `pathlib` module for robust file path handling.

**Core Dependency**: PyMuPDF (fitz) is the only external dependency required. This library provides comprehensive PDF manipulation capabilities and includes native support for JPEG 2000 images, making it ideal for this specific conversion task.

**Memory Considerations**: While the tool is designed to be efficient, processing very large JP2 files or directories with many files may require adequate system memory. The tool loads images into memory during conversion, so available RAM may be a limiting factor for extremely large operations.

## Troubleshooting Common Issues

If you encounter problems, here are some common scenarios and solutions:

**"JP2 files not found" message**: This typically means either the directory doesn't contain any `.jp2` files, or the files have a different extension. Check that your files actually have the `.jp2` extension and not `.jpeg2000` or another variant.

**Individual file processing errors**: If specific files fail to convert, they may be corrupted or use a variant of the JPEG 2000 standard that PyMuPDF doesn't support. The tool will log detailed error information to help you identify the issue.

**Permission errors**: Ensure you have read access to the input files and write access to the output directory.

## License and Attribution

This project is released under the MIT License, which means you're free to use, modify, and distribute the tool for both personal and commercial purposes, subject to the license terms.

**Author**: wabisuke

The MIT License provides maximum flexibility while requiring only that you preserve the original copyright notice in any distributions or derivative works.

## Integration and Automation

This tool's command-line interface makes it easy to integrate into larger workflows:

**Batch Scripts**: You can call JP2pdf from shell scripts or batch files to automate document processing workflows.

**Python Integration**: Since JP2pdf is written in Python, you can also import and use its core functions within larger Python applications.

**CI/CD Pipelines**: The tool's clear exit codes and logging make it suitable for use in continuous integration environments where document processing is part of an automated workflow.
