# Import the parent image
FROM node:18-alpine
# Specify working directory
WORKDIR /app
# Copy over requirements/dependencies file
COPY package.json .
# Install dependencies
RUN npm install
# Copy over your app files
COPY . .
# Run the app
CMD ["npm", "run", "dev"]

