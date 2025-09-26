# Deployment

Deployment options and guidelines for OParl MCP Server.

## Docker Deployment

### Build Image
```bash
docker build -f docker/Dockerfile -t oparl-mcp-server .
```

### Run Container
```bash
docker run -p 8000:8000 oparl-mcp-server
```

### With Environment Variables
```bash
docker run -p 8000:8000 \
  -e OPARL_BASE_URL=https://oparl.muenchen.de \
  -e OPARL_API_KEY=your-key \
  oparl-mcp-server
```

## Docker Compose

```yaml
version: '3.8'
services:
  oparl-mcp-server:
    image: oparl-mcp-server:latest
    ports:
      - "8000:8000"
    environment:
      - OPARL_BASE_URL=https://oparl.muenchen.de
      - OPARL_API_KEY=your-key
      - OPARL_TIMEOUT=60.0
    restart: unless-stopped
```

## Production Deployment

### Environment Setup
```bash
# Create production environment
python -m venv venv
source venv/bin/activate
pip install oparl-mcp-server
```

### Configuration
Create production configuration:

```env
OPARL_BASE_URL=https://api.oparl.org
OPARL_API_KEY=your-production-key
OPARL_TIMEOUT=60.0
OPARL_LOG_LEVEL=INFO
OPARL_SERVER_NAME=Production OParl Server
```

### Process Management
Use systemd or similar for process management:

```ini
[Unit]
Description=OParl MCP Server
After=network.target

[Service]
Type=simple
User=oparl
WorkingDirectory=/opt/oparl-mcp-server
Environment=PATH=/opt/oparl-mcp-server/venv/bin
ExecStart=/opt/oparl-mcp-server/venv/bin/python -m oparl_mcp
Restart=always

[Install]
WantedBy=multi-user.target
```

## Cloud Deployment

### AWS ECS
- Use the provided Dockerfile
- Configure environment variables
- Set up load balancing if needed

### Google Cloud Run
- Deploy as containerized service
- Configure environment variables
- Set up monitoring

### Azure Container Instances
- Deploy using Azure CLI
- Configure environment variables
- Set up logging

## Monitoring

### Health Checks
The server provides health check endpoints:
- `/health` - Basic health status
- `/metrics` - Performance metrics

### Logging
Configure structured logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Security Considerations

- Use HTTPS in production
- Secure API keys and secrets
- Regular security updates
- Network isolation
- Access controls
