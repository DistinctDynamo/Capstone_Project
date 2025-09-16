#!/usr/bin/env python3
"""
Document to Markdown Converter
Converts Word documents (.doc, .docx) to Markdown format using pandoc
"""

import os
import subprocess
import sys
import glob
from pathlib import Path
from typing import List, Dict, Optional


class DocumentConverter:
    def __init__(self):
        self.supported_formats = ['.doc', '.docx']
        self.conversion_log = []
    
    def check_pandoc_available(self) -> bool:
        """Check if pandoc is installed and available"""
        try:
            result = subprocess.run(['pandoc', '--version'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def check_textutil_available(self) -> bool:
        """Check if textutil is available (macOS only, for .doc files)"""
        try:
            result = subprocess.run(['textutil', '--help'], 
                                  capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def install_pandoc_instructions(self):
        """Print instructions for installing pandoc"""
        print("❌ Pandoc is not installed!")
        print("\nTo install pandoc:")
        print("  macOS:   brew install pandoc")
        print("  Ubuntu:  sudo apt-get install pandoc")
        print("  Windows: Download from https://pandoc.org/installing.html")
        print("\nPandoc is required for document conversion.")
    
    def convert_docx_to_md(self, input_file: str, output_file: str = None) -> bool:
        """Convert .docx file to Markdown using pandoc"""
        if not output_file:
            output_file = os.path.splitext(input_file)[0] + '.md'
        
        try:
            result = subprocess.run([
                'pandoc', input_file, '-o', output_file
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                file_size = os.path.getsize(output_file)
                self.conversion_log.append({
                    'input': input_file,
                    'output': output_file,
                    'status': 'success',
                    'size': file_size,
                    'method': 'pandoc'
                })
                return True
            else:
                self.conversion_log.append({
                    'input': input_file,
                    'output': output_file,
                    'status': 'failed',
                    'error': result.stderr,
                    'method': 'pandoc'
                })
                return False
        except Exception as e:
            self.conversion_log.append({
                'input': input_file,
                'output': output_file,
                'status': 'error',
                'error': str(e),
                'method': 'pandoc'
            })
            return False
    
    def convert_doc_to_md(self, input_file: str, output_file: str = None) -> bool:
        """Convert .doc file to Markdown using textutil + pandoc (macOS)"""
        if not output_file:
            output_file = os.path.splitext(input_file)[0] + '.md'
        
        # Step 1: Convert .doc to .html using textutil
        temp_html = os.path.splitext(input_file)[0] + '_temp.html'
        
        try:
            # Convert to HTML first
            result1 = subprocess.run([
                'textutil', '-convert', 'html', input_file, '-output', temp_html
            ], capture_output=True, text=True)
            
            if result1.returncode != 0:
                if not self.check_textutil_available():
                    print(f"❌ textutil not available. Cannot convert {input_file}")
                    print("Note: .doc files require textutil (macOS) or other conversion method")
                    return False
                else:
                    print(f"❌ Failed to convert {input_file} to HTML")
                    return False
            
            # Step 2: Convert HTML to Markdown using pandoc
            result2 = subprocess.run([
                'pandoc', temp_html, '-o', output_file
            ], capture_output=True, text=True)
            
            # Clean up temporary file
            if os.path.exists(temp_html):
                os.remove(temp_html)
            
            if result2.returncode == 0:
                file_size = os.path.getsize(output_file)
                self.conversion_log.append({
                    'input': input_file,
                    'output': output_file,
                    'status': 'success',
                    'size': file_size,
                    'method': 'textutil + pandoc'
                })
                return True
            else:
                self.conversion_log.append({
                    'input': input_file,
                    'output': output_file,
                    'status': 'failed',
                    'error': result2.stderr,
                    'method': 'textutil + pandoc'
                })
                return False
                
        except Exception as e:
            # Clean up temporary file if it exists
            if os.path.exists(temp_html):
                os.remove(temp_html)
            
            self.conversion_log.append({
                'input': input_file,
                'output': output_file,
                'status': 'error',
                'error': str(e),
                'method': 'textutil + pandoc'
            })
            return False
    
    def convert_file(self, input_file: str, output_file: str = None) -> bool:
        """Convert a single file to Markdown"""
        file_ext = os.path.splitext(input_file)[1].lower()
        
        if file_ext not in self.supported_formats:
            print(f"❌ Unsupported format: {file_ext}")
            return False
        
        if not os.path.exists(input_file):
            print(f"❌ File not found: {input_file}")
            return False
        
        print(f"🔄 Converting {input_file}...")
        
        if file_ext == '.docx':
            return self.convert_docx_to_md(input_file, output_file)
        elif file_ext == '.doc':
            return self.convert_doc_to_md(input_file, output_file)
        
        return False
    
    def find_documents(self, directory: str = '.') -> List[str]:
        """Find all Word documents in the specified directory"""
        documents = []
        for ext in self.supported_formats:
            pattern = os.path.join(directory, f'*{ext}')
            documents.extend(glob.glob(pattern))
        return sorted(documents)
    
    def convert_all_in_directory(self, directory: str = '.', force: bool = False) -> Dict:
        """Convert all Word documents in a directory"""
        documents = self.find_documents(directory)
        
        if not documents:
            print(f"📂 No Word documents found in {directory}")
            return {'converted': 0, 'skipped': 0, 'failed': 0}
        
        stats = {'converted': 0, 'skipped': 0, 'failed': 0}
        
        print(f"📂 Found {len(documents)} document(s) to convert:")
        for doc in documents:
            print(f"   • {doc}")
        print()
        
        for doc in documents:
            output_file = os.path.splitext(doc)[0] + '.md'
            
            # Skip if output already exists and not forcing
            if os.path.exists(output_file) and not force:
                print(f"⏭️  Skipping {doc} (output exists, use --force to overwrite)")
                stats['skipped'] += 1
                continue
            
            if self.convert_file(doc, output_file):
                print(f"✅ Converted: {doc} → {output_file}")
                stats['converted'] += 1
            else:
                print(f"❌ Failed: {doc}")
                stats['failed'] += 1
        
        return stats
    
    def print_conversion_log(self):
        """Print detailed conversion log"""
        if not self.conversion_log:
            print("📋 No conversions performed")
            return
        
        print("\n📋 Conversion Log:")
        print("=" * 60)
        
        for entry in self.conversion_log:
            status_icon = "✅" if entry['status'] == 'success' else "❌"
            print(f"{status_icon} {entry['input']}")
            print(f"   Method: {entry['method']}")
            print(f"   Output: {entry['output']}")
            
            if entry['status'] == 'success':
                size_kb = entry['size'] / 1024
                print(f"   Size: {size_kb:.1f} KB")
            else:
                print(f"   Error: {entry.get('error', 'Unknown error')}")
            print()


def main():
    """Main function with command line interface"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Convert Word documents to Markdown format',
        epilog='''
Examples:
  python convert_docs_to_md.py                           # Convert all docs in current directory
  python convert_docs_to_md.py --file document.docx      # Convert specific file
  python convert_docs_to_md.py --directory /path/to/docs # Convert all docs in directory
  python convert_docs_to_md.py --force                   # Overwrite existing files
  python convert_docs_to_md.py --list                    # List documents without converting
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('--file', '-f', 
                       help='Convert a specific file')
    parser.add_argument('--directory', '-d', default='.', 
                       help='Directory to search for documents (default: current)')
    parser.add_argument('--output', '-o', 
                       help='Output filename (only used with --file)')
    parser.add_argument('--force', action='store_true', 
                       help='Overwrite existing Markdown files')
    parser.add_argument('--list', '-l', action='store_true', 
                       help='List documents without converting')
    parser.add_argument('--verbose', '-v', action='store_true', 
                       help='Show detailed conversion log')
    
    args = parser.parse_args()
    
    converter = DocumentConverter()
    
    # Check dependencies
    if not converter.check_pandoc_available():
        converter.install_pandoc_instructions()
        return 1
    
    # List mode
    if args.list:
        docs = converter.find_documents(args.directory)
        if docs:
            print(f"📂 Word documents in {args.directory}:")
            for doc in docs:
                md_file = os.path.splitext(doc)[0] + '.md'
                status = "✅ (MD exists)" if os.path.exists(md_file) else "⏳ (not converted)"
                print(f"   • {doc} {status}")
        else:
            print(f"📂 No Word documents found in {args.directory}")
        return 0
    
    # Single file mode
    if args.file:
        success = converter.convert_file(args.file, args.output)
        if args.verbose:
            converter.print_conversion_log()
        return 0 if success else 1
    
    # Directory mode
    print("📄 Document to Markdown Converter")
    print("=" * 40)
    
    stats = converter.convert_all_in_directory(args.directory, args.force)
    
    # Print summary
    print(f"\n📊 Conversion Summary:")
    print(f"   ✅ Converted: {stats['converted']}")
    print(f"   ⏭️  Skipped: {stats['skipped']}")
    print(f"   ❌ Failed: {stats['failed']}")
    
    if args.verbose:
        converter.print_conversion_log()
    
    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())