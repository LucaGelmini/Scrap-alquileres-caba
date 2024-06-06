FROM python:3.10.14-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make the output directory
RUN mkdir -p /usr/src/app/output

# Define environment variable for output directory
ENV OUTPUT_DIR=/usr/src/app/output

# Copy output files to a server folder and then close
CMD ["sh", "-c", "python scraper.py && cp -r /usr/src/app/output/* /server/folder/ && echo 'Files copied to server folder'"]
