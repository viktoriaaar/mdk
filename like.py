class Post(object):
  def __init__(self,nic,time,likes,text,comment):
    self.nic = nic
    self.time = time
    self.likes = likes
    self.text = text
    self.comment = comment
  def like(self):
    self.likes += 1
  def __str__(self):
    return f'Никнейм пользователя- {self.nic}, Время публикации- {self.time}, Количество лайков- {self.likes}, Текст сообщения- {self.text}, Список комментариев- {self.comment}' 
p = Post(input(), input(), int(input()),input(), input())
print(p.like())
print(p)
