@echo off
setlocal EnableExtensions

set "SELF=%~f0"
set "WRAPPER=%TEMP%\git_command_wrapper_%RANDOM%%RANDOM%.ps1"

> "%WRAPPER%" (
    echo param([string]^$path^)
    echo ^$content = Get-Content -Raw -Path ^$path -Encoding UTF8
    echo ^$marker = [regex]::Match(^$content, "`r?`n:__PS_PAYLOAD__`r?`n"^)
    echo if (-not ^$marker.Success^) { Write-Error "PowerShell payload marker not found."; exit 1 }
    echo ^$payload = ^$content.Substring(^$marker.Index + ^$marker.Length^)
    echo Invoke-Expression ^$payload
    echo exit ^$LASTEXITCODE
)

powershell.exe -NoLogo -ExecutionPolicy Bypass -File "%WRAPPER%" "%SELF%"
set "ERR=%ERRORLEVEL%"
del "%WRAPPER%" >nul 2>&1
exit /b %ERR%

:__PS_PAYLOAD__
# Git Helper Script (PowerShell payload generated from git_command.sh functionality)

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git command was not found. Please install Git and ensure it is on PATH."
    exit 1
}

$LogFile = Join-Path -Path $HOME -ChildPath "git_helper.log"

function Write-HelperLog {
    param([string]$Message)

    $timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    Add-Content -Path $LogFile -Value "$timestamp - $Message"
}

function Invoke-GitCommand {
    param(
        [Parameter(Mandatory)]
        [string[]]$Arguments,
        [string]$Description
    )

    if (-not $Description) {
        $Description = "git " + ($Arguments -join " ")
    }

    Write-Host "Running: $Description" -ForegroundColor Cyan
    & git @Arguments
    $exitCode = $LASTEXITCODE

    if ($exitCode -eq 0) {
        Write-Host "Success" -ForegroundColor Green
        Write-HelperLog "SUCCESS: $Description"
    } else {
        Write-Host "Failed (exit code $exitCode)" -ForegroundColor Red
        Write-HelperLog "FAILED: $Description (exit $exitCode)"
    }
}

function Show-Header {
    Write-Host "===============================" -ForegroundColor Yellow
    Write-Host "       Git Helper Script" -ForegroundColor Yellow
    Write-Host "===============================" -ForegroundColor Yellow
}

function Show-Menu {
    Write-Host "1. git status"
    Write-Host "2. git add (specify path)"
    Write-Host "3. git commit"
    Write-Host "4. git push"
    Write-Host "5. git pull (normal or --rebase)"
    Write-Host "6. git log"
    Write-Host "7. git branch"
    Write-Host "8. git checkout (target branch)"
    Write-Host "9. git merge (target branch)"
    Write-Host "10. git stash"
    Write-Host "11. git remote -v"
    Write-Host "12. git diff"
    Write-Host "13. git stash -> git pull --rebase -> git stash pop"
    Write-Host "14. enforce LF (Ubuntu) line endings"
    Write-Host "15. git fetch"
    Write-Host "16. git reset (unstage / undo commit)"
    Write-Host "h. Help"
    Write-Host "0. Exit"
}

function Show-Help {
    Write-Host "Git Helper Script - Help" -ForegroundColor Green
    Write-Host "---------------------------------"
    Write-Host "1. git status         : Show repository status"
    Write-Host "2. git add (path)     : Stage the specified path (default '.')"
    Write-Host "3. git commit         : Choose UpDaTe / single-line / editor flow"
    Write-Host "4. git push           : Push changes to the remote"
    Write-Host "5. git pull           : Pull normally or with --rebase"
    Write-Host "6. git log            : Show commit history"
    Write-Host "7. git branch         : List branches"
    Write-Host "8. git checkout       : Switch to the specified branch"
    Write-Host "9. git merge          : Merge the specified branch"
    Write-Host "10. git stash         : Stash current work in progress"
    Write-Host "11. git remote -v     : Show configured remotes"
    Write-Host "12. git diff          : Show diffs"
    Write-Host "13. git stash -> git pull --rebase -> git stash pop"
    Write-Host "    Temporarily stash changes, rebase pull from origin/main, then pop"
    Write-Host "14. enforce LF line endings : Set core.autocrlf=false and renormalize"
    Write-Host "15. git fetch         : Fetch remote updates without merging"
    Write-Host "16. git reset         : Unstage files or undo commits"
    Write-Host "h. Help               : Show this help"
    Write-Host "0. Exit               : Quit the script"
    Write-Host "---------------------------------"
}

function Invoke-GitAddPath {
    $path = Read-Host "Enter path to add (default: .)"
    if ([string]::IsNullOrWhiteSpace($path)) {
        $path = "."
    }

    Invoke-GitCommand -Arguments @("add", $path) -Description "git add $path"
}

