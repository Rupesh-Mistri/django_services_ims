FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
# RUN npm install

# Copy project files
COPY . .

# Expose the port
EXPOSE 3000

# Start the React app
#CMD ["npm", "start"]
CMD ["sh", "-c", "npm install && npm start"]

