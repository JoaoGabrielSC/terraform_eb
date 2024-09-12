from dotenv import load_dotenv
# Load environment variables
load_dotenv()

import os
import traceback


import io
import uvicorn
from mangum import Mangum
from fastapi import Body, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

from entities.services.eb_service import enable_event_rule, disable_event_rule

print("=== API IS STARTING ===")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/relaunch-eventbus")
def relaunch_event_bus():
    try:
        response = enable_event_rule()
        return {'status_code':'200','response': response}
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

@app.get("/stop-eventbus}")
def stop_event_bus():
    try:
        response = disable_event_rule()
        # check 
        return {'status_code':'200','response': response}
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}

@app.get("/test/{input}")
def test(input: str):
    response = f'You have entered {input}'
    return {"input": response}

handler = Mangum(app, lifespan="off")


if __name__ == "__main__":
    print("=== API IS RUNNING ===")
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"
    uvicorn.run(uvicorn_app, host="0.0.0.0", port=3000, reload=True)
