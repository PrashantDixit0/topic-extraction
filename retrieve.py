from indexify import IndexifyClient

client = IndexifyClient()

def retrieve(file_path):
    content_id = client.upload_file("topic_extraction", file_path)
    client.wait_for_extraction(content_id)
    transcription = client.get_extracted_content(content_id, "topic_extraction", "transcription")
    summary = client.get_extracted_content(content_id, "topic_extraction", "summarization")
    topics_extracted = client.get_extracted_content(content_id, "topic_extraction", "topics")
    return transcription, summary, topics_extracted
