FROM nginx:alpine

# Copy all static files to nginx's default serve directory
COPY . /usr/share/nginx/html

# Remove the Dockerfile itself from the served files
RUN rm /usr/share/nginx/html/Dockerfile

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
