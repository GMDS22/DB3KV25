param(
    [Parameter(Mandatory = $true)]
    [string]$SpeechKey,

    [Parameter(Mandatory = $true)]
    [string]$SpeechRegion
)

if ([string]::IsNullOrWhiteSpace($SpeechKey)) {
    throw "SpeechKey is required."
}
if ([string]::IsNullOrWhiteSpace($SpeechRegion)) {
    throw "SpeechRegion is required."
}

# Current shell session (effective immediately for this terminal).
$env:AZURE_SPEECH_KEY = $SpeechKey
$env:AZURE_SPEECH_REGION = $SpeechRegion

# Persist for future shells for the current Windows user.
setx AZURE_SPEECH_KEY "$SpeechKey" | Out-Null
setx AZURE_SPEECH_REGION "$SpeechRegion" | Out-Null

Write-Host "Azure Speech environment variables configured."
Write-Host "Current session: AZURE_SPEECH_KEY and AZURE_SPEECH_REGION are set."
Write-Host "Persisted for future terminals via setx."
