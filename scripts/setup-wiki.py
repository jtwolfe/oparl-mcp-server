#!/usr/bin/env python3
"""
GitHub Wiki Setup Script

This script helps set up the GitHub Wiki with content from the documentation.
Since GitHub Wiki cannot be edited directly via repository, this script:
1. Generates wiki content from documentation files
2. Creates templates for manual wiki updates
3. Provides instructions for manual wiki setup

Usage:
    python scripts/setup-wiki.py
"""

import os
import json
from pathlib import Path
from typing import Dict, List

def create_wiki_structure():
    """Create wiki directory structure and content."""
    
    wiki_dir = Path("wiki")
    wiki_dir.mkdir(exist_ok=True)
    
    # Wiki structure
    wiki_pages = {
        "Home.md": "docs/en/index.md",
        "Getting-Started.md": "docs/en/getting-started/installation.md",
        "Installation.md": "docs/en/getting-started/installation.md",
        "Configuration.md": "docs/en/getting-started/configuration.md",
        "API-Reference.md": "docs/en/api/server.md",
        "Examples.md": "docs/en/user-guide/examples.md",
        "Contributing.md": "docs/en/development/contributing.md",
        "License.md": "docs/en/about/license.md",
        
        # German pages
        "Startseite.md": "docs/de/index.md",
        "Erste-Schritte.md": "docs/de/getting-started/installation.md",
        "Installation-DE.md": "docs/de/getting-started/installation.md",
        "Konfiguration.md": "docs/de/getting-started/configuration.md",
        "API-Referenz.md": "docs/de/api/server.md",
        "Beispiele.md": "docs/de/user-guide/examples.md",
        "Beitragen.md": "docs/de/development/contributing.md",
        "Lizenz.md": "docs/de/about/license.md",
    }
    
    # Create wiki pages
    for wiki_file, source_file in wiki_pages.items():
        if Path(source_file).exists():
            with open(source_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Convert markdown links for wiki
            content = convert_links_for_wiki(content)
            
            with open(wiki_dir / wiki_file, 'w', encoding='utf-8') as f:
                f.write(content)
    
    # Create wiki setup instructions
    create_wiki_instructions(wiki_dir)
    
    print(f"✅ Wiki content generated in {wiki_dir}/")
    print("📝 Manual setup required - see wiki-setup-instructions.md")

def convert_links_for_wiki(content: str) -> str:
    """Convert markdown links to wiki format."""
    # This is a basic conversion - may need more sophisticated handling
    content = content.replace("](getting-started/", "](Getting-Started-")
    content = content.replace("](api/", "](API-Reference-")
    content = content.replace("](development/", "](Contributing-")
    content = content.replace("](about/", "](License-")
    content = content.replace(".md)", ")")
    return content

def create_wiki_instructions(wiki_dir: Path):
    """Create instructions for manual wiki setup."""
    
    instructions = """# GitHub Wiki Setup Instructions

## Overview

This directory contains generated wiki content that needs to be manually uploaded to the GitHub Wiki.

## Manual Setup Steps

1. **Enable GitHub Wiki**:
   - Go to your repository on GitHub
   - Click on "Settings" tab
   - Scroll down to "Features" section
   - Check "Wikis" to enable it

2. **Create Wiki Pages**:
   - Go to the "Wiki" tab in your repository
   - Click "Create the first page"
   - Copy content from the generated files in this directory

3. **Page Structure**:
   - **Home.md** → Main wiki page
   - **Getting-Started.md** → Getting started guide
   - **Installation.md** → Installation instructions
   - **Configuration.md** → Configuration guide
   - **API-Reference.md** → API documentation
   - **Examples.md** → Usage examples
   - **Contributing.md** → Contributing guidelines
   - **License.md** → License information

4. **German Pages**:
   - **Startseite.md** → Hauptseite (Deutsch)
   - **Erste-Schritte.md** → Erste Schritte (Deutsch)
   - **Installation-DE.md** → Installation (Deutsch)
   - **Konfiguration.md** → Konfiguration (Deutsch)
   - **API-Referenz.md** → API-Dokumentation (Deutsch)
   - **Beispiele.md** → Verwendungsbeispiele (Deutsch)
   - **Beitragen.md** → Beitragsrichtlinien (Deutsch)
   - **Lizenz.md** → Lizenzinformationen (Deutsch)

## Automation Options

Since GitHub Wiki cannot be automated directly, consider these alternatives:

1. **GitHub Pages**: Use the documentation site instead
2. **External Wiki**: Use tools like Notion, GitBook, or Confluence
3. **Documentation Site**: Deploy MkDocs or Sphinx site
4. **README Updates**: Keep main documentation in repository

## Maintenance

- Update wiki content manually when documentation changes
- Use this script to regenerate content from documentation
- Consider migrating to GitHub Pages for automated updates

## Generated Files

The following files have been generated for manual upload:
"""
    
    # List generated files
    for file in sorted(wiki_dir.glob("*.md")):
        if file.name != "wiki-setup-instructions.md":
            instructions += f"- `{file.name}`\n"
    
    with open(wiki_dir / "wiki-setup-instructions.md", 'w', encoding='utf-8') as f:
        f.write(instructions)

def create_github_pages_alternative():
    """Create GitHub Pages as alternative to wiki."""
    
    pages_dir = Path("docs")
    
    # Create GitHub Pages configuration
    pages_config = {
        "name": "OParl MCP Server Documentation",
        "description": "Model Context Protocol server for OParl API",
        "url": "https://oparl-mcp-team.github.io/oparl-mcp-server",
        "baseurl": "/oparl-mcp-server",
        "markdown": "kramdown",
        "highlighter": "rouge",
        "theme": "minima",
        "plugins": ["jekyll-feed", "jekyll-sitemap"],
        "exclude": ["node_modules", "Gemfile.lock", "README.md"]
    }
    
    with open(pages_dir / "_config.yml", 'w', encoding='utf-8') as f:
        f.write("---\n")
        for key, value in pages_config.items():
            if isinstance(value, str):
                f.write(f"{key}: \"{value}\"\n")
            else:
                f.write(f"{key}: {value}\n")
        f.write("---\n")
    
    print("✅ GitHub Pages configuration created")
    print("📝 Enable GitHub Pages in repository settings")

if __name__ == "__main__":
    print("🚀 Setting up GitHub Wiki content...")
    create_wiki_structure()
    create_github_pages_alternative()
    print("\n📋 Next steps:")
    print("1. Enable GitHub Wiki in repository settings")
    print("2. Manually upload generated wiki content")
    print("3. Or enable GitHub Pages for automated documentation")
    print("\n🔗 See wiki-setup-instructions.md for detailed steps")
