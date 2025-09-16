# Meeting Minutes Generator

A Python script that generates professional meeting minutes in both Markdown (.md) and Word Document (.docx) formats based on the COMP3059-F25-Minutes of Meeting-Template.

## Features

- ✅ **Dual Format Output**: Generates both Markdown and Word Document formats
- ✅ **Interactive Mode**: User-friendly prompts for all meeting details
- ✅ **JSON Configuration**: Batch generation from predefined JSON files
- ✅ **Template Compliance**: Follows the exact structure of COMP3059-F25 template
- ✅ **Customizable**: Supports custom attendees, agenda items, and meeting details

## Requirements

- Python 3.6+
- `python-docx` library (for Word document generation)

## Installation

### Option 1: Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate
pip install python-docx
```

### Option 2: System-wide Installation
```bash
pip install --user python-docx
```

## Usage

### Interactive Mode
```bash
# With virtual environment
source venv/bin/activate && python generate_meeting_minutes.py

# Without virtual environment (MD only)
python generate_meeting_minutes.py
```

### JSON Configuration Mode
```bash
# Generate sample configuration
python generate_meeting_minutes.py --sample

# Use existing configuration
python generate_meeting_minutes.py --json sample_meeting_config.json
```

### Help
```bash
python generate_meeting_minutes.py --help
```

## JSON Configuration Format

```json
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
      "item": "Review of previous meeting",
      "description": "N/A",
      "responsibility": "N/A",
      "planned_date": "N/A",
      "status": "N/A",
      "actual_date": "N/A"
    },
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
    "agenda": "Review project requirements and assign initial tasks"
  },
  "output_filename": "sample_meeting_minutes",
  "output_formats": ["md", "docx"]
}
```

## Output Formats

### Markdown (.md)
- Clean, readable format
- Compatible with all Markdown processors
- Easy to convert to other formats
- Version control friendly

### Word Document (.docx)
- Professional appearance
- Formatted tables and headers
- Ready for printing/sharing
- Compatible with Microsoft Word

## File Structure

```
.
├── generate_meeting_minutes.py       # Main script
├── sample_meeting_config.json        # Sample configuration
├── venv/                            # Virtual environment
├── sample_meeting_minutes.md         # Generated markdown
├── sample_meeting_minutes.docx       # Generated Word doc
└── README_meeting_generator.md       # This file
```

## Template Compliance

The generated documents follow the exact structure of `COMP3059-F25-Minutes of Meeting-Template.docx`:

- **Header Section**: Team name, project name, meeting number, date, time, location
- **Attendees Section**: List of all team members
- **Agenda Table**: Items with descriptions, responsibilities, dates, and status
- **Next Meeting Section**: Date, time, location, and agenda for next meeting  
- **Signature Section**: Spaces for all team member signatures

## Troubleshooting

### "python-docx not installed" Warning
- Install python-docx: `pip install python-docx`
- Or use virtual environment as shown above
- Script will still work for Markdown generation

### "externally-managed-environment" Error
- Use virtual environment instead of system-wide installation
- Or use `pip install --user python-docx`

## Examples

### Quick Start
```bash
# Create sample config
python generate_meeting_minutes.py --sample

# Generate both formats
source venv/bin/activate
python generate_meeting_minutes.py --json sample_meeting_config.json
```

### Custom Meeting
```bash
# Interactive mode with format selection
source venv/bin/activate
python generate_meeting_minutes.py
```

## License

This script is created for COMP3059 Capstone Project course requirements.