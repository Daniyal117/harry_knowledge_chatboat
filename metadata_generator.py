import os
import json

def metadata_generation():
    processed_dir = "processed"  # Directory where book text files are stored
    metadata = []

    # Iterate over each book file
    for file_name in os.listdir(processed_dir):
        if file_name.endswith(".txt"):
            file_path = os.path.join(processed_dir, file_name)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Extract book and chapter names
            book_name = None
            chapters = []
            
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if line.startswith("Book:"):
                    book_name = line.replace("Book:", "").strip()
                elif line.startswith("Chapter:"):
                    chapter_name = line.replace("Chapter:", "").strip()
                    chapter_text = "\n".join(lines[i+1:]).strip()  # Rest of the text is the chapter content
                    
                    chapters.append({
                        "book_name": book_name,
                        "chapter_name": chapter_name,
                        "file_path": file_path,
                        "chapter_text": chapter_text
                    })

            # Add extracted metadata
            metadata.extend(chapters)

    # Save metadata
    with open("metadata.json", "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    print("✅ Metadata generated successfully!")
    return 