

def login_required(func):
  def decorated(info):
    if info == 'login_user':
      print('상태 : login')
      return func(info)
    else:
      print('상태 : logout')
  return decorated


@login_required
def user_detail(info):
  print('detail한 정보')


user_detail('login_user')


def has_owner_ship(func):
  def decorated(target, user,instance):
    if user == target:
      print("상태 : 본인")
      func(target,user,instance)
    else:
      print("상태 : 타인")
      print("접근 금지")
  return decorated

@has_owner_ship
def user_detail2(target,user,instance):
  print("detail한 정보")

user_detail2('user_pk=2', 'user_pk=1', 'instance')

user_detail2('user_pk=2', 'user_pk=2', 'instance')


    




      

