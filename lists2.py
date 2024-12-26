corr_ans=0
wronge_ans=0
q=['1.what i capital of india!',
   '2.what is national animal of india!',
  '3.what is capital of karnatka!',
  '4.which is ths cleanest city in india',
  '5.which is the silicon city in india']
ans=['delhi','tiger','banglore','indore','banglore']
for x in range (len(q)):
    print(q[x])
    user_ans=input('enter ths anser:').lower()
    if user_ans==ans[x]:
        corr_ans+=1
        print('correct ans')
        print('percentage',((corr_ans/(corr_ans+wronge_ans))*100))
    else:
        wronge_ans+=1
        print('percentage',((corr_ans/(corr_ans+wronge_ans))*100))