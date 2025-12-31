"""Script to organize the repo into logical folders."""
import os
import shutil
from pathlib import Path

def organize_repo():
    repo_root = Path(__file__).parent.parent
    
    # Define folder structure and file mappings
    folders = {
        "company": [],          # Company info, bios, pitch materials
        "applications": [],     # Applications for conferences, competitions, awards
        "conferences": [],      # Conference tracking, registration lists
        "contacts": [],         # Contact lists, networking, attendees
        "press-media": [],      # Press outlets, influencers, PR
        "resources": [],        # Community resources, research
        "archive": [],          # Old/historical files (2022, etc.)
    }
    
    # File categorization rules
    file_mapping = {
        # Company core materials
        "ATDev C Suite Bios.md": "company",
        "pitch application_.md": "company",
        "ATDev - MedInvest MedTech Conference - Information Request.md": "company",
        "medinvest Investor message_.md": "company",
        "Application_.md": "company",
        
        # Applications (awards, competitions, conferences)
        "SXSW 2026 Application.md": "applications",
        "Eureka Park Accessibility contest application_.md": "applications",
        "2026 Global Innovation Awards.md": "applications",
        "CTA Match.md": "applications",
        "Tech and Society Draft 1.md": "applications",
        "Reflex_AOSSM_Marketing_Plan.md": "applications",
        
        # Conference tracking
        "2025 Conferences.csv": "conferences",
        "2026 Conferences_updated_Conference List.csv": "conferences",
        "2026 Conferences_updated_Conference List 2026.csv": "conferences",
        "2026 Conferences_updated_Log-in Information.csv": "conferences",
        "2026 Conferences_updated_CES Tasks.csv": "conferences",
        "HLTH 2025 Master Sheet_Tasks.csv": "conferences",
        "HLTH 2025 Master Sheet_Companies to meet.csv": "conferences",
        
        # Contacts and networking
        "AOSSM 2025 AM Professional Registrants 6.20.25.csv": "contacts",
        "APTA Contact List.csv": "contacts",
        "APTA Future of Rehab 2025 Registration List_.csv": "contacts",
        "HLTH_2025_Attendees_with_LinkedIn_Search.csv": "contacts",
        "Wheelchair Survey Contact List_Wheelchair Survey Contact List .csv": "contacts",
        "Wheelchair Survey Contact List_(old) I-Corps Call Tracker.csv": "contacts",
        "Wheelchair Survey Contact List_Sheet3.csv": "contacts",
        "Wheelchair Survey Contact List_Social Groups.csv": "contacts",
        "Mailchimp Import_Sheet1.csv": "contacts",
        "Mailchimp Import_Sheet2.csv": "contacts",
        "Wilson Sonsini Networking.md": "contacts",
        "Potential Podcast Guests.csv": "contacts",
        
        # Press and media
        "Press_News Outlets for PR_final_News Outlets.csv": "press-media",
        "Press_News Outlets for PR_final_PR Firms.csv": "press-media",
        "Press_News Outlets for PR_final_Influecers.csv": "press-media",
        "all_news_outlets_with_contacts.csv": "press-media",
        "CES26_Press_Release_List_2025-12-01.csv": "press-media",
        "At Dev Potential Health Tech Influencers.csv": "press-media",
        
        # Resources
        "Assorted Caregiving Community Resources_GENERAL.csv": "resources",
        "Assorted Caregiving Community Resources_BLACK, LATINE, POC.csv": "resources",
        "Assorted Caregiving Community Resources_LGBTQIA .csv": "resources",
        "Assorted Caregiving Community Resources_OLDER ADULTS.csv": "resources",
        "Assorted Caregiving Community Resources_ALS .csv": "resources",
        "Assorted Caregiving Community Resources_ILM Videos.csv": "resources",
        "Assorted Caregiving Community Resources_Template.csv": "resources",
        
        # Archive (historical)
        "CureSMA 2022 Networking.md": "archive",
        "HLTH VIVE 2022 Registeration.md": "archive",
    }
    
    # Create folders
    for folder in folders.keys():
        (repo_root / folder).mkdir(exist_ok=True)
    
    # Move files
    for filename, destination in file_mapping.items():
        src = repo_root / filename
        if src.exists():
            dst = repo_root / destination / filename
            shutil.move(str(src), str(dst))
            print(f"Moved: {filename} -> {destination}/")
        else:
            print(f"Not found: {filename}")
    
    # Move Competitions folder contents to applications
    competitions_dir = repo_root / "Competitions"
    if competitions_dir.exists():
        for item in competitions_dir.iterdir():
            if item.suffix in ['.md', '.csv']:
                dst = repo_root / "applications" / item.name
                shutil.move(str(item), str(dst))
                print(f"Moved: Competitions/{item.name} -> applications/")
    
    # Move Digital Health Awards application contents to applications
    dha_dir = repo_root / "Digital Health Awards application"
    if dha_dir.exists():
        for item in dha_dir.iterdir():
            if item.suffix in ['.md', '.csv']:
                dst = repo_root / "applications" / item.name
                shutil.move(str(item), str(dst))
                print(f"Moved: Digital Health Awards application/{item.name} -> applications/")
    
    print("\n=== Organization complete ===")

if __name__ == "__main__":
    organize_repo()
