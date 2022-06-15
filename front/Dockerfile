FROM node:16.15.1

WORKDIR /app
RUN npm install -g @vue/cli
COPY ./package.json /app/package.json
RUN npm install
CMD ["npm", "run", "serve"]