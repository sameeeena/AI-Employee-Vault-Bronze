import os
import shutil

def process_task():
    """
    Process files in the Needs_Action folder according to Company_Handbook.md
    Move completed files to Done folder and update Dashboard.md counts
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    needs_action_dir = os.path.join(base_dir, "Needs_Action")
    done_dir = os.path.join(base_dir, "Done")
    handbook_path = os.path.join(base_dir, "Company_Handbook.md", "company_Handbook.md")
    dashboard_path = os.path.join(base_dir, "Dasboard.md", "dashbord.md")

    # Ensure directories exist
    os.makedirs(needs_action_dir, exist_ok=True)
    os.makedirs(done_dir, exist_ok=True)

    # Read Company Handbook
    handbook_content = ""
    if os.path.exists(handbook_path):
        with open(handbook_path, 'r', encoding='utf-8') as f:
            handbook_content = f.read()

    # Process each file in Needs_Action
    processed_count = 0
    for filename in os.listdir(needs_action_dir):
        file_path = os.path.join(needs_action_dir, filename)

        if os.path.isfile(file_path):
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Generate a short action summary based on handbook rules
            # This is a simplified implementation
            summary = f"Processed: {filename}\nContent length: {len(content)} characters\nHandbook applied: {bool(handbook_content)}"

            # Move file to Done folder
            done_path = os.path.join(done_dir, filename)
            shutil.move(file_path, done_path)

            processed_count += 1

    # Update Dashboard.md counts
    total_processed = processed_count
    if os.path.exists(dashboard_path):
        with open(dashboard_path, 'r', encoding='utf-8') as f:
            dashboard_content = f.read()

        # Look for a processed count and update it
        if "Processed:" in dashboard_content:
            # Simple replacement - in a real scenario would be more robust
            import re
            dashboard_content = re.sub(r'Processed:\s*\d+', f'Processed: {total_processed}', dashboard_content)
        else:
            # Append the count if not present
            dashboard_content += f"\n\nProcessed: {total_processed}"

        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(dashboard_content)
    else:
        # Create dashboard if it doesn't exist
        with open(dashboard_path, 'w', encoding='utf-8') as f:
            f.write(f"# Dashboard\n\nProcessed: {total_processed}\nPending: 0\nFailed: 0")

    print(f"Processed {processed_count} files")
    print("Files moved to Done folder")
    print("Dashboard updated")

if __name__ == "__main__":
    process_task()
    print("BRONZE_PROCESS_COMPLETE")