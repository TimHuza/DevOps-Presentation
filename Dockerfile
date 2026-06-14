FROM node:18-alpine

WORKDIR /app

COPY server/package*.json ./server/

RUN cd server && npm ci --only=production

COPY server/ ./server/

COPY register.html ./

EXPOSE 3001

CMD ["node", "server/index.js"]