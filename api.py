from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel
from src.TextSummarizer.pipeline.prediction_pipeline import PredictionPipeline
import os

# Define the text input schema
class TextInput(BaseModel):
    text: str

app = FastAPI()

@app.get("/", tags=['Root'])
async def index():
    """Redirect to the API documentation."""
    return RedirectResponse(url="/docs")

@app.get("/train", tags=['Training'])
async def training():
    """Endpoint to trigger model training."""
    try:
        os.system("python main.py")
        return JSONResponse(content={"message": "Training completed successfully"})
    except Exception as e:
        return JSONResponse(content={"error": f"Error occurred during training: {e}"}, status_code=500)

@app.post("/predict", tags=['Prediction'])
async def predict_route(input: TextInput):
    """Endpoint to generate a summary for the provided text."""
    try:
        # Initialize the PredictionPipeline and make a prediction
        obj = PredictionPipeline()
        summary = obj.predict(input.text)
        
        # Check for unexpected tokens or error messages in the summary
        if "<n>" in summary or "Error:" in summary:
            raise ValueError("Summary generation failed due to unexpected response content.")
        
        # Clean up summary by replacing newline characters
        summary = summary.replace("\n", " ")
        
        return JSONResponse(content={"summary": summary})
    except ValueError as ve:
        return JSONResponse(content={"error": str(ve)}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"error": "Could not generate summary. Please try again."}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
