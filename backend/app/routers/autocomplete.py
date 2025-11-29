from fastapi import APIRouter
from app.schemas import AutocompleteRequest, AutocompleteResponse

router = APIRouter(prefix="/autocomplete", tags=["autocomplete"])


def mock_autocomplete(code: str, cursor_pos: int, language: str) -> str:
    """
    Generate a mocked autocomplete suggestion based on code context.
    
    Simple rule-based approach:
    - If ending with 'def', suggest function definition
    - If ending with 'class', suggest class definition
    - If ending with 'import', suggest import statement
    - Otherwise, suggest a common pattern
    """
    lines = code[:cursor_pos].split('\n')
    current_line = lines[-1] if lines else ""
    
    if current_line.strip().endswith('def'):
        return " my_function(args):\n    pass"
    elif current_line.strip().endswith('class'):
        return " MyClass:\n    pass"
    elif current_line.strip().endswith('import'):
        return " os"
    elif current_line.strip().endswith('for'):
        return " item in items:\n    pass"
    elif current_line.strip().endswith('if'):
        return " condition:\n    pass"
    else:
        # Default suggestion based on language
        if language == "python":
            return "  # Add your code here"
        elif language == "javascript":
            return "  // Add your code here"
        else:
            return "  # suggestion"


@router.post("/", response_model=AutocompleteResponse)
async def get_autocomplete(request: AutocompleteRequest):
    """
    Return a mocked autocomplete suggestion.
    
    Request body:
    {
        "code": "...",
        "cursorPosition": 0,
        "language": "python"
    }
    """
    suggestion = mock_autocomplete(request.code, request.cursorPosition, request.language)
    return AutocompleteResponse(suggestion=suggestion)
