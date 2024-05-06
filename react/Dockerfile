FROM node:14-alpine

WORKDIR /app

# Install dependencies
COPY package.json /app/
COPY yarn.lock /app/
RUN yarn install --frozen-lockfile

# Copy project
COPY . /app

# Build app
RUN yarn build

# Use Nginx for serving the build
FROM nginx:1.19-alpine
COPY --from=0 /app/build /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf