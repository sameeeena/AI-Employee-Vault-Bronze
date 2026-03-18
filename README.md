# AI Employee Vault [Bronze]

A file-based autonomous task management system built on Obsidian vaults. This Bronze-level implementation provides a simple yet effective framework for an AI employee to process, track, and manage tasks automatically.

## 📁 Project Structure

```
AI_Employee_vault[Bronze]/
├── commands.md              # Command reference for running scripts and tasks
├── filesystem_watcher.py    # Watches Inbox folder and copies new files to Needs_Action
├── process_task.py          # Processes tasks from Needs_Action and moves to Done
├── Company_Handbook.md/     # Directory containing company rules and policies
│   └── company_Handbook.md  # Core rules for communication, safety, and task handling
├── Dasboard.md/             # Directory containing dashboard statistics
│   └── dashbord.md          # Task statistics and recent activity log
├── Inbox/                   # Incoming task files (watched by filesystem_watcher.py)
├── Needs_Action/            # Tasks pending processing
├── Done/                    # Completed and processed tasks
└── skills/                  # Skill definitions for AI agent capabilities
    └── process_task/
        └── SKILL.md         # Process task skill specification
```

## 🚀 Features

- **Automated File Watching**: Monitors the `Inbox` folder for new task files
- **Task Processing Pipeline**: Moves tasks through Inbox → Needs_Action → Done
- **Company Handbook Integration**: Applies defined rules during task processing
- **Dashboard Updates**: Tracks completed tasks and activity logs
- **Skill-Based Architecture**: Modular skill system for extensible AI capabilities

## 📋 How It Works

### Task Flow

1. **Create Task**: Add a new file to the `Inbox/` folder
2. **Auto-Copy**: `filesystem_watcher.py` detects and copies it to `Needs_Action/`
3. **Process**: Run `process_task.py` to process all files in `Needs_Action/`
4. **Complete**: Files are moved to `Done/` with summaries generated
5. **Update**: Dashboard statistics are automatically updated

### Company Handbook Rules

The system follows these core principles:

- **Communication**: Professional and polite, never emotional
- **Safety**: Request approval when unsure, never delete files, always log actions
- **Task Handling**: Move completed tasks to `/Done`, keep incomplete in `/Needs_Action`

## 🛠️ Usage

### Start the File Watcher

```bash
python filesystem_watcher.py
```

This watches the `Inbox/` folder and automatically copies new files to `Needs_Action/`.

### Create a New Task

```bash
echo "prepare weekly report" > Inbox/task.txt
```

### Process Tasks

```bash
python process_task.py
```

This processes all files in `Needs_Action/`, applies handbook rules, and moves them to `Done/`.

### Using Skills

To use the process_task skill with an AI agent:

```
use the process_task skill.
process all files in /Needs_Action.
move them to /Done.
update Dashboard.md.
```

## 📄 Configuration Files

### `commands.md`
Quick reference for common commands and operations.

### `skills/process_task/SKILL.md`
Defines the process_task skill specification including:
- Purpose and constraints
- Execution flow
- Input/output parameters
- Files operated on

## 🎯 Bronze Level Characteristics

This Bronze-level implementation features:
- Simple file-based task storage
- Basic folder structure (Inbox → Needs_Action → Done)
- Minimal dependencies (watchdog library)
- Straightforward processing logic
- No external API calls or complex integrations

## 📦 Requirements

- Python 3.x
- `watchdog` library (`pip install watchdog`)

## 📝 Notes

- Files are never deleted, only moved between folders
- All actions are logged for transparency
- Dashboard tracks active and completed task counts
- System operates entirely within the vault directory

## 🔧 Extending the System

To add new capabilities:
1. Create a new skill folder under `skills/`
2. Define the skill in `SKILL.md`
3. Implement corresponding Python logic
4. Update `commands.md` with usage instructions

---

**Status**: Bronze Level Implementation  
**Last Updated**: March 19, 2026
