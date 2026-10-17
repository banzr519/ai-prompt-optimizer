# Run from a reviewed checkout/archive; no execution-policy or security setting changes.
$ErrorActionPreference = 'Stop'
$forwardArgs = @($args)
if ($forwardArgs.Count -eq 0) { $forwardArgs = @('install', '--source', $PSScriptRoot) }
$scriptPath = Join-Path $PSScriptRoot 'scripts/manage_install.py'
if ($env:APO_PYTHON) {
    & $env:APO_PYTHON -c 'import sys; sys.exit(sys.version_info < (3,9))'
    if ($LASTEXITCODE -ne 0) { exit 1 }
    & $env:APO_PYTHON $scriptPath @forwardArgs
    exit $LASTEXITCODE
}
foreach ($candidate in @('python3', 'python', 'py')) {
    if (Get-Command $candidate -ErrorAction SilentlyContinue) {
        $prefixArgs = @()
        if ($candidate -eq 'py') { $prefixArgs = @('-3') }
        & $candidate @prefixArgs -c 'import sys; sys.exit(sys.version_info < (3,9))' 2>$null
        if ($LASTEXITCODE -eq 0) {
            & $candidate @prefixArgs $scriptPath @forwardArgs
            exit $LASTEXITCODE
        }
    }
}
Write-Error 'Python 3.9+ was not found. Ask Codex to locate a runtime, or set APO_PYTHON. Nothing was installed.'
exit 1
