#!/usr/bin/env python3
"""
Meeting Minutes Generator
Creates meeting minutes document based on COMP3059-F25-Minutes of Meeting-Template
Generates clean Markdown (.md) format for easy editing and version control
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
import os


class MeetingMinutesGenerator:
    def __init__(self):
        self.template_data = {}
    
    def collect_basic_info(self) -> Dict:
        """Collect basic meeting information"""
        print("=== Meeting Basic Information ===")
        
        team_name = input("Team name (default: Team 46): ").strip() or "Team 46"
        project_name = input("Project name (default: Capstone Project I): ").strip() or "Capstone Project I"
        meeting_number = input("Meeting number (default: 1): ").strip() or "1"
        
        # Date and time
        date_input = input("Meeting date (YYYY-MM-DD, default: today): ").strip()
        if not date_input:
            date = datetime.now().strftime("%d/%m/%Y")
        else:
            try:
                parsed_date = datetime.strptime(date_input, "%Y-%m-%d")
                date = parsed_date.strftime("%d/%m/%Y")
            except ValueError:
                print("Invalid date format, using today's date")
                date = datetime.now().strftime("%d/%m/%Y")
        
        time = input("Meeting time (default: 1:30pm): ").strip() or "1:30pm"
        location = input("Meeting location (default: n/a): ").strip() or "n/a"
        
        return {
            "team_name": team_name,
            "project_name": project_name,
            "meeting_number": meeting_number,
            "date": date,
            "time": time,
            "location": location
        }
    
    def collect_attendees(self) -> List[str]:
        """Collect meeting attendees"""
        print("\n=== Meeting Attendees ===")
        attendees = []
        
        print("Enter attendee names (press Enter with empty name to finish):")
        i = 1
        while True:
            name = input(f"Team member {i}: ").strip()
            if not name:
                break
            attendees.append(name)
            i += 1
        
        if not attendees:
            # Default attendees from template
            attendees = ["Steven", "Kathan", "Laurence", "Kenan", "Soroush"]
        
        return attendees
    
    def collect_agenda_items(self) -> List[Dict]:
        """Collect agenda items"""
        print("\n=== Agenda Items ===")
        agenda_items = []
        
        # Add default items
        agenda_items.extend([
            {
                "item": "Review of previous meeting",
                "description": "N/A",
                "responsibility": "N/A",
                "planned_date": "N/A",
                "status": "N/A",
                "actual_date": "N/A"
            },
            {
                "item": "Tasks Assigned as per previous meeting",
                "description": "N/A",
                "responsibility": "N/A", 
                "planned_date": "N/A",
                "status": "N/A",
                "actual_date": "N/A"
            }
        ])
        
        print("Enter additional agenda items (press Enter with empty item to finish):")
        i = 1
        while True:
            item_name = input(f"Item #{i} name: ").strip()
            if not item_name:
                break
            
            description = input(f"  Description: ").strip()
            responsibility = input(f"  Responsibility: ").strip()
            planned_date = input(f"  Planned completion date: ").strip()
            status = input(f"  Status (% done): ").strip()
            actual_date = input(f"  Actual completion date: ").strip()
            
            agenda_items.append({
                "item": item_name,
                "description": description,
                "responsibility": responsibility,
                "planned_date": planned_date,
                "status": status,
                "actual_date": actual_date
            })
            i += 1
        
        return agenda_items
    
    def collect_next_meeting(self) -> Dict:
        """Collect next meeting information"""
        print("\n=== Next Meeting Information ===")
        
        next_date = input("Next meeting date: ").strip()
        next_time = input("Next meeting time: ").strip()
        next_location = input("Next meeting location: ").strip()
        next_agenda = input("Next meeting agenda: ").strip()
        
        return {
            "date": next_date,
            "time": next_time,
            "location": next_location,
            "agenda": next_agenda
        }
    
    def generate_markdown(self, basic_info: Dict, attendees: List[str], 
                         agenda_items: List[Dict], next_meeting: Dict) -> str:
        """Generate the markdown meeting minutes"""
        
        # Header section
        markdown = f"""# Meeting Minutes

## {basic_info['team_name']} - {basic_info['project_name']}

**Minutes of Meeting # {basic_info['meeting_number']}**

