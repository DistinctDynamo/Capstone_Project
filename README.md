# COMP3059 Capstone Project - Document Tools

This repository contains Python tools for managing COMP3059 capstone project documentation, including automated meeting minutes generation and document conversion utilities.

## 📁 Repository Structure

```
Capstone_Project/
├── README.md                                          # Main documentation
├── Sprint1_REQUIREMENTS.md                            # Sprint requirements
│
├── scripts/                                           # Python automation tools
│   ├── generate_meeting_minutes.py                    # Meeting minutes generator
│   └── convert_docs_to_md.py                         # Document converter
│
├── templates/                                         # Course templates
│   ├── original/                                      # Original Word documents
│   │   ├── COMP3059-F25-High Level Requirements-Template.doc
│   │   ├── COMP3059-F25-Project Vision Template.docx
│   │   ├── COMP3059-F25-Project_Summary_Template.docx
│   │   └── COMP3059-F25-Minutes of Meeting-Template.docx
│   └── markdown/                                      # Converted Markdown versions
│       ├── COMP3059-F25-High Level Requirements-Template.md
│       ├── COMP3059-F25-Project Vision Template.md
│       ├── COMP3059-F25-Project_Summary_Template.md
│       └── COMP3059-F25-Minutes of Meeting-Template.md
│
├── config/                                            # Configuration files
│   └── sample_meeting_config.json                    # Sample meeting config
│
├── documentation/                                     # Additional documentation
│   └── README_meeting_generator.md                   # Detailed meeting tool docs
│
├── generated/                                         # Generated meeting minutes
│   └── sample_meeting_minutes.md                     # Sample output
│
└── venv/                                             # Python virtual environment
```

## 🚀 Quick Start

### 1. Setup Environment
```bash
# Clone repository
git clone <repository-url>
cd Capstone_Project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install python-docx
```

### 2. Generate Meeting Minutes
```bash
# Interactive mode
source venv/bin/activate
python scripts/generate_meeting_minutes.py

# Quick generation from template
python scripts/generate_meeting_minutes.py --sample
python scripts/generate_meeting_minutes.py --json config/sample_meeting_config.json
```

### 3. Convert Documents
```bash
# Convert all Word docs to Markdown
python scripts/convert_docs_to_md.py

# Convert specific file
python scripts/convert_docs_to_md.py --file templates/original/document.docx
```

## 📝 Meeting Minutes Generator

### Features
- ✅ **Professional Format**: Follows COMP3059-F25 template exactly
- ✅ **Dual Output**: Generates both Markdown (.md) and Word (.docx) formats
- ✅ **Interactive Mode**: User-friendly prompts for all details
- ✅ **JSON Configuration**: Batch generation from config files
- ✅ **Team Management**: Handles multiple attendees and signatures

### Usage Examples

#### Interactive Mode
```bash
source venv/bin/activate
python scripts/generate_meeting_minutes.py

# Follow prompts for:
# - Team name, project name, meeting number
# - Date, time, location
# - Attendees list
# - Agenda items with responsibilities and dates
# - Next meeting details
# - Output format selection (MD, DOCX, or both)
```

#### JSON Configuration Mode
```bash
# Create sample configuration
python scripts/generate_meeting_minutes.py --sample

# Edit config/sample_meeting_config.json to customize:
{
  "basic_info": {
    "team_name": "Team 46",
    "project_name": "Capstone Project I", 
    "meeting_number": "1",
    "date": "16/09/2025",
    "time": "1:30pm",
    "location": "Online"
  },
  "attendees": ["Steven", "Kathan", "Laurence", "Kenan", "Soroush"],
  "agenda_items": [
    {
      "item": "Project kickoff",
      "description": "Discuss project scope and timeline",
      "responsibility": "All team members",
      "planned_date": "20/09/2025", 
      "status": "0%",
      "actual_date": "TBD"
    }
  ],
  "next_meeting": {
    "date": "23/09/2025",
    "time": "1:30pm", 
    "location": "Online",
    "agenda": "Review requirements and assign tasks"
  },
  "output_formats": ["md", "docx"]
}

# Generate from configuration
python scripts/generate_meeting_minutes.py --json config/sample_meeting_config.json
```

#### Command Line Options
```bash
python scripts/generate_meeting_minutes.py --help           # Show help
python scripts/generate_meeting_minutes.py                  # Interactive mode  
python scripts/generate_meeting_minutes.py --sample         # Create sample config
python scripts/generate_meeting_minutes.py --json config/sample_meeting_config.json # Generate from JSON
```

### Output Structure
The generated documents include:
- **Header**: Team info, project name, meeting number, date/time/location
- **Attendees**: Complete list of team members
- **Agenda Table**: Items with descriptions, responsibilities, planned dates, status, actual dates
- **Next Meeting**: Date, time, location, agenda for next meeting
- **Signatures**: Signature lines for all attendees

