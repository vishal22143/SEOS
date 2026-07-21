param(
    [Parameter(Mandatory = $true)]
    [string]$Build
)

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
$BuildFolder = Join-Path $Root "builds"
$BuildFile = Join-Path $BuildFolder "$Build.ps1"

Write-Host ""
Write-Host "========================================"
Write-Host " SHOURYA ENGINEERING OS (SEOS)"
Write-Host "========================================"
Write-Host ""

# Check DFR

$DFR = Join-Path $Root "docs\Design\DFR\MASTER_DFR.md"

if(Test-Path $DFR)
{
    Write-Host "[OK] Design Freeze Register Found"
}
else
{
    Write-Host "[ERROR] Design Freeze Register Missing"
    exit
}

# Check Build File

if(Test-Path $BuildFile)
{
    Write-Host "[OK] Executing $Build"
    & $BuildFile
}
else
{
    Write-Host ""
    Write-Host "[ERROR] Build File Not Found"
    Write-Host $BuildFile
}