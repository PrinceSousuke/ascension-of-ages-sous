param(
    [string]$ModsPath = "mods",
    [string]$OutFile = "docs/modlist.md"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $ModsPath)) {
    throw "Mods path not found: $ModsPath"
}

$mods = Get-ChildItem -LiteralPath $ModsPath -Filter "*.jar" -File |
    Sort-Object Name |
    Select-Object Name, Length, LastWriteTime

$lines = @()
$lines += "# Installed Mod Jar List"
$lines += ""
$lines += "Generated from local jar filenames. This file is documentation only; jars are not redistributed by this repository."
$lines += ""
$lines += "| Mod jar | Size MB | Modified |"
$lines += "| --- | ---: | --- |"

foreach ($mod in $mods) {
    $sizeMb = [math]::Round($mod.Length / 1MB, 2)
    $modified = $mod.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")
    $safeName = $mod.Name.Replace("|", "\|")
    $lines += "| `$safeName` | $sizeMb | $modified |"
}

Set-Content -LiteralPath $OutFile -Value $lines -Encoding UTF8
Write-Host "Wrote $OutFile with $($mods.Count) mods."
