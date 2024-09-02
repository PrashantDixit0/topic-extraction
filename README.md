# From Calls to Insights: Topic Extraction from Contact Center Calls
1. The extraction graph creates an endpoint which accepts audio files and transcribes them using OpenAI's Whisper model
2. The transcription is fed into an LLM for Topic Extraction.
3. The transcription is fed into a summarization model to summarize the entire transcript.

## Code Reference
1. `graph.yaml` - contains the extraction graph.
2. `setup_graph.py` - Sets up the extraction graph in Indexify Server
3. `upload_and_retrieve.py` - Uploads audio into the extraction graph, waits for extraction and finally retrieves from the endpoint.

## Download & Start Indexify Server
```
curl https://getindexify.ai | sh
./indexify server -d
```

## Download & Join Indexify Extractors
adds OPENAI_API_KEY too, don't forget to change placeholder for it in following code.
```
virtualenv ve
source ve/bin/activate

pip install indexify-extractor-sdk
indexify-extractor download tensorlake/whisper-asr
indexify-extractor download tensorlake/summarization
indexify-extractor download tensorlake/openai
export OPENAI_API_KEY="sk-..."
indexify-extractor join-server
```
## Demo App
Now you are ready to run Streamlit app.
![demo](https://github.com/user-attachments/assets/2a8450da-a954-4b6d-bef4-7d16e8bce31c)

Run following code
```python3
streamlit run app.py
```
