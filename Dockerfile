FROM node:18-alpine

WORKDIR /app

# Copy server package manifest files first to leverage Docker caching
COPY server/package*.json ./server/

# Install server dependencies
RUN cd server && npm ci --only=production

# Copy the server source code
COPY server/ ./server/

# Copy the email template and assets
COPY email/ ./email/

# Copy the register.html file (since server/index.js looks for it at '../register.html')
COPY register.html ./

# Expose the server port
EXPOSE 3001

# Start the server
CMD ["node", "server/index.js"]