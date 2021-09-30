FROM node:latest
ENV GQL_ENDPOINT=http://backend:4000/graphql
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build
CMD npm run start
