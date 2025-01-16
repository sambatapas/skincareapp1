'use client'

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"

type UserData = {
  skinType: string;
  waterIntake: string;
  currentProducts: string;
}

export default function SkinCareTest() {
  const [step, setStep] = useState(0)
  const [userData, setUserData] = useState<UserData>({
    skinType: '',
    waterIntake: '',
    currentProducts: ''
  })
  const [result, setResult] = useState('')

  const handleNext = () => {
    if (step === 0 && userData.skinType) {
      setStep(1)
    } else if (step === 1 && userData.waterIntake && userData.currentProducts) {
      setStep(2)
      setResult(getRecommendation(userData))
    }
  }

  const handlePrevious = () => {
    if (step > 0) {
      setStep(step - 1)
    }
  }

  const getRecommendation = (data: UserData) => {
    let recommendation = `Based on your ${data.skinType} skin type, `

    switch (data.skinType) {
      case 'dry':
        recommendation += 'use a gentle, creamy cleanser and a rich, hydrating moisturizer. '
        break
      case 'oily':
        recommendation += 'choose a foaming cleanser and a lightweight, oil-free moisturizer. '
        break
      case 'combination':
        recommendation += 'use a balanced cleanser and a lightweight moisturizer, applying a heavier cream on dry areas. '
        break
      case 'normal':
        recommendation += 'use a mild cleanser and a medium-weight moisturizer. '
        break
      case 'sensitive':
        recommendation += 'opt for fragrance-free, hypoallergenic products including a gentle cleanser and soothing moisturizer. '
        break
    }

    recommendation += 'Always use a broad-spectrum sunscreen daily. '

    if (data.waterIntake === 'low') {
      recommendation += 'Try to increase your daily water intake to improve skin hydration. '
    }

    return recommendation
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <Card className="w-full max-w-lg">
        <CardHeader>
          <CardTitle className="text-2xl font-bold text-center">Simple Skincare Test</CardTitle>
        </CardHeader>
        <CardContent>
          {step === 0 && (
            <div className="space-y-4">
              <RadioGroup 
                value={userData.skinType} 
                onValueChange={(value) => setUserData({...userData, skinType: value})}
              >
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="dry" id="dry" />
                  <Label htmlFor="dry">Dry</Label>
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="oily" id="oily" />
                  <Label htmlFor="oily">Oily</Label>
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="combination" id="combination" />
                  <Label htmlFor="combination">Combination</Label>
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="normal" id="normal" />
                  <Label htmlFor="normal">Normal</Label>
                </div>
                <div className="flex items-center space-x-2">
                  <RadioGroupItem value="sensitive" id="sensitive" />
                  <Label htmlFor="sensitive">Sensitive</Label>
                </div>
              </RadioGroup>
            </div>
          )}
          {step === 1 && (
            <div className="space-y-4">
              <h2 className="text-lg font-semibold">Additional Information</h2>
              <div className="space-y-2">
                <Label htmlFor="waterIntake">How much water do you drink daily?</Label>
                <RadioGroup 
                  value={userData.waterIntake} 
                  onValueChange={(value) => setUserData({...userData, waterIntake: value})}
                >
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="low" id="low" />
                    <Label htmlFor="low">Less than 4 cups</Label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="moderate" id="moderate" />
                    <Label htmlFor="moderate">4-8 cups</Label>
                  </div>
                  <div className="flex items-center space-x-2">
                    <RadioGroupItem value="high" id="high" />
                    <Label htmlFor="high">More than 8 cups</Label>
                  </div>
                </RadioGroup>
              </div>
              <div className="space-y-2">
                <Label htmlFor="currentProducts">What skincare products are you currently using?</Label>
                <Input 
                  id="currentProducts" 
                  value={userData.currentProducts}
                  onChange={(e) => setUserData({...userData, currentProducts: e.target.value})}
                  placeholder="E.g., cleanser, moisturizer, sunscreen"
                />
              </div>
            </div>
          )}
          {step === 2 && (
            <div className="space-y-4">
              <h2 className="text-lg font-semibold">Your Skincare Recommendation</h2>
              <p>{result}</p>
            </div>
          )}
        </CardContent>
        <CardFooter className="flex justify-between">
          {step > 0 && step < 2 && (
            <Button onClick={handlePrevious} variant="outline">
              Previous
            </Button>
          )}
          {step < 2 ? (
            <Button 
              onClick={handleNext} 
              disabled={
                (step === 0 && !userData.skinType) || 
                (step === 1 && (!userData.waterIntake || !userData.currentProducts))
              } 
              className={step === 0 ? "ml-auto" : ""}
            >
              {step === 1 ? "Get Recommendation" : "Next"}
            </Button>
          ) : (
            <Button onClick={() => {setStep(0); setUserData({skinType: '', waterIntake: '', currentProducts: ''}); setResult('')}} className="ml-auto">
              Start Over
            </Button>
          )}
        </CardFooter>
      </Card>
    </div>
  )
}