**Date:** {basic_info['date']}  
**Time:** {basic_info['time']}  
**Location:** {basic_info['location']}

## Attendees

"""
        
        # Add attendees
        for i, attendee in enumerate(attendees, 1):
            markdown += f"- Team member {i}: {attendee}\n"
        
        # Agenda section
        markdown += "\n## Agenda\n\n"
        markdown += "| Item | Description | Responsibility | Planned Completion Date | Status (% done) | Actual Date |\n"
        markdown += "|------|-------------|----------------|------------------------|-----------------|-------------|\n"
        
        for item in agenda_items:
            markdown += f"| {item['item']} | {item['description']} | {item['responsibility']} | {item['planned_date']} | {item['status']} | {item['actual_date']} |\n"
        
        # Next meeting section
        markdown += f"\n## Next Meeting\n\n"
        markdown += f"**Date:** {next_meeting['date']}\n\n"
        markdown += f"**Time:** {next_meeting['time']}\n\n"
        markdown += f"**Location:** {next_meeting['location']}\n\n"
        markdown += f"**Agenda:** {next_meeting['agenda']}\n\n"
        
        # Signatures section
        markdown += "## Signatures\n\n"
        for i, attendee in enumerate(attendees, 1):
            markdown += f"**Team member {i} ({attendee}):** ___________________\n\n"
        
        return markdown
    
    
    def save_to_file(self, content: str, filename: Optional[str] = None) -> str:
        """Save the generated minutes to a Markdown file"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"meeting_minutes_{timestamp}.md"
        
        # Ensure .md extension
        if not filename.endswith('.md'):
            filename = f"{filename}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filename
    
    def generate_interactive(self) -> str:
        """Interactive generation of meeting minutes"""
        print("Welcome to Meeting Minutes Generator!")
        print("=" * 50)
        
        # Collect all information
        basic_info = self.collect_basic_info()
        attendees = self.collect_attendees()
        agenda_items = self.collect_agenda_items()
        next_meeting = self.collect_next_meeting()
        
        # Generate markdown content
        markdown_content = self.generate_markdown(basic_info, attendees, agenda_items, next_meeting)
        
        # Save to file
        filename = self.save_to_file(markdown_content)
        
        print(f"\n✅ Meeting minutes generated successfully!")
        print(f"📄 Saved to: {filename}")
        
        return filename
    
    def generate_from_json(self, json_file: str) -> str:
        """Generate meeting minutes from JSON configuration file"""
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        markdown_content = self.generate_markdown(
            data['basic_info'],
            data['attendees'],
            data['agenda_items'],
            data['next_meeting']
        )
        
        # Get filename (remove extension if provided and ensure .md)
        filename = data.get('output_filename', 'meeting_minutes')
        if filename.endswith('.docx'):
            filename = os.path.splitext(filename)[0]
        
        filename = self.save_to_file(markdown_content, filename)
        return filename


def create_sample_json():
    """Create a sample JSON configuration file"""
    sample_data = {
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
        "output_filename": "sample_meeting_minutes"
    }
    
    with open('sample_meeting_config.json', 'w', encoding='utf-8') as f:
        json.dump(sample_data, f, indent=2)
    
    print("✅ Sample configuration saved to: sample_meeting_config.json")


def main():
    """Main function with command line interface"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] in ["-h", "--help"]:
        print("Meeting Minutes Generator")
        print("=" * 40)
        print("Usage:")
        print("  python generate_meeting_minutes.py                    # Interactive mode")
        print("  python generate_meeting_minutes.py --json config.json # Generate from JSON")
        print("  python generate_meeting_minutes.py --sample           # Create sample config")
        print("  python generate_meeting_minutes.py --help             # Show this help")
        print()
        print("Output format:")
        print("  - Markdown (.md) - Clean, readable format for easy editing and version control")
        return
    
    generator = MeetingMinutesGenerator()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--sample":
            create_sample_json()
            return
        elif sys.argv[1] == "--json":
            if len(sys.argv) < 3:
                print("Usage: python generate_meeting_minutes.py --json <config_file.json>")
                return
            filename = generator.generate_from_json(sys.argv[2])
            print(f"✅ Meeting minutes generated from JSON: {filename}")
            return
    
    # Interactive mode
    generator.generate_interactive()


if __name__ == "__main__":
    main()