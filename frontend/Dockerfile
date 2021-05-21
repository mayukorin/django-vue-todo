FROM node:12.14.1

WORKDIR /todo-docker/frontend
RUN npm install -g @vue/cli 
COPY  ./package*.json /todo-docker/frontend/
RUN npm install
COPY . .
RUN npm run build
EXPOSE 8080