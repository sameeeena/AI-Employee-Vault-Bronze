# Process Task Skill

This skill handles the processing of tasks within the AI employee system.
 Process Task Skill

  Name: process_task

  Purpose:
  - Scan /Needs_Action folder
  - For each file:
    - Read content
    - Follow Company_Handbook.md rules
    - Generate a short action summary
    - Mark task as completed
    - Move file to /Done

  Constraints:
  - Do NOT delete files
  - Do NOT execute external actions
  - Only work within the vault
  - Keep logic simple (Bronze level)

  Parameters:
  - None

  Output:
  - Short action summary for each processed file
  - Files moved from /Needs_Action to /Done folder

  Execution Flow:
  1. Scan /Needs_Action directory for files
  2. For each file found:
  a. Read file content
  b. Apply rules from Company_Handbook.md
  c. Generate short action summary
  d. Mark original file as completed
  e. Move file to /Done directory
  3. Return list of processed items with summaries

  Files Operated On:
  - Input: Files in /Needs_Action folder
  - Reference: Company_Handbook.md for rule application
  - Output: Moved files to /Done folder with action summaries
