# FileFlow

A safe, script-based file management command-line tool with virtual pre-simulation and automatic rollback capabilities.

---

## Key Features

- **Virtual Tree Simulation**: Pre-validates multi-step TOML scripts in an in-memory virtual file system before modifying disk, catching errors and missing dependencies early.
- **Targeted Delta Backup & Auto-Rollback**: Automatically snapshots affected files prior to destructive operations with instant rollback on failure and an `undo` command.
- **Strict Workspace Sandboxing**: Keeps all file operations securely bounded within a designated workspace directory.
- **Smart Collision Handling**: Supports `--soft-force` (`-sf`) to auto-rename duplicates without data loss, alongside standard `--force` (`-f`).
- **Zero External Dependencies**: Built natively using Python 3.12+ standard libraries (`tomllib`, `argparse`, `pathlib`, `shutil`, `fnmatch`).

---

## Installation & Setup

FileFlow requires **Python >= 3.12**.

### Using `uv`
```bash
# Clone the repository
git clone https://github.com/S-Astralcoder/FileFlow.git
cd FileFlow

# Install dependencies and editable package
uv sync
```

### Using `pip`
```bash
pip install -e .
```

---

## CLI Usage

```bash
fileflow [-ws WORKSPACE] [-f] <command> [options]
```

### Global Options
- `-ws, --workspace <path>`: Root workspace directory (default: `.`).
- `-f, --force`: Bypasses safety guards and confirms destructive actions.

---

### Commands Overview

#### 1. Create File or Directory
```bash
# Create a file
fileflow create -f path/to/file.txt

# Create a directory recursively
fileflow create -d -r path/to/nested/dir
```

#### 2. Copy Items
```bash
# Safe copy with collision auto-renaming (-sf)
fileflow copy -f -sf source.txt backup/source.txt

# Copy a directory
fileflow copy -d src_dir/ dest_dir/
```

#### 3. Move Items
```bash
fileflow move -f old_name.txt new_name.txt
```

#### 4. Delete Items
```bash
# Delete a specific file or directory (creates backup automatically)
fileflow delete -f temp.log
fileflow delete -d temp_folder/
```

#### 5. Pattern-based Deletion (`gdelete`)
```bash
# Delete all .tmp files under cache/
fileflow gdelete -f cache "*.tmp"
```

#### 6. Extract / Flatten Files (`extract`)
```bash
# Find and flatten all .png files under modules/ into assets/
fileflow extract modules "*.png" assets/
```

#### 7. Script Execution (`script`)
```bash
# Dry-run / test simulation without touching disk
fileflow script recipe.toml --dry-run

# Run full simulation and execute
fileflow script recipe.toml
```

#### 8. Undo Recent Action
```bash
# Restore previous state from backup
fileflow undo
```

---

## Scripting with TOML

FileFlow recipes let you define and chain multi-step workspace automations safely:

```toml
[metadata]
name = "Workspace Cleanup"
version = "1.0.0"
workspace = "."

[[actions]]
type = "create"
file = false
directory = true
recursive = true
item = "archive/logs"

[[actions]]
type = "move"
file = false
directory = false
source = "temp_output.log"
destination = "archive/logs/temp_output.log"
soft_force = true

[[actions]]
type = "gdelete"
file = true
directory = false
source = "cache"
pattern = "*.tmp"
```

---

## License

This project is licensed under the [MIT License](LICENSE).
