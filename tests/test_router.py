import pytest
from unittest.mock import MagicMock, patch
from core.router import CoreSwitchyardRouter

@pytest.fixture
def mock_openai_response():
    """Generates a mock OpenAI completion response object."""
    mock_res = MagicMock()
    mock_res.choices = [
        MagicMock(message=MagicMock(content="[HAZARD ASSESSMENT]: All nominal.\n[ACTION PLAN]: None.\n[SAFETY CLEARANCE SIGN-OFF]: STATUS: Approved"))
    ]
    return mock_res

@pytest.mark.asyncio
async def test_switchyard_routing_fallback_and_completion(mock_openai_response):
    """
    Verifies that CoreSwitchyardRouter correctly invokes Switchyard's step loop 
    and handles client completion responses.
    """
    router = CoreSwitchyardRouter()
    
    # Patch all client endpoints in the router with mock responses
    for key in router.clients:
        router.clients[key].chat.completions.create = MagicMock(return_value=mock_openai_response)
        
    model_used, result = await router.route_async("Routine telemetry check on Cabinet B.")
    
    assert model_used is not None
    assert "HAZARD ASSESSMENT" in result
    assert "STATUS: Approved" in result

def test_sync_router_wrapper(mock_openai_response):
    """Verifies that the synchronous .route() wrapper correctly executes the async loop."""
    router = CoreSwitchyardRouter()
    
    for key in router.clients:
        router.clients[key].chat.completions.create = MagicMock(return_value=mock_openai_response)
        
    model_used, result = router.route("Verify upper flange bolt structural stress.")
    assert model_used is not None
    assert len(result) > 0