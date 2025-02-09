FROM node:20-alpine

RUN mkdir -p /opt/app/ps-client

WORKDIR /opt/app/ps-client

# install app dependencies
COPY package.json .
# COPY package-lock.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD [ "npm", "run", "dev"]