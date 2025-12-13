# test-model.ps1
$body = @{
    Administrative               = 0
    Administrative_Duration      = 0.0
    Informational                = 0
    Informational_Duration       = 0.0
    ProductRelated               = 37
    ProductRelated_Duration      = 5.25641
    BounceRates                  = 0.020767196
    ExitRates                    = 0.054225865
    PageValues                   = 10.0
    SpecialDay                   = 0.0
    OperatingSystems             = 1
    Browser                      = 1
    Region                       = 8
    TrafficType                  = 1
    Weekend                      = 1
    VisitorType_New_Visitor      = 0
    VisitorType_Other            = 0
    VisitorType_Returning_Visitor = 1
    Month_Aug                    = 0
    Month_Dec                    = 0
    Month_Feb                    = 0
    Month_Jul                    = 0
    Month_June                   = 0
    Month_Mar                    = 0
    Month_May                    = 0
    Month_Nov                    = 1
    Month_Oct                    = 0
    Month_Sep                    = 0
} | ConvertTo-Json

try {
    $response = Invoke-RestMethod -Uri "http://localhost/api/predict" -Method Post -Body $body -ContentType "application/json"
    Write-Host "✅ Успех:" -ForegroundColor Green
    $response | ConvertTo-Json
}
catch {
    Write-Host "❌ Ошибка:" -ForegroundColor Red
    Write-Host $_.Exception.Response.StatusCode
    Write-Host $_.ErrorDetails.Message
}