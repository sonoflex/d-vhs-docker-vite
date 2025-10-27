FROM node:20

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 5173

# direkt npx Vite starten
CMD ["npx", "vite", "--host", "0.0.0.0", "--port", "5173"]