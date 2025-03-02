FROM node:20.18.3

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5137

CMD ["npm", "run", "dev"]