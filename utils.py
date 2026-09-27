def format_response(data, metadata):
    """
    Format a standard API response.
    Changed: Now requires metadata to be passed.
    """
    return {
        "success": True,
        "data": data,
        "metadata": metadata,
        "error": None
    }
