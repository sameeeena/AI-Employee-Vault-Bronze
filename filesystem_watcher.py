# import os
# import time
# import shutil
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler


# class ActionFolderHandler(FileSystemEventHandler):
#     def __init__(self, action_folder, done_folder, handbook_file):
#         self.action_folder = action_folder
#         self.done_folder = done_folder
#         self.handbook_file = handbook_file

#     def on_created(self, event):
#         if not event.is_directory:
#             print(f"File detected: {event.src_path}")
#             self.process_file(event.src_path)

#     def on_moved(self, event):
#         if not event.is_directory:
#             print(f"File moved to action folder: {event.dest_path}")
#             self.process_file(event.dest_path)

#     def process_file(self, file_path):
#         """Process a file according to company handbook rules"""
#         # Wait briefly to ensure file write is complete
#         time.sleep(1)
#         try:
#             # Read the file content
#             with open(file_path, 'r', encoding='utf-8') as f:
#                 content = f.read()

#             print(f"Processing file: {os.path.basename(file_path)}")

#             # Generate a short action summary (placeholder logic)
#             summary = self.generate_summary(content)

#             # Print the summary
#             print(f"Action Summary for {os.path.basename(file_path)}:")
#             print(summary)
#             print("-" * 50)

#             # Move file to Done folder
#             filename = os.path.basename(file_path)
#             destination = os.path.join(self.done_folder, filename)
            
#             # Handle duplicate filenames in destination
#             if os.path.exists(destination):
#                 base, ext = os.path.splitext(filename)
#                 timestamp = int(time.time())
#                 destination = os.path.join(self.done_folder, f"{base}_{timestamp}{ext}")

#             shutil.move(file_path, destination)
#             print(f"Moved {filename} to Done folder")

#         except Exception as e:
#             print(f"Error processing file {file_path}: {str(e)}")

#     def generate_summary(self, content):
#         """Generate a short action summary based on content"""
#         # This is a simplified implementation
#         # In a real scenario, this would apply rules from the handbook
#         lines = content.split('\n')
#         summary = "Action Summary:\n"
#         summary += f"- File contained {len(lines)} lines\n"
#         summary += f"- First line: {lines[0][:50] if len(lines) > 0 else 'Empty'}\n"
#         summary += "- Task processed according to company handbook\n"
#         return summary


# def setup_folders(base_dir):
#     """Create required folders if they don't exist"""
#     needs_action = os.path.join(base_dir, "Needs_Action")
#     done = os.path.join(base_dir, "Done")
#     handbook = os.path.join(base_dir, "Company_Handbook.md")

#     os.makedirs(needs_action, exist_ok=True)
#     os.makedirs(done, exist_ok=True)

#     # Ensure handbook exists
#     if not os.path.exists(handbook):
#         with open(handbook, 'w') as f:
#             f.write("# Company Handbook\n\nBasic company policies and procedures.\n")

#     return needs_action, done, handbook


# if __name__ == "__main__":
#     # Get the directory where this script is located
#     base_dir = os.path.dirname(os.path.abspath(__file__))

#     # Setup required folders
#     action_folder, done_folder, handbook_file = setup_folders(base_dir)

#     # Create event handler
#     event_handler = ActionFolderHandler(action_folder, done_folder, handbook_file)

#     # Create observer
#     observer = Observer()
#     observer.schedule(event_handler, action_folder, recursive=False)

#     # Start watching
#     observer.start()
#     print(f"Started watching {action_folder} for new files...")

#     # Process existing files
#     print("Checking for existing files...")
#     for filename in os.listdir(action_folder):
#         file_path = os.path.join(action_folder, filename)
#         if os.path.isfile(file_path):
#             print(f"Found existing file: {filename}")
#             event_handler.process_file(file_path)

#     print("Press Ctrl+C to stop.")

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#         print("\nStopping file watcher...")

#     observer.join()

import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

BASE_DIR = Path(__file__).parent.resolve()
INBOX = BASE_DIR / "Inbox"
NEEDS_ACTION = BASE_DIR / "Needs_Action"

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        print("New file detected:", event.src_path)

        source = Path(event.src_path)
        destination = NEEDS_ACTION / source.name

        shutil.copy2(source, destination)

        print("Copied to Needs_Action:", destination)

if __name__ == "__main__":
    INBOX.mkdir(exist_ok=True)
    NEEDS_ACTION.mkdir(exist_ok=True)

    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, str(INBOX), recursive=False)
    observer.start()

    print("Watching Inbox folder...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()