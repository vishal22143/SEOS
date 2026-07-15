Clear-Host

function Pause-SEOS {
    Write-Host ""
    Read-Host "Press ENTER to continue"
}

while ($true) {

    Clear-Host

    Write-Host "====================================================="
    Write-Host "        SHOURYA ENGINEERING OS (SEOS)"
    Write-Host "              Developer Console v1.0"
    Write-Host "====================================================="
    Write-Host ""
    Write-Host "1. Repository Status"
    Write-Host "2. Git Status"
    Write-Host "3. Repository Tree"
    Write-Host "4. Run Tests"
    Write-Host "5. Install Requirements"
    Write-Host "6. Run SEOS"
    Write-Host "7. Git Add"
    Write-Host "8. Git Commit"
    Write-Host "9. Git Push"
    Write-Host "10. Exit"
    Write-Host ""

    $choice = Read-Host "Select Option"

    switch ($choice) {

        "1" {
            Get-Location
            python --version
            git status
            Pause-SEOS
        }

        "2" {
            git status
            Pause-SEOS
        }

        "3" {
            tree /F
            Pause-SEOS
        }

        "4" {
            pytest -q
            Pause-SEOS
        }

        "5" {
            pip install -r requirements.txt
            Pause-SEOS
        }

        "6" {
            python seos.py
            Pause-SEOS
        }

        "7" {
            git add .
            git status
            Pause-SEOS
        }

        "8" {
            $msg = Read-Host "Commit Message"
            git commit -m "$msg"
            Pause-SEOS
        }

        "9" {
            git push origin main
            Pause-SEOS
        }

        "10" {
            break
        }

        default {
            Write-Host "Invalid Option"
            Pause-SEOS
        }
    }
}