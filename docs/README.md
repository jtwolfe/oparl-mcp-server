# OParl MCP Server Documentation

This directory contains the Jekyll-based documentation for the OParl MCP Server project.

## Local Development

To run the documentation locally:

```bash
cd docs
bundle install
bundle exec jekyll serve --baseurl=""
```

Then open [http://localhost:4000](http://localhost:4000) in your browser.

## Structure

- `_config.yml` - Jekyll configuration
- `_pages/` - Documentation pages organized by section
- `_layouts/` - Custom page layouts
- `_includes/` - Reusable components
- `index.md` - Homepage

## Deployment

The documentation is automatically built and deployed to GitHub Pages when changes are pushed to the main branch.

The site will be available at: https://jtwolfe.github.io/oparl-mcp-server