function Invoke-GitCommit {
    Write-Host "Choose commit mode:"
    Write-Host "0) Default commit message: ""UpDaTe<datetime>"""
    Write-Host "1) Single-line commit message"
    Write-Host "2) Use default editor (multi-line)"
    $choice = Read-Host "Select commit mode [0,1,2] (default: 0)"

    if ([string]::IsNullOrWhiteSpace($choice)) {
        $choice = "0"
    }

    switch ($choice) {
        "0" {
            $datetime = Get-Date -Format "yyyyMMdd_HHmmss"
            $msg = "UpDaTe_$datetime"
            Write-Host "Using default commit message: ""$msg""" -ForegroundColor Cyan
            Invoke-GitCommand -Arguments @("commit", "-m", $msg) -Description "git commit -m ""$msg"""
        }
        "1" {
            $msg = Read-Host "Enter commit message (default: ""UpDaTe<datetime>"")"
            if ([string]::IsNullOrWhiteSpace($msg)) {
                $datetime = Get-Date -Format "yyyyMMdd_HHmmss"
                $msg = "UpDaTe_$datetime"
                Write-Host "Using default commit message: ""$msg""" -ForegroundColor Cyan
            }
            Invoke-GitCommand -Arguments @("commit", "-m", $msg) -Description "git commit -m ""$msg"""
        }
        "2" {
            Write-Host "Opening editor for commit message..." -ForegroundColor Cyan
            Invoke-GitCommand -Arguments @("commit") -Description "git commit (editor)"
        }
        Default {
            Write-Host "Invalid choice for commit message. Skipped." -ForegroundColor Red
        }
    }
}

function Invoke-StashPullRebase {
    Write-Host "Stash local changes, pull with rebase (origin/main), and pop stash."
    Invoke-GitCommand -Arguments @("stash") -Description "git stash"
    Invoke-GitCommand -Arguments @("pull", "--rebase", "origin", "main") -Description "git pull --rebase origin main"

    # stash pop前にstashが存在するか確認
    $stashList = git stash list 2>$null
    if ($stashList) {
        Invoke-GitCommand -Arguments @("stash", "pop") -Description "git stash pop"
    } else {
        Write-Host "No stash entries to pop." -ForegroundColor Yellow
        Write-HelperLog "INFO: No stash entries to pop"
    }
}

function Invoke-GitReset {
    Write-Host "Choose reset mode:"
    Write-Host "0) Unstage all files (git reset HEAD)"
    Write-Host "1) Unstage specific file"
    Write-Host "2) Soft reset last commit (keep changes staged)"
    Write-Host "3) Mixed reset last commit (keep changes unstaged)"
    Write-Host "4) Cancel"
    $resetChoice = Read-Host "Select reset mode [0-4] (default: 4)"

    if ([string]::IsNullOrWhiteSpace($resetChoice)) {
        $resetChoice = "4"
    }

    switch ($resetChoice) {
        "0" {
            Invoke-GitCommand -Arguments @("reset", "HEAD") -Description "git reset HEAD"
        }
        "1" {
            $filePath = Read-Host "Enter file path to unstage"
            if ([string]::IsNullOrWhiteSpace($filePath)) {
                Write-Host "File path is required. Skipped." -ForegroundColor Red
            } else {
                Invoke-GitCommand -Arguments @("reset", "HEAD", $filePath) -Description "git reset HEAD $filePath"
            }
        }
        "2" {
            Invoke-GitCommand -Arguments @("reset", "--soft", "HEAD~1") -Description "git reset --soft HEAD~1"
        }
        "3" {
            Invoke-GitCommand -Arguments @("reset", "--mixed", "HEAD~1") -Description "git reset --mixed HEAD~1"
        }
        "4" {
            Write-Host "Reset cancelled." -ForegroundColor Yellow
        }
        Default {
            Write-Host "Invalid choice. Skipped." -ForegroundColor Red
        }
    }
}

