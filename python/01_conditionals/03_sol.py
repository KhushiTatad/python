score = 78

if score >= 101:
    print("Please Varify Your Grade Again")
    exit()
    
if score < 60:
    print("Your Grade Is F As Your Score Is :", score)
elif score < 70:
    print("Your Grade Is D As Your Score Is :", score)
elif score < 80:
    print("Your Grade Is C As Your Score Is :", score)
elif score < 90:
    print("Your Grade Is B As Your Score Is :", score)
else:
    print("Your Grade Is A As Your Score Is :", score)
