#!/usr/bin/env python3
"""
PDF Text Extraction Utility for NH Data Scraper

Extracts text and tables from PDF files using pdfplumber.
Supports both local files and URLs.
"""

import argparse
import json
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
import tempfile

try:
    import pdfplumber
except ImportError:
    print("Error: pdfplumber not installed. Run: pip install pdfplumber")
    sys.exit(1)


# Known NH data PDF sources
NH_PDF_SOURCES = {
    "wages": "https://www.nhes.nh.gov/elmi/products/documents/wages-intro.pdf",
    "budget": "https://www.das.nh.gov/budget/Budget2026-2027/Governor_Executive_Summary_FY_2026-2027.pdf",
}


def download_pdf(url: str, timeout: int = 30) -> bytes:
    """Download PDF from URL and return bytes."""
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; NHDataScraper/1.0)"
    }
    request = Request(url, headers=headers)

    try:
        with urlopen(request, timeout=timeout) as response:
            return response.read()
    except HTTPError as e:
        raise RuntimeError(f"HTTP Error {e.code}: {e.reason}")
    except URLError as e:
        raise RuntimeError(f"URL Error: {e.reason}")


def extract_text(pdf_path: str) -> str:
    """Extract all text from a PDF file."""
    text_parts = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            page_text = page.extract_text()
            if page_text:
                text_parts.append(f"--- Page {i} ---\n{page_text}")

    return "\n\n".join(text_parts)


def extract_tables(pdf_path: str) -> list:
    """Extract all tables from a PDF file."""
    all_tables = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            tables = page.extract_tables()
            for j, table in enumerate(tables, 1):
                if table:
                    all_tables.append({
                        "page": i,
                        "table_number": j,
                        "data": table
                    })

    return all_tables


def extract_from_source(source: str, extract_tables_flag: bool = False) -> dict:
    """
    Extract content from a PDF source.

    Args:
        source: File path, URL, or known source key (wages, budget)
        extract_tables_flag: Whether to also extract tables

    Returns:
        Dictionary with extracted content
    """
    # Check if source is a known key
    if source.lower() in NH_PDF_SOURCES:
        url = NH_PDF_SOURCES[source.lower()]
        print(f"Using known source '{source}': {url}")
        source = url

    result = {
        "source": source,
        "text": "",
        "tables": [],
        "page_count": 0
    }

    # Handle URL vs local file
    if source.startswith(("http://", "https://")):
        print(f"Downloading PDF from {source}...")
        try:
            pdf_bytes = download_pdf(source)
        except RuntimeError as e:
            result["error"] = str(e)
            return result

        # Write to temp file for pdfplumber
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
            tmp.write(pdf_bytes)
            tmp_path = tmp.name

        pdf_path = tmp_path
    else:
        pdf_path = source
        if not Path(pdf_path).exists():
            result["error"] = f"File not found: {pdf_path}"
            return result

    # Extract content
    try:
        with pdfplumber.open(pdf_path) as pdf:
            result["page_count"] = len(pdf.pages)

        print(f"Extracting text from {result['page_count']} pages...")
        result["text"] = extract_text(pdf_path)

        if extract_tables_flag:
            print("Extracting tables...")
            result["tables"] = extract_tables(pdf_path)
            print(f"Found {len(result['tables'])} tables")

    finally:
        # Clean up temp file if created
        if source.startswith(("http://", "https://")):
            Path(tmp_path).unlink(missing_ok=True)

    return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract text and tables from PDF files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s document.pdf                    Extract text from local file
  %(prog)s wages                           Extract from NH wages PDF
  %(prog)s budget --tables                 Extract text and tables from NH budget PDF
  %(prog)s https://example.com/doc.pdf     Extract from URL
  %(prog)s document.pdf -o output.txt      Save text to file
  %(prog)s document.pdf --json -o out.json Save as JSON

Known sources:
  wages  - NH Employment Security Wages PDF
  budget - Governor's Executive Budget Summary FY 2026-2027
        """
    )

    parser.add_argument(
        "source",
        help="PDF file path, URL, or known source (wages, budget)"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output file path (default: stdout)"
    )
    parser.add_argument(
        "--tables",
        action="store_true",
        help="Also extract tables from the PDF"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON format"
    )
    parser.add_argument(
        "--tables-only",
        action="store_true",
        help="Only extract tables (implies --tables and --json)"
    )

    args = parser.parse_args()

    # Handle --tables-only
    if args.tables_only:
        args.tables = True
        args.json = True

    # Extract content
    result = extract_from_source(args.source, args.tables)

    if "error" in result:
        print(f"Error: {result['error']}", file=sys.stderr)
        sys.exit(1)

    # Format output
    if args.json:
        if args.tables_only:
            output = json.dumps(result["tables"], indent=2)
        else:
            output = json.dumps(result, indent=2)
    else:
        output = result["text"]
        if args.tables and result["tables"]:
            output += "\n\n=== TABLES ===\n"
            for table in result["tables"]:
                output += f"\n--- Page {table['page']}, Table {table['table_number']} ---\n"
                for row in table["data"]:
                    output += " | ".join(str(cell) if cell else "" for cell in row) + "\n"

    # Write output
    if args.output:
        Path(args.output).write_text(output)
        print(f"Output saved to {args.output}")
    else:
        print(output)


if __name__ == "__main__":
    main()
