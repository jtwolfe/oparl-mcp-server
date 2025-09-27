# GitHub Pages Setup Guide

This guide explains how to configure GitHub Pages for the OParl MCP Server documentation with a subdomain.

## Repository Configuration

### 1. Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select **GitHub Actions**
4. The documentation will be built and deployed automatically

### 2. Repository Settings

The repository should be configured with:

- **Repository name**: `oparl-mcp-server`
- **Owner**: `jtwolfe`
- **Visibility**: Public (required for GitHub Pages)
- **Default branch**: `main`

### 3. Custom Domain (Optional)

If you want to use a custom domain instead of the GitHub subdomain:

1. In **Settings** → **Pages**
2. Enter your custom domain in the **Custom domain** field
3. Add a `CNAME` file to the `docs/` directory with your domain

## Jekyll Configuration

The Jekyll site is configured for the subdomain `jtwolfe.github.io/oparl-mcp-server`:

### Key Configuration Points

1. **Base URL**: Set to `/oparl-mcp-server` in `_config.yml`
2. **URL**: Set to `https://jtwolfe.github.io`
3. **Theme**: Uses GitHub Pages compatible Minima theme
4. **Plugins**: Includes GitHub Pages compatible plugins

### File Structure

```
docs/
├── _config.yml          # Jekyll configuration
├── Gemfile              # Ruby dependencies
├── index.md             # Homepage
├── _pages/              # Documentation pages
│   ├── getting-started/
│   ├── user-guide/
│   ├── api/
│   ├── development/
│   └── about/
├── _layouts/            # Custom layouts
├── _includes/           # Reusable components
└── README.md            # Documentation README
```

## GitHub Actions Workflow

The `.github/workflows/docs-jekyll.yml` workflow:

1. **Triggers** on pushes to `main` and `dev` branches
2. **Builds** the Jekyll site with proper base URL
3. **Deploys** to GitHub Pages automatically
4. **Uses** GitHub Pages deployment action

### Workflow Features

- **Ruby 3.1** environment
- **Bundler** for dependency management
- **Jekyll build** with subdomain base URL
- **Automatic deployment** to GitHub Pages
- **Artifact upload** for build results

## Accessing the Documentation

Once deployed, the documentation will be available at:

**Primary URL**: https://jtwolfe.github.io/oparl-mcp-server

### Navigation Structure

- **Home**: https://jtwolfe.github.io/oparl-mcp-server/
- **Getting Started**: https://jtwolfe.github.io/oparl-mcp-server/getting-started/quickstart/
- **User Guide**: https://jtwolfe.github.io/oparl-mcp-server/user-guide/overview/
- **API Reference**: https://jtwolfe.github.io/oparl-mcp-server/api/server/
- **Development**: https://jtwolfe.github.io/oparl-mcp-server/development/contributing/
- **About**: https://jtwolfe.github.io/oparl-mcp-server/about/license/

## Local Development

Since you're on an atomic OS, local Jekyll development isn't possible. However, you can:

1. **Edit documentation** in the `docs/` directory
2. **Preview changes** by pushing to a branch
3. **Use GitHub's preview** for pull requests
4. **Check the Actions tab** for build status

## Troubleshooting

### Common Issues

1. **Build Failures**: Check the Actions tab for error details
2. **Missing Pages**: Ensure files have proper front matter
3. **Broken Links**: Use `{{ '/path' | relative_url }}` for internal links
4. **Styling Issues**: Verify theme configuration in `_config.yml`

### Debugging Steps

1. **Check Actions logs** in the GitHub repository
2. **Verify file structure** matches Jekyll requirements
3. **Test YAML syntax** in `_config.yml`
4. **Validate front matter** in markdown files

## Maintenance

### Regular Tasks

1. **Update dependencies** in `Gemfile`
2. **Test documentation** after major changes
3. **Monitor build status** in Actions
4. **Update links** when restructuring

### Adding New Pages

1. Create markdown file in appropriate `_pages/` subdirectory
2. Add front matter with title, description, and permalink
3. Update navigation in `_includes/navigation.html` if needed
4. Test the build by pushing changes

## Security Considerations

- **No sensitive data** in documentation
- **Public repository** required for GitHub Pages
- **Automated builds** from main branch only
- **Review process** for documentation changes

## Performance

- **Static site** for fast loading
- **CDN delivery** via GitHub Pages
- **Minified assets** by Jekyll
- **Optimized images** recommended

This setup provides a professional, maintainable documentation site that integrates seamlessly with GitHub's infrastructure.
