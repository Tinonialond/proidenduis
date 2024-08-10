def get_files_with_comments(service):
    # List all files
    results = service.files().list(
        q="mimeType='application/vnd.example-apps.document'",
        pageSize=100,
        fields="nextPageToken, files(id, name)"
    ).execute()

    files = results.get('files', [])

    # List to hold FileIDs with comments
    files_with_comments = []

    for file in files:
        file_id = file['id']
        try:
            # Retrieve the comments for each file
            comments = service.comments().list(fileId=file_id).execute()
            
            if comments.get('comments', []):
                files_with_comments.append(file_id)
        except Exception as e:
            print(f"Error retrieving comments for file {file_id}: {e}")

    return files_with_comments

if __name__ == '__main__':
    files_with_comments = get_files_with_comments(service)
    print("Files with comments:", files_with_comments)