## 📄 Document Converter

### Features
- ✅ **Multiple Formats**: Supports .doc and .docx files
- ✅ **Batch Processing**: Convert entire directories
- ✅ **Smart Detection**: Auto-finds Word documents
- ✅ **Cross-Platform**: Works on macOS, Linux, Windows
- ✅ **Conversion Log**: Detailed success/failure reporting

### Usage Examples

#### Convert All Documents
```bash
# Convert all Word docs in current directory
python scripts/convert_docs_to_md.py

# Convert all docs in templates directory
python scripts/convert_docs_to_md.py --directory templates/original

# Force overwrite existing Markdown files
python scripts/convert_docs_to_md.py --force
```

#### Convert Specific File
```bash
# Convert single file
python scripts/convert_docs_to_md.py --file templates/original/document.docx

# Convert with custom output name
python scripts/convert_docs_to_md.py --file templates/original/document.docx --output templates/markdown/custom_name.md
```

#### List and Analyze
```bash
# List all Word documents without converting
python scripts/convert_docs_to_md.py --list

# Show detailed conversion log
python scripts/convert_docs_to_md.py --verbose
```

#### Command Line Options
```bash
python scripts/convert_docs_to_md.py --help                    # Show help
python scripts/convert_docs_to_md.py                           # Convert all in current dir
python scripts/convert_docs_to_md.py --file templates/original/document.docx      # Convert specific file
python scripts/convert_docs_to_md.py --directory templates/original # Convert all in directory
python scripts/convert_docs_to_md.py --force                   # Overwrite existing files
python scripts/convert_docs_to_md.py --list                    # List documents only
python scripts/convert_docs_to_md.py --verbose                 # Show detailed log
```

### Conversion Methods
- **.docx files**: Direct conversion using `pandoc`
- **.doc files**: Two-step conversion using `textutil` (macOS) → `pandoc`

## 🛠️ Requirements

### System Requirements
- Python 3.6+
- pandoc (document conversion)
- textutil (macOS, for .doc files)

### Python Dependencies
```bash
pip install python-docx  # For Word document generation
```

### Installation Instructions

#### macOS
```bash
brew install pandoc
python3 -m venv venv
source venv/bin/activate
pip install python-docx
```

#### Ubuntu/Debian
```bash
sudo apt-get install pandoc
python3 -m venv venv
source venv/bin/activate
pip install python-docx
```

#### Windows
1. Download pandoc from https://pandoc.org/installing.html
2. Install Python 3.6+
3. Create virtual environment:
```cmd
python -m venv venv
venv\\Scripts\\activate
pip install python-docx
```


## 🎯 Use Cases

### Weekly Team Meetings
1. Use JSON configuration for recurring meetings
2. Update attendees, date, and agenda items
3. Generate both MD (for version control) and DOCX (for submission)

### Document Management
1. Convert all Word templates to Markdown for Git tracking
2. Maintain both formats for different use cases
3. Batch convert new documents as needed

### Project Documentation
1. Keep all templates in Markdown for easy editing
2. Generate professional Word documents when needed
3. Track changes in Git with Markdown versions

## ⚡ Quick Commands Cheat Sheet

```bash
# Setup (one time)
python3 -m venv venv && source venv/bin/activate && pip install python-docx

# Generate meeting minutes (interactive)
source venv/bin/activate && python scripts/generate_meeting_minutes.py

# Generate meeting minutes (from config)
python scripts/generate_meeting_minutes.py --json config/sample_meeting_config.json

# Convert all documents to Markdown
python scripts/convert_docs_to_md.py

# Convert specific document
python scripts/convert_docs_to_md.py --file templates/original/document.docx

# List all Word documents
python scripts/convert_docs_to_md.py --list

# Show help for any script
python script_name.py --help
```

## 🔧 Troubleshooting

### "pandoc not found"
```bash
# macOS
brew install pandoc

# Ubuntu
sudo apt-get install pandoc

# Windows
# Download from https://pandoc.org/installing.html
```

### "python-docx not installed"
```bash
source venv/bin/activate
pip install python-docx
```

### "externally-managed-environment" error
```bash
# Use virtual environment instead
python3 -m venv venv
source venv/bin/activate
pip install python-docx
```

### ".doc files not converting"
- macOS: Uses `textutil` (built-in)
- Linux/Windows: Convert .doc to .docx first, then use converter

## 📚 Additional Documentation

- [Meeting Generator Details](documentation/README_meeting_generator.md) - Comprehensive meeting minutes tool guide
- [COMP3059 Templates](templates/) - Original course templates in both Word and Markdown formats

## 🤝 Contributing

This project is for COMP3059 Capstone Project coursework. Team members can:
1. Update meeting configurations in `config/sample_meeting_config.json`
2. Add new document templates
3. Enhance script functionality
4. Improve documentation

## 📄 License

Created for COMP3059 Capstone Project course requirements at George Brown College.