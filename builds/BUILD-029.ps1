$Root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)

$VersionFile = Join-Path $Root "config\version.json"
$BuildLog = Join-Path $Root "logs\build_history.csv"

if(!(Test-Path $VersionFile))
{
@'
{
    "project":"SEOS",
    "version":"0.2.0",
    "build":"029",
    "status":"Development"
}
'@ | Set-Content -Encoding UTF8 $VersionFile
}

if(!(Test-Path $BuildLog))
{
"Date,Build,Status" | Set-Content -Encoding UTF8 $BuildLog
}

$Date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Add-Content $BuildLog "$Date,029,SUCCESS"

Write-Host ""
Write-Host "======================================="
Write-Host " BUILD-029 COMPLETED"
Write-Host "======================================="
Write-Host ""
Write-Host "Version File Created"
Write-Host "Build History Started"
Write-Host ""