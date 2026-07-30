# Use a Python base image compatible with your CodeShield pipeline
FROM python:3.11-slim                     
# Prevent Python from buffering output  
ENV PYTHONUNBUFFERED=1                 
# Set working directory        
WORKDIR /app                   
# Copy dependency file first for Docker layer caching    
COPY requirements.txt .                                 
# Upgrade pip and install dependencies                  
RUN pip install --upgrade pip && \                    
pip install --no-cache-dir -r requirements.txt       
# Copy the application source                        
COPY . .                                             
# Expose the default Flask port                      
EXPOSE 5000                                          
# Start the application                              
CMD ["python", "app.py"]