function Invoke-EnforceLFEndings {
    Write-Host "Applying Windows/Ubuntu compatible Git settings..." -ForegroundColor Cyan

    $gitattributes = @'
# Keep text normalized in Git, then choose safe working-tree endings.
* text=auto

# Unix/Linux scripts must stay LF so they run correctly on Ubuntu.
*.sh text eol=lf
*.bash text eol=lf

# Source and web content are safest as LF across Windows and Ubuntu.
*.py text eol=lf
*.html text eol=lf
*.htm text eol=lf
*.css text eol=lf
*.js text eol=lf
*.json text eol=lf
*.md text eol=lf
*.txt text eol=lf
*.ipynb text eol=lf
*.yml text eol=lf
*.yaml text eol=lf

# Windows command files should keep CRLF in the working tree.
*.bat text eol=crlf
*.cmd text eol=crlf
*.ps1 text eol=crlf

# Binary files must never be line-ending normalized.
*.pdf binary
*.png binary
*.jpg binary
*.jpeg binary
*.gif binary
*.webp binary
*.ico binary
*.woff binary
*.woff2 binary
*.ttf binary
*.otf binary
*.zip binary
'@

    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText((Join-Path (Get-Location) ".gitattributes"), $gitattributes + [Environment]::NewLine, $utf8NoBom)

    Invoke-GitCommand -Arguments @("config", "core.autocrlf", "false") -Description "git config core.autocrlf false"
    Invoke-GitCommand -Arguments @("config", "core.eol", "lf") -Description "git config core.eol lf"
    Invoke-GitCommand -Arguments @("config", "core.filemode", "false") -Description "git config core.filemode false"

    if (Test-Path -Path "git_command_2512.sh") {
        Invoke-GitCommand -Arguments @("update-index", "--chmod=+x", "git_command_2512.sh") -Description "git update-index --chmod=+x git_command_2512.sh"
    }

    if (Test-Path -Path "git_command_2512.cmd") {
        Invoke-GitCommand -Arguments @("update-index", "--chmod=-x", "git_command_2512.cmd") -Description "git update-index --chmod=-x git_command_2512.cmd"
    }

    Invoke-GitCommand -Arguments @("add", "--renormalize", ".") -Description "git add --renormalize ."
    Invoke-GitCommand -Arguments @("add", ".gitattributes") -Description "git add .gitattributes"

    Write-Host ""
    Write-Host "Verification:" -ForegroundColor Yellow
    & git ls-files --eol git_command_2512.sh git_command_2512.cmd .gitattributes 2>$null
    & git ls-files -s git_command_2512.sh git_command_2512.cmd .gitattributes 2>$null
    & git status --short

    Write-Host ""
    Write-Host "Expected: .sh is i/lf w/lf and 100755; .cmd is w/crlf and 100644." -ForegroundColor Yellow
    Write-Host "If the output looks correct, commit the normalization." -ForegroundColor Yellow
}

while ($true) {
    Show-Header
    Show-Menu
    $choice = Read-Host "Choose an option"

    switch ($choice) {
        "1"  { Invoke-GitCommand -Arguments @("status") -Description "git status" }
        "2"  { Invoke-GitAddPath }
        "3"  { Invoke-GitCommit }
        "4"  { Invoke-GitCommand -Arguments @("push") -Description "git push" }
        "5"  {
            Write-Host "Choose pull method:"
            Write-Host "  0) Normal pull (default)"
            Write-Host "  1) Pull with rebase"
            $pullChoice = Read-Host "Select pull mode [0 or 1] (default: 0)"
            if ([string]::IsNullOrWhiteSpace($pullChoice)) {
                $pullChoice = "0"
            }

            switch ($pullChoice) {
                "0" { Invoke-GitCommand -Arguments @("pull") -Description "git pull" }
                "1" { Invoke-GitCommand -Arguments @("pull", "--rebase") -Description "git pull --rebase" }
                Default { Write-Host "Invalid choice for pull method. Skipped." -ForegroundColor Red }
            }
        }
        "6"  { Invoke-GitCommand -Arguments @("log") -Description "git log" }
        "7"  { Invoke-GitCommand -Arguments @("branch") -Description "git branch" }
        "8"  {
            $branch = Read-Host "Enter branch name"
            if ([string]::IsNullOrWhiteSpace($branch)) {
                Write-Host "Branch name is required." -ForegroundColor Red
            } else {
                Invoke-GitCommand -Arguments @("checkout", $branch) -Description "git checkout $branch"
            }
        }
        "9"  {
            $mergeBranch = Read-Host "Enter branch to merge"
            if ([string]::IsNullOrWhiteSpace($mergeBranch)) {
                Write-Host "Branch name is required." -ForegroundColor Red
            } else {
                Invoke-GitCommand -Arguments @("merge", $mergeBranch) -Description "git merge $mergeBranch"
            }
        }
        "10" { Invoke-GitCommand -Arguments @("stash") -Description "git stash" }
        "11" { Invoke-GitCommand -Arguments @("remote", "-v") -Description "git remote -v" }
        "12" { Invoke-GitCommand -Arguments @("diff") -Description "git diff" }
        "13" { Invoke-StashPullRebase }
        "14" { Invoke-EnforceLFEndings }
        "15" { Invoke-GitCommand -Arguments @("fetch") -Description "git fetch" }
        "16" { Invoke-GitReset }
        "h"  { Show-Help }
        "H"  { Show-Help }
        "0"  {
            Write-Host "Exiting Git Helper..." -ForegroundColor Green
            Write-HelperLog "Exited Git Helper"
            break
        }
        Default {
            Write-Host "Invalid choice. Please try again." -ForegroundColor Red
        }
    }

    Write-Host ""
}
