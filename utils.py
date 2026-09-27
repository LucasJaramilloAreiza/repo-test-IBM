def format_response(data):
    """
    Format a standard API response.
    """
    return {
        "success": True,
        "data": data,
        "error": None
    }
