#production Dockerfile

FROM node:alpine as builder

WORKDIR '/usr/app'

COPY package.json .
RUN npm install
COPY . .

RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache
RUN npm run build

#creating an ngnix image from build resources for deployment
FROM nginx
# exposing the 80 port for incoming traffic to the container
#mainly used during automatic delployment from service provider like AWS
EXPOSE 80

COPY --from=builder /usr/app/build /usr/share/nginx/html


