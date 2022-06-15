FROM node:16.15.1

WORKDIR /app
RUN npm install -g @vue/cli
ADD ./doko-yahoo/package.json /app/package.json
RUN npm install
ADD ./start.sh /app/start.sh
