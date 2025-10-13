FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY oparl_openapi.json .

# Copy entrypoint script
COPY docker/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Create non-root user
RUN useradd --create-home --shell /bin/bash oparl
USER oparl

# Expose port (if needed for MCP over HTTP)
EXPOSE 8000

# Set environment variables
ENV PYTHONPATH=/app/src
ENV OPARL_BASE_URL=https://api.oparl.org
ENV OPARL_LOG_LEVEL=INFO

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.path.insert(0, '/app/src'); from oparl_mcp.server import OParlMCPServer; print('OK')" || exit 1

# Run the entrypoint script
CMD ["./entrypoint.sh"]
