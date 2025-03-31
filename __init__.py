"""
AI Services Package - Provides unified access to various AI services for the Resume AI application
"""

from utils.ai_services.service_manager import AIServiceManager

# Create a singleton instance of the service manager
service_manager = AIServiceManager()

# Export the get_service function for easy access
def get_service(service_name):
    """
    Get an AI service by name
    
    Args:
        service_name (str): Name of the service to get
        
    Returns:
        object: Service instance or None if not available
    """
    return service_manager.get_service(service_name) 