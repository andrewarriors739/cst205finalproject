# ----
# Study Buddy App - Image Processing Utilities
# CST 205 Design Project - Study Organization & Matching App
# Members: Alexis Chavarria, Anthony Jordan Lagura, James Lindfors, Andre Gutierrez
# Date : 7/25/25
# ----

import base64
import io
from PIL import Image

class ImageService:
    """Service for handling profile picture upload and processing"""
    
    @staticmethod
    def process_profile_picture(file):
        """
        Process uploaded image file: resize to standard size and convert to base64
        Args:
            file: FileStorage object from Flask request
        Returns:
            str: Base64 encoded image string, or None if processing fails
        """
        try:
            # Open the image
            image = Image.open(file.stream)
            
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize to (150x150)
            size = (150, 150)
            image = image.resize(size, Image.Resampling.LANCZOS)
            
            # Save to bytes buffer
            buffer = io.BytesIO()
            image.save(buffer, format='PNG', quality=85)
            buffer.seek(0)
            
            # Encode to base64
            base64_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
            
            return f"data:image/jpeg;base64,{base64_string}"
            
        except Exception as e:
            print(f"Error processing image: {e}")
            return None
    
    @staticmethod
    def is_valid_image(file):
        """
        Check if uploaded file is a valid image
        Args:
            file: FileStorage object from Flask request
        Returns:
            bool: True if valid image, False otherwise
        """
        if not file or not file.filename:
            return False
        
        # Check file extension
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
        file_extension = file.filename.rsplit('.', 1)[-1].lower()
        
        if file_extension not in allowed_extensions:
            return False
        
        try:
            Image.open(file.stream)
            
            # Reset stream position
            file.stream.seek(0)
            return True
        except Exception:
            return False
