q=['1.what i capital of india!',
   '2.what is national animal of india!',
  '3.what is capital of karnatka!',
  '4.which is ths cleanest city in india',
  '5.which is the silicon city in india']
ans=['delhi','tiger','banglore','indore','banglore']
for x in q:
    print(x)
    user_ans=input('enter ths anser:').lower()
    if user_ans in ans:
        print('correct ans')
    else:
        print('wrong ans')